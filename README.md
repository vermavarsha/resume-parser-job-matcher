# 📄 Resume Parser + Job Matcher using Sentence-BERT

This project matches uploaded resumes to job descriptions using **Semantic Similarity** via **Sentence-BERT** and provides a **Streamlit UI** for easy interaction.

---

## 🌐 Live Demo

🔗 [Click here to try the app](https://resume-parser-job-matcher-7gjuz42zi35pkunvcseckj.streamlit.app/)  

---

## 🚀 Features

- ✅ Upload multiple resumes (`.pdf`, `.docx`)
- ✅ Auto-extract candidate details (name, email, phone, skills)
- ✅ Add multiple job descriptions and titles
- ✅ Compute semantic similarity using **Sentence-BERT**
- ✅ View, rank, and download match results as CSV

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **NLP**: [Sentence-Transformers](https://www.sbert.net/)
- **Parsing**: `PyMuPDF`, `docx`, `re`
- **Languages**: Python

---

## 📦 Installation

```bash
# 1. Clone the repo
git clone https://github.com/vermavarsha/resume-parser-job-matcherr.git
cd resume-parser-job-matcher

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run main.py


---
## 📂 Project Structure

resume-matcher/
│
├── parser.py              # Resume text & detail extraction
├── matcher.py             # BERT embedding + similarity logic
├── main.py                # UI logic (Streamlit)
├── requirements.txt       # Dependencies
├── README.md              # Project info
└── resumes/               # Optional: local test resumes

📄 Example Input
Resumes:

PDF/DOCX with candidate profile

Jobs:

Job titles: Data Analyst, Backend Developer

Job descriptions (separated by ---):

Looking for someone with Python, SQL, and visualization.
  ---
Must know Java, Spring Boot, REST APIs, databases.
```
--- 

## 📊 Output
Resume matches for each job

Candidate name, skills,experience, email, phone

Match percentage score

Downloadable .csv

---

## 💡 Future Enhancements
Resume tagging/classification

GloVe/BERT fine-tuning


