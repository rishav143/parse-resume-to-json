import pdfplumber
import re
import json
import nltk

# Download NLTK data files (only need to run once)
nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

def parse_resume(text):
    resume_data = {
        "name": "",
        "contact": "",
        "email": "",
        "education": [],
        "experience": [],
        "skills": []
    }
    
    # Dummy regex patterns (You need to adjust these based on the resume format)
    name_pattern = r"Name:\s*(.*)"
    contact_pattern = r"Contact:\s*(.*)"
    email_pattern = r"Email:\s*(.*)"
    education_pattern = r"Education:\s*(.*)"
    experience_pattern = r"Experience:\s*(.*)"
    skills_pattern = r"Skills:\s*(.*)"
    
    # Extract details
    resume_data['name'] = re.findall(name_pattern, text)[0]
    resume_data['contact'] = re.findall(contact_pattern, text)[0]
    resume_data['email'] = re.findall(email_pattern, text)[0]
    
    education = re.findall(education_pattern, text)
    experience = re.findall(experience_pattern, text)
    skills = re.findall(skills_pattern, text)
    
    resume_data['education'] = [edu.strip() for edu in education]
    resume_data['experience'] = [exp.strip() for exp in experience]
    resume_data['skills'] = [skill.strip() for skill in skills]
    
    return resume_data

def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    resume_data = parse_resume(text)
    print(json.dumps(resume_data, indent=4))

if __name__ == "__main__":
    pdf_path = 'path/to/your/resume.pdf'
    main(pdf_path)