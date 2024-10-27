from dotenv import load_dotenv
load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import fitz  # PyMuPDF
import google.generativeai as genai

# Configure the Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Helper Function: Get AI Response
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

# Helper Function: Convert PDF to Image
def convert_pdf_to_image(pdf_data):
    pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
    page = pdf_document.load_page(0)  # Get the first page
    pix = page.get_pixmap()
    
    img_byte_arr = io.BytesIO(pix.tobytes(output="png"))
    img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
    
    return img_base64

# PDF Processing Function
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_data = uploaded_file.read()
        pdf_image_base64 = convert_pdf_to_image(pdf_data)
        pdf_parts = [
            {
                "mime_type": "image/png",
                "data": pdf_image_base64  # image as base64 string
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App
st.set_page_config(page_title="ATS Resume Expert (Updated)")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Buttons
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")
submit_write_resume = st.button("Write Perfect Resume")

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Provide a match percentage, list the missing keywords, and provide final thoughts.
"""

# New Prompt for Writing the Perfect Resume
write_resume_prompt = """
You are an experienced resume writer with expertise in creating resumes optimized for Applicant Tracking Systems (ATS).
Using only the skills and relevant experience from the provided resume, and analyzing the job description, rewrite and enhance the resume.
Make sure to improve the candidate's strengths and align the resume with the job description without including job requirements such as qualifications, experience requirements, or salary information.
Focus on optimizing the candidate's profile to match the job description and highlight key strengths for the role.
"""

# Button Action: "Tell Me About the Resume"
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt1)
        st.subheader("Response:")
        st.write(response)
    else:
        st.write("Please upload the resume.")

# Button Action: "Percentage Match"
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt3)
        st.subheader("Response:")
        st.write(response)
    else:
        st.write("Please upload the resume.")

# Button Action: "Write Perfect Resume"
# Button Action: "Write Perfect Resume"
elif submit_write_resume:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, write_resume_prompt)
        st.subheader("Generated Perfect Resume:")
        st.write(response)
    else:
        st.write("Please upload the resume.")

