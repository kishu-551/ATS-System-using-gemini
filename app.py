import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Configure the Google Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from the Google Generative AI
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from the uploaded PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_n in range(len(reader.pages)):
        page = reader.pages[page_n]
        text += str(page.extract_text())
    return text

# Input prompt for the Generative AI
input_prompt = """
Hey act like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst,
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide the best assistance
for improving the resumes. Assign the percentage matching based on JD (Job Description)
and the missing keywords with high accuracy.

I want the response in JSON structure like:
{
    "JD Match": "%",
    "Missing Keywords": [],
    "Profile Summary": ""
}
"""

# Streamlit app layout
st.title("Resume Screening Software (ATS)")
st.subheader("Match Your Resume Against the Job Description")

# Text area for the Job Description
jd = st.text_area("Paste the Job Description")

# File uploader for the resume PDF
uploaded_file = st.file_uploader("Upload your Resume", type="pdf", help="Please upload the PDF")

# Submit button
submit = st.button("Submit")

if submit:
    if uploaded_file:
        # Extract text from the uploaded resume PDF
        text = input_pdf_text(uploaded_file)
        
        # Get response from the Generative AI
        response = get_gemini_response([input_prompt, "Job Description\n" + jd, "Resume \n" + text])
        
        # Display a progress bar
        bar = st.progress(50)
        time.sleep(3)
        bar.progress(100)
        
        # Display the JSON response
        st.json(response)
