# Adobe India Hackathon 2025

## Welcome to the "Connecting the Dots" Challenge

### Rethink Reading. Rediscover Knowledge

What if every time you opened a PDF, it didn't just sit there—it spoke to you, connected ideas, and narrated meaning across your entire library?

That's the future we're building — and we want you to help shape it.

In the Connecting the Dots Challenge, your mission is to reimagine the humble PDF as an intelligent, interactive experience—one that understands structure, surfaces insights, and responds to you like a trusted research companion.

### The Journey Ahead

**Round 1:**
Kick things off by building the brains — extract structured outlines from raw PDFs with blazing speed and pinpoint accuracy. Then, power it up with on-device intelligence that understands sections and links related ideas together.

**Round 2:**
It's showtime! Build a beautiful, intuitive reading webapp using Adobe's PDF Embed API. You will be using your Round 1 work to design a futuristic webapp.

### Why This Matters

In a world flooded with documents, what wins is not more content — it's context. You're not just building tools — you're building the future of how we read, learn, and connect. No matter your background — ML hacker, UI builder, or insight whisperer — this is your stage.

Are you in?

It's time to read between the lines. Connect the dots. And build a PDF experience that feels like magic. Let's go.

---

## Challenge Solutions

### [Challenge 1a: PDF Heading Extractor](./Challenge_1a/README.md)

**Machine Learning-Based PDF Structure Analysis with Docker Containerization**

A sophisticated tool that automatically extracts and classifies headings from PDF documents using font size analysis and machine learning classification. Now includes full Docker containerization for easy deployment and consistent execution across different environments.

**Key Features:**
- **Intelligent Extraction**: Uses PyMuPDF to extract text, font size, position, and page metadata
- **ML Classification**: Random Forest classifier trained on text features (length, case, positioning)
- **Hierarchical Structure**: Classifies headings into levels (Title, H1, H2, H3, H4)
- **JSON Output**: Generates structured outlines for each processed PDF
- **Complete Pipeline**: From raw PDFs to machine learning model to structured output
- **Docker Containerization**: Full containerized deployment with volume mounting for data persistence
- **Cross-Platform Scripts**: Windows (.bat) and Linux/Mac (.sh) runner scripts for easy operation

**Technology Stack:**
- Python 3.9 (Docker containerized)
- PyMuPDF (fitz) for PDF processing
- scikit-learn for machine learning
- pandas for data manipulation
- joblib for model persistence
- Docker & Docker Compose for containerization

**Deployment Options:**
1. **Docker (Recommended)**: Consistent environment with simple commands
2. **Local Installation**: Traditional Python setup for development

**Docker Workflow:**
1. **Build**: `run.bat build` or `./run.sh build`
2. **Start**: `run.bat start` or `./run.sh start`
3. **Process**: `run.bat process` or `./run.sh process`
4. **Train**: `run.bat train` or `./run.sh train`
5. **Predict**: `run.bat predict` or `./run.sh predict`

**Performance:** Achieves 75-90% accuracy depending on data quality, with detailed precision/recall metrics for each heading level.

### [Challenge 1b: Persona Document Intelligence](./Challenge_1b/challenge_1B_persona_document_intelligence/README.md)

**Advanced Multi-Collection PDF Analysis with Persona-Based Intelligence**

Processes collections of PDF documents to extract, classify, and rank important sections based on specific personas and job-to-be-done scenarios.

**Key Features:**
- **Persona-Driven Analysis**: Tailors content extraction to specific user roles and tasks
- **Multi-Collection Processing**: Handles diverse document collections with different use cases
- **Intelligent Classification**: Combines heuristic and ML-based approaches for heading/body classification
- **Section Ranking**: Ranks content by importance using font size, text length, and relevance
- **Structured Output**: Generates comprehensive JSON summaries with metadata and analysis

**Technology Stack:**
- Python 3.8+
- PyMuPDF for PDF text extraction
- scikit-learn for classification
- sentence-transformers for text embeddings
- Logistic Regression for ML classification

**Use Cases Demonstrated:**
1. **Travel Planning**: Extract relevant sections for trip planning from travel guides
2. **HR Documentation**: Identify key sections for form creation from software tutorials
3. **Menu Planning**: Surface relevant recipes and meal ideas for catering events

**Output Format:** Rich JSON structure containing metadata, extracted sections with importance rankings, and detailed subsection analysis.

---

## Project Structure

```
Adobe-India-Hackathon25/
├── README.md                                    # This file
├── Challenge_1a/                                # PDF Heading Extractor
│   ├── README.md                               # Detailed documentation
│   ├── process_pdfs.py                        # PDF processing script
│   ├── requirements.txt                       # Python dependencies
│   ├── Dockerfile                             # Docker container configuration
│   ├── docker-compose.yml                     # Docker Compose configuration
│   ├── .dockerignore                          # Docker build exclusions
│   ├── run.bat                                # Windows Docker runner script
│   ├── run.sh                                 # Linux/Mac Docker runner script
│   ├── ml/                                    # Machine learning components
│   │   ├── train_model.py                     # Model training
│   │   ├── predict_headings.py                # Prediction script
│   │   ├── prepare_labeling_csv.py            # Data preparation
│   │   └── model.pkl                          # Trained model
│   └── dataset/                               # Data and outputs
│       ├── pdfs/                              # Training PDFs
│       ├── new_pdfs/                          # New PDFs for prediction
│       └── outputs/                           # Generated outputs
└── Challenge_1b/                               # Persona Document Intelligence
    └── challenge_1B_persona_document_intelligence/
        ├── README.md                          # Project documentation
        ├── process_collection.py              # Main processing script
        ├── utils.py                           # Utility functions
        ├── Collection 1/                      # Travel planning use case
        ├── Collection 2/                      # HR documentation use case
        └── Collection 3/                      # Menu planning use case
```

## Getting Started

### Prerequisites
- Python 3.7+ (Challenge 1a) or Python 3.8+ (Challenge 1b)
- pip (Python package installer)
- Docker Desktop (for Challenge 1a Docker deployment)

### Installation

**For Challenge 1a:**

**Option 1: Docker Installation (Recommended)**
```bash
cd Challenge_1a
# Build and start the container
run.bat build    # Windows
./run.sh build   # Linux/Mac
run.bat start    # Windows
./run.sh start   # Linux/Mac
```

**Option 2: Local Installation**
```bash
cd Challenge_1a
pip install -r requirements.txt
```

**For Challenge 1b:**
```bash
cd Challenge_1b/challenge_1B_persona_document_intelligence
pip install pymupdf scikit-learn sentence-transformers
```

### Quick Start

**Challenge 1a - Extract PDF Headings:**

**Docker Method (Recommended):**
```bash
cd Challenge_1a
run.bat build                             # Build container
run.bat start                             # Start container
run.bat process                           # Extract training data
run.bat prepare                           # Prepare data
run.bat train                             # Train model
run.bat predict                           # Predict on new PDFs
```

**Local Method:**
```bash
cd Challenge_1a
python process_pdfs.py                    # Extract training data
python ml/prepare_labeling_csv.py         # Prepare data
python ml/train_model.py                  # Train model
python ml/predict_headings.py             # Predict on new PDFs
```

**Challenge 1b - Process Document Collections:**
```bash
cd Challenge_1b/challenge_1B_persona_document_intelligence
python process_collection.py "Collection 1"  # Process travel planning
python process_collection.py "Collection 2"  # Process HR documentation
python process_collection.py "Collection 3"  # Process menu planning
```

## Innovation Highlights

### Challenge 1a Innovations
- **Font Size Hierarchy Analysis**: Intelligent detection of heading levels based on typography
- **Multi-Feature ML Classification**: Combines text characteristics with spatial positioning
- **End-to-End Pipeline**: Complete workflow from PDF processing to structured output
- **High Accuracy**: Achieves 75-90% accuracy with detailed performance metrics
- **Docker Containerization**: Full containerized deployment ensuring consistency across environments
- **Cross-Platform Scripts**: Automated runner scripts for Windows and Unix-based systems

### Challenge 1b Innovations
- **Persona-Driven Intelligence**: Context-aware content extraction based on user roles
- **Hybrid Classification**: Combines rule-based heuristics with machine learning
- **Importance Ranking**: Sophisticated algorithm for ranking content relevance
- **Multi-Domain Adaptability**: Handles diverse document types and use cases

## Future Enhancements

Both solutions are designed to be extensible and can be enhanced with:
- **Advanced NLP**: Integration with large language models for better understanding
- **Real-time Processing**: Web-based interfaces for instant PDF analysis
- **Cross-Document Linking**: Intelligent connections between related documents
- **Interactive Visualizations**: Rich UI for exploring document structures
- **API Integration**: RESTful services for enterprise deployment

---

**Note**: Each challenge directory contains detailed documentation and implementation details. Please refer to the individual README files for comprehensive information about each solution.

## Contributing

This project was developed for the Adobe India Hackathon 2025. The solutions demonstrate advanced PDF processing capabilities using machine learning and intelligent document analysis techniques.

## License

This project is part of the Adobe India Hackathon 2025 submission. 