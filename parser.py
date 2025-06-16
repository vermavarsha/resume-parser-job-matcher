import fitz
from docx import Document
import re


#extract text and upload resume
def extract_text(file):
    if file.name.endswith(".docx"):
        doc = Document(file)
        full_text=[]
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    elif file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text=""
        for page in doc:
            text+=page.get_text()
        return text
    else:
        return ""


def extract_details(text):
    # Email extraction using labeled format
    email_match = re.search(r'Email:\s*([^\s]+@[^\s]+)', text, re.I)
    email = email_match.group(1) if email_match else "N/A"

    # Phone number extraction (handles +1, dashes, spaces)
    phone_match = re.search(r'Phone:\s*([\+\d][\d\s\-()]+)', text, re.I)
    phone = phone_match.group(1).strip() if phone_match else "N/A"

    # Skills extraction from "Skills:" section
    skills_match = re.search(r'Skills:\s*(.+)', text, re.I)
    if skills_match:
        skill_line = skills_match.group(1)
        skills = [skill.strip().lower() for skill in skill_line.split(',')]
    else:
        skills = []


    # Experience section: get lines under 'Experience'
    experience_match = re.search(r'Experience:\s*(.*?)\n(?:Education:|$)', text, re.I | re.S)
    if experience_match:
        experience_lines = experience_match.group(1).strip().split('\n')
        experience_lines = [line.strip('-• ').strip() for line in experience_lines if line.strip()]
    else:
        experience_lines = []

    # Extract years of experience (e.g., "3 years")
    year_match = re.search(r'(\d+)\s+years?', text, re.I)
    years_of_experience = year_match.group(1) + " years" if year_match else "N/A"

    # Education section: get lines under 'Education'
    education_match = re.search(r'Education:\s*(.*)', text, re.I | re.S)
    if education_match:
        education_lines = education_match.group(1).strip().split('\n')
        education_lines = [line.strip('-• ').strip() for line in education_lines if line.strip()]
    else:
        education_lines = []

    return {
        "email": email,
        "phone": phone,
        "skills": skills,
        "experience": experience_lines,
        "years_of_experience": years_of_experience,
        "education": education_lines
    }
