import openai
import docx

docx_file = f"C:/Users/prabhu.jaypal.nadar/Hackathon/Krishna Kanth.docx"
doc = docx.Document(docx_file)
text = ""

for paragraph in doc.paragraphs:
    text += paragraph.text + "\n"

print("-----------------------------------------------------------")
# print(text)
print("-----------------------------------------------------------")
with open("C:/Users/prabhu.jaypal.nadar/Hackathon/resume_txt.txt", "w") as txt:
    txt.write(text)

api_key = ""

skill_keyword = ['html', 'react', 'javascript']

with open("C:/Users/prabhu.jaypal.nadar/Hackathon/resume_txt.txt", "r") as text_file:
    text_data = text_file.read()

    match = []

for key_words in skill_keyword:
    prompt = f"Find occurrences of '{key_words}' in the following text:\n{text_data}\n\nOccurrences:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        api_key=api_key
    )

    generated_text = response.choices[0].text.strip()
    match.append((key_words, generated_text))

skill_present = set()
for key_words, generated_text in match:
    occurrences = generated_text.splitlines()
    print(f"Skills Defined string: '{key_words}'")
    print()
    skill_present.add(key_words)
    for occurrence in occurrences:
        print(occurrence)
text_file.close()
print(skill_present)
