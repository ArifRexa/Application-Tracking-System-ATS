# import openai
# from dotenv import load_dotenv
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image
# import fitz  # PyMuPDF
# # Configure the OpenAI API
# load_dotenv()
# # Configure the Generative AI
# # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# openai.api_key = os.getenv("OPENAI_API_KEY")
# # Helper Function: Get AI Response
# # Helper Function: Get AI Response using OpenAI
# def get_openai_response(input_text, pdf_content, prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",  # You can use "gpt-3.5-turbo" if needed
#         messages=[
#             {"role": "system", "content": prompt},
#             {"role": "user", "content": f"Job Description: {input_text}\nResume Content: {pdf_content[0]}"},
#         ]
#     )
#     return response['choices'][0]['message']['content']

# # Helper Function: Convert PDF to Image
# def convert_pdf_to_image(pdf_data):
#     pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
#     page = pdf_document.load_page(0)  # Get the first page
#     pix = page.get_pixmap()
    
#     img_byte_arr = io.BytesIO(pix.tobytes(output="png"))
#     img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
    
#     return img_base64

# # PDF Processing Function
# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         pdf_data = uploaded_file.read()
#         pdf_image_base64 = convert_pdf_to_image(pdf_data)
#         pdf_parts = [
#             {
#                 "mime_type": "image/png",
#                 "data": pdf_image_base64  # image as base64 string
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# # Streamlit App
# st.set_page_config(page_title="ATS Resume Expert (Updated)")
# st.header("ATS Tracking System (OpenAI API)")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")

# # Buttons
# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage Match")
# submit_write_resume = st.button("Write Perfect Resume")

# # Prompts
# input_prompt1 = """
# You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
# Please share your professional evaluation on whether the candidate's profile aligns with the role. 
# Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resume against the provided job description. Provide a match percentage, list the missing keywords, and provide final thoughts.
# """

# # New Prompt for Writing the Perfect Resume
# write_resume_prompt = """
# You are an experienced resume writer with expertise in creating resumes optimized for Applicant Tracking Systems (ATS).
# Using only the skills and relevant experience from the provided resume, and analyzing the job description, rewrite and enhance the resume.
# Make sure to improve the candidate's strengths and align the resume with the job description without including job requirements such as qualifications, experience requirements, or salary information.
# Focus on optimizing the candidate's profile to match the job description and highlight key strengths for the role.
# """

# # Button Action: "Tell Me About the Resume"
# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_openai_response(input_text, pdf_content, input_prompt1)
#         st.subheader("Response:")
#         st.write(response)
#     else:
#         st.write("Please upload the resume.")

# # Button Action: "Percentage Match"
# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_openai_response(input_text, pdf_content, input_prompt3)
#         st.subheader("Response:")
#         st.write(response)
#     else:
#         st.write("Please upload the resume.")

# # Button Action: "Write Perfect Resume"
# elif submit_write_resume:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_openai_response(input_text, pdf_content, write_resume_prompt)
#         st.subheader("Generated Perfect Resume:")
#         st.write(response)
#     else:
#         st.write("Please upload the resume.")






import openai
from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image
import fitz  # PyMuPDF

# Configure the OpenAI API
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Helper Function: Get AI Response using OpenAI
def get_openai_response(input_text, pdf_content, prompt):
    response = openai.ChatCompletion.create(
        model="chatgpt-4o-latest",  # You can use "gpt-3.5-turbo" if needed
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Job Description: {input_text}\nResume Content: {pdf_content[0]}"},
        ]
    )
    return response['choices'][0]['message']['content']

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
st.header("ATS Tracking System (OpenAI API)")
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
        response = get_openai_response(input_text, pdf_content, input_prompt1)
        st.subheader("Response:")
        st.write(response)
    else:
        st.write("Please upload the resume.")

# Button Action: "Percentage Match"
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_openai_response(input_text, pdf_content, input_prompt3)
        st.subheader("Response:")
        st.write(response)
    else:
        st.write("Please upload the resume.")

# Button Action: "Write
elif submit_write_resume:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_openai_response(input_text, pdf_content, write_resume_prompt)
        st.subheader("Generated Perfect Resume:")
        st.write(response)
    else:
        st.write("Please upload the resume.")







# import openai
# from dotenv import load_dotenv
# import base64
# import streamlit as st
# import os
# import io
# import fitz  # PyMuPDF
# import re

# # Configure the OpenAI API
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Helper Function: Get AI Response using OpenAI
# def get_openai_response(input_text, resume_content, prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",  # or use "gpt-3.5-turbo"
#         messages=[
#             {"role": "system", "content": prompt},
#             {"role": "user", "content": f"Job Description: {input_text}\nResume Content: {resume_content}"},
#         ]
#     )
#     return response['choices'][0]['message']['content']

# # Helper Function: Extract Text from PDF
# def extract_text_from_pdf(uploaded_file):
#     pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     text = ""
#     for page_num in range(pdf_document.page_count):
#         page = pdf_document.load_page(page_num)
#         text += page.get_text("text")
#     return text

# # Streamlit App
# st.set_page_config(page_title="ATS Resume Expert (Updated)")
# st.header("ATS Tracking System (OpenAI API)")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")
#     resume_content = extract_text_from_pdf(uploaded_file)

# # Buttons
# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage Match")
# submit_write_resume = st.button("Suggest Resume Improvements")

# # Prompts
# input_prompt1 = """
# You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
# Please share your professional evaluation on whether the candidate's profile aligns with the role. 
# Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resume against the provided job description. Provide a match percentage, list the missing keywords, and provide final thoughts.
# """

# # Prompt for Improving the Resume
# improve_resume_prompt = """
# You are an experienced resume writer. Using only the content of the provided resume, suggest improvements without changing the format. 
# Make sure to focus on adding missing keywords, improving weak sections, and aligning the resume better with the job description. 
# Provide clear suggestions while keeping the existing format intact.
# """

# # Button Action: "Tell Me About the Resume"
# if submit1:
#     if uploaded_file is not None:
#         response = get_openai_response(input_text, resume_content, input_prompt1)
#         st.subheader("Response:")
#         st.write(response)
#     else:
#         st.write("Please upload the resume.")

# # Button Action: "Percentage Match"
# elif submit3:
#     if uploaded_file is not None:
#         response = get_openai_response(input_text, resume_content, input_prompt3)
#         st.subheader("Response:")
#         st.write(response)
#     else:
#         st.write("Please upload the resume.")

# # Button Action: "Suggest Resume Improvements"
# elif submit_write_resume:
#     if uploaded_file is not None:
#         response = get_openai_response(input_text, resume_content, improve_resume_prompt)
#         st.subheader("Suggested Improvements:")
#         st.write(response)
#     else:
#         st.write("Please upload the resume.")







# With download button and suggesions

# import openai
# from dotenv import load_dotenv
# import base64
# import streamlit as st
# import os
# import io
# import fitz  # PyMuPDF

# # Configure the OpenAI API
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Helper Function: Get AI Response using OpenAI
# def get_openai_response(input_text, resume_content, prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",  # or use "gpt-3.5-turbo"
#         messages=[
#             {"role": "system", "content": prompt},
#             {"role": "user", "content": f"Job Description: {input_text}\nResume Content: {resume_content}"},
#         ]
#     )
#     return response['choices'][0]['message']['content']

# # Helper Function: Extract Text from PDF
# def extract_text_from_pdf(uploaded_file):
#     pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     text = ""
#     for page_num in range(pdf_document.page_count):
#         page = pdf_document.load_page(page_num)
#         text += page.get_text("text")
#     return text

# # Helper Function: Generate Downloadable File
# def download_button(data, file_name, label):
#     b64 = base64.b64encode(data.encode()).decode()
#     href = f'<a href="data:file/txt;base64,{b64}" download="{file_name}">{label}</a>'
#     return href

# # Streamlit App
# st.set_page_config(page_title="ATS Resume Expert (Updated)")
# st.header("ATS Tracking System (OpenAI API)")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")
#     resume_content = extract_text_from_pdf(uploaded_file)

# # Buttons
# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage Match")
# submit_write_resume = st.button("Improve Resume and Download")

# # Prompts
# input_prompt1 = """
# You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
# Please share your professional evaluation on whether the candidate's profile aligns with the role. 
# Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resume against the provided job description. Provide a match percentage, list the missing keywords, and provide final thoughts.
# """

# # Prompt for Improving the Resume
# improve_resume_prompt = """
# You are an experienced resume writer. Using only the content of the provided resume, rewrite it and suggest improvements. 
# Make sure to focus on adding missing keywords, improving weak sections, and aligning the resume better with the job description.
# Rewrite the resume with your suggestions while keeping the format intact.
# """

# # Button Action: "Tell Me About the Resume"
# if submit1:
#     if uploaded_file is not None:
#         response = get_openai_response(input_text, resume_content, input_prompt1)
#         st.subheader("Response:")
#         st.write(response)
#     else:
#         st.write("Please upload the resume.")

# # Button Action: "Percentage Match"
# elif submit3:
#     if uploaded_file is not None:
#         response = get_openai_response(input_text, resume_content, input_prompt3)
#         st.subheader("Response:")
#         st.write(response)
#     else:
#         st.write("Please upload the resume.")

# # Button Action: "Improve Resume and Download"
# elif submit_write_resume:
#     if uploaded_file is not None:
#         # Get the improved resume content
#         improved_resume = get_openai_response(input_text, resume_content, improve_resume_prompt)

#         # Display the improved resume in the app
#         st.subheader("Improved Resume:")
#         st.write(improved_resume)

#         # Create a download button for the improved resume
#         st.markdown(download_button(improved_resume, "Improved_Resume.txt", "Download Improved Resume as .txt"), unsafe_allow_html=True)
#     else:
#         st.write("Please upload the resume.")
