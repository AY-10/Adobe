import os
import json
import datetime
import fitz  # PyMuPDF
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_validate
from sentence_transformers import SentenceTransformer


def load_input_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_output_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def extract_spans_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    spans = []
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            for line in b.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if not text:
                        continue
                    spans.append({
                        "text": text,
                        "font_size": round(span["size"], 1),
                        "x": span["bbox"][0],
                        "y": span["bbox"][1],
                        "page_number": page_num,
                        "document": os.path.basename(pdf_path)
                    })
    return spans


def heuristic_label(spans):
    # Heading if short text mostly title case or ends with colon
    for s in spans:
        t = s["text"]
        if len(t) < 60 and (t.istitle() or t.endswith(':')):
            s["level"] = "Heading"
        else:
            s["level"] = "Body"
    return spans


def train_classifier(spans, model):
    texts = [s["text"] for s in spans]
    embeddings = model.encode(texts, batch_size=64, show_progress_bar=False)
    labels = [s["level"] for s in spans]
    le = LabelEncoder()
    y = le.fit_transform(labels)

    clf = LogisticRegression(max_iter=500)
    if len(set(y)) < 2:
        clf.fit(embeddings, y)  # Only one class present
    else:
        cross_validate(clf, embeddings, y, cv=5, scoring=["accuracy"])
        clf.fit(embeddings, y)
    return clf, le, embeddings


def classify_spans(clf, le, embeddings, spans):
    preds = clf.predict(embeddings)
    for s, p in zip(spans, preds):
        s["predicted_level"] = le.inverse_transform([p])[0]
    return spans


def group_spans_to_sections(spans):
    spans = sorted(spans, key=lambda s: (
        s["document"], s["page_number"], s["y"]))
    sections = []
    current_section = None

    for span in spans:
        level = span.get("predicted_level", span.get("level"))
        if level == "Heading":
            if current_section:
                sections.append(current_section)
            current_section = {
                "document": span["document"],
                "page_number": span["page_number"],
                "section_title": span["text"],
                "body_texts": [],
                "font_sizes": [span["font_size"]]
            }
        else:
            if current_section is None:
                current_section = {
                    "document": span["document"],
                    "page_number": span["page_number"],
                    "section_title": "",
                    "body_texts": [],
                    "font_sizes": []
                }
            current_section["body_texts"].append(span["text"])
            current_section["font_sizes"].append(span["font_size"])

    if current_section:
        sections.append(current_section)
    return sections


def rank_and_format_sections(sections, persona, job_to_be_done, input_docs):
    for s in sections:
        heading_score = 1 if s["section_title"].strip() else 0
        avg_font = sum(s["font_sizes"]) / \
            len(s["font_sizes"]) if s["font_sizes"] else 0
        body_len = sum(len(t) for t in s["body_texts"])
        s["importance"] = heading_score * 1000 + avg_font * 10 + body_len

    sections = sorted(
        sections, key=lambda s: (-s["importance"], s["page_number"]))
    extracted_sections = []
    subsection_analysis = []

    for rank, s in enumerate(sections[:5], start=1):
        title = s["section_title"].strip()
        if len(title) > 70:
            title = title[:67].rsplit(" ", 1)[0] + "..."
        body_text = " ".join(s["body_texts"]).strip()
        if len(body_text) > 400:
            body_text = body_text[:397].rsplit(" ", 1)[0] + "..."

        extracted_sections.append({
            "document": s["document"],
            "section_title": title,
            "importance_rank": rank,
            "page_number": s["page_number"]
        })
        subsection_analysis.append({
            "document": s["document"],
            "refined_text": body_text,
            "page_number": s["page_number"]
        })

    return {
        "metadata": {
            "input_documents": input_docs,
            "persona": persona,
            "job_to_be_done": job_to_be_done,
            "processing_timestamp": datetime.datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }


def main(collection_path):
    input_json_path = os.path.join(collection_path, "challenge1b_input.json")
    output_json_path = os.path.join(collection_path, "challenge1b_output.json")
    pdf_folder = os.path.join(collection_path, "PDFs")

    # Load input
    input_data = load_input_json(input_json_path)
    persona = input_data.get("persona", {}).get("role", "")
    job_to_be_done = input_data.get("job_to_be_done", {}).get("task", "")
    input_docs = [d["filename"] for d in input_data.get("documents", [])]

    all_spans = []
    for doc in input_docs:
        pdf_path = os.path.join(pdf_folder, doc)
        all_spans.extend(extract_spans_from_pdf(pdf_path))

    all_spans = heuristic_label(all_spans)

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    clf, le, embeddings = train_classifier(all_spans, model)
    all_spans = classify_spans(clf, le, embeddings, all_spans)

    sections = group_spans_to_sections(all_spans)

    output_data = rank_and_format_sections(
        sections, persona, job_to_be_done, input_docs)
    save_output_json(output_data, output_json_path)

    print(f"Processed collection at {collection_path}")
    print(f"Output saved to {output_json_path}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python process_collection.py <Collection_Folder_Path>")
        sys.exit(1)
    main(sys.argv[1])
