'''
Project Description
    In this project, we will build a program that extracts text from a PDF document.

Prerequisites
    Required Libraries: PyPDF2
                        pip install pypdf2
'''
import PyPDF2

with open("11.Extract Text from PDF.pdf","rb") as file:
    reader=PyPDF2.PdfReader(file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()+"\n"

print(text)