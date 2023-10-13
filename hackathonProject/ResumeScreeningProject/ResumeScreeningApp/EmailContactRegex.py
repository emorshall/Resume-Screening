import openai
import docx


def read_docx(file_path):
    doc = docx.Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)


docx_file_path = 'your_docx_file.docx'  # Replace with your DOCX file path
docx_text = read_docx(docx_file_path)


def extract_names(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Extract names from the following text:\n{text}\n\nNames:",
        max_tokens=50,  # Adjust as needed
        temperature=0.7  # Adjust for creativity vs. accuracy
    )
    names = response.choices[0].text.strip()
    return names


extracted_names = extract_names(docx_text)
print("Extracted Names:")
print(extracted_names)
