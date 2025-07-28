# Challenge 1B: Persona Document Intelligence

This project processes collections of PDF documents to extract, classify, and rank important sections based on a given persona and job-to-be-done. It uses machine learning and heuristics to identify headings and body text, then outputs structured JSON summaries for each collection.

## Features

- Extracts text spans from PDFs using PyMuPDF
- Heuristically and ML-based classification of headings vs. body text
- Groups spans into logical sections
- Ranks and summarizes the most important sections per collection
- Outputs results in a structured JSON format

## Requirements

- Python 3.8+
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/)
- [sentence-transformers](https://www.sbert.net/)

Install dependencies:

```bash
pip install pymupdf scikit-learn sentence-transformers
```

## Folder Structure

```
process_collection.py
utils.py
Collection 1/
    challenge1b_input.json
    challenge1b_output.json
    PDFs/
        ...PDF files...
Collection 2/
    ...
Collection 3/
    ...
```

## Usage

Run the script on a collection folder:

```bash
python process_collection.py <Collection_Folder_Path>
```

Example:

```bash
python process_collection.py "Collection 1"
```

- The script reads `challenge1b_input.json` and PDFs from the specified collection folder.
- It writes the output to `challenge1b_output.json` in the same folder.

## Input JSON Format (`challenge1b_input.json`)

```json
{
  "persona": { "role": "..." },
  "job_to_be_done": { "task": "..." },
  "documents": [{ "filename": "file1.pdf" }, { "filename": "file2.pdf" }]
}
```

## Output JSON Format (`challenge1b_output.json`)

- Contains metadata, extracted section summaries, and subsection analyses.
