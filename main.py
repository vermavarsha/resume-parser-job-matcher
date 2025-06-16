import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from parser import extract_text, extract_details
from matcher import match_resumes_to_jobs


st.set_page_config(page_title="Resume Matcher", layout="wide")

# Load model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

#UI
st.title("📄 Resume Matcher & Parser")

# Upload resumes
st.sidebar.header("Upload Resumes (PDF or DOCX)")
uploaded_resumes = st.sidebar.file_uploader("Choose resume files", type=["pdf", "docx"], accept_multiple_files=True)

# Enter job descriptions
st.sidebar.header("Add Job Descriptions")
job_titles = st.sidebar.text_area("Job Titles (comma-separated)", "Data Analyst Intern, Backend Developer")
job_texts = st.sidebar.text_area("Job Descriptions (separated by ---)", 
    """Looking for someone skilled in Python, SQL, data analysis, and visualization.
---
Must know Java, Spring Boot, APIs, and database systems.""")

#extract name
def extract_name (text):
  lines=text.split('\n')
  for line in lines:
    tokens=word_tokenize(line)
    tagged=pos_tag(tokens)
    for i in range(len(tagged)-1):
      if tagged[i][1]=='NNP' and tagged[i+1][1]=='NNP':
        return " ".join([tagged[i][0],tagged[i+1][0]])
  return None


if st.sidebar.button("Run Matcher"):
    # Process resumes
    resumes = []
    for file in uploaded_resumes:
        text = extract_text(file)
        info = extract_details(text)
        resumes.append({
            "name": extract_name(text) or file.name.split('.')[0].title(),
            "text": text,
            **info
        })

    # Process jobs
    job_titles = [j.strip() for j in job_titles.split(",")]
    job_texts = [j.strip() for j in job_texts.split("---")]
    job_descriptions = [{"title": title, "text": desc} for title, desc in zip(job_titles, job_texts)]

    results = match_resumes_to_jobs(resumes, job_descriptions)
    df = pd.DataFrame(results)

    st.subheader("📊 Match Results")
    st.dataframe(df, use_container_width=True)

    # Optional download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "resume_job_matches.csv", "text/csv")
