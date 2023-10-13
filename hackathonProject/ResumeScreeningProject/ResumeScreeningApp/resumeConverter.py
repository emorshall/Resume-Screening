import docx
import os
import re

email_id = ""
phone_num = ""
def emailContact(emails, phones):
    global email_id
    global phone_num
    if len(emails) > 0:
        print("Email addresses found:")
        for email in emails:
            print(email)
            email_id = email

    if len(phones) > 0:
        print("\nPhone numbers found:")
        for phone in phones:
            print(phone)
            phone_num=phone


def ResumeScreening(uploaded_file, skills):
    """
    :param skills:
    :return:
    """
    path = f"C:/Users/prabhu.jaypal.nadar/Hackathon/Resume"
    name = uploaded_file.name
    file_path = f"{path}/{name}"
    print(file_path)
    docx_file = file_path
    doc = docx.Document(docx_file)
    text = ""

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    # Regular expression pattern for phone numbers (a simple example, you can adjust it based on your needs)
    phone_pattern = r'[0-9]{10}'

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    with open("C:/Users/prabhu.jaypal.nadar/Hackathon/Resume/resume_txt.txt", "w") as txt:
        txt.write(text)

        skill_present = set()
        match_keyword = []

    with open("C:/Users/prabhu.jaypal.nadar/Hackathon/resume_txt.txt", "r") as text_file:
        lines = text_file.readlines()
        for line in lines:
            emails = re.findall(email_pattern, line)
            phones = re.findall(phone_pattern, line)
            emailContact(emails, phones)
            for keywords in skills:
                if keywords in line.lower():
                    match_keyword.append(keywords)
                    skill_present.add(keywords)

    required_count = len(skills)
    actual_count = len(skill_present)

    result_in_per = (actual_count / required_count) * 100
    result = {
        'result_in_per': result_in_per,
        'skills': skill_present,
        'email_id': email_id,
        'phone_num': phone_num,
    }
    text_file.close()

    path = os.path.join("C:/Users/prabhu.jaypal.nadar/Hackathon/resume_txt.txt")
    os.remove(path)
    print("The file has been removed")
    return result
