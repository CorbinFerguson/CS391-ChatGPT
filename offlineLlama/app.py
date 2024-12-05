import requests
import json

url = "http://localhost:11434/api/generate"

headers = { 
    "Content-Type": "application/json"
}

# Read the contents of the input file
with open("input.txt", "r", encoding="utf-8") as file:
    input_text = file.read()

data = {
    "model": "llama2",
    "prompt": "Summarize the attached text. The output should be only in French and should be simple enough for a 5th grader to understand.",
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_text = response.text 
    data = json.loads(response_text)
    actual_response = data["response"]
    print(actual_response)
else:
    print("Error:", response.status_code, response.text)

#Here is a summary of the text in French, written at a 5th grade level:
#Le texte parle des différents types de plantes qui existent. Il y a des plantes à floraison printanière comme la tulipe et le girasole, des plantes à feuilles comme le chardon et la fougère, et des plantes grimpantes comme la vigne et le lierre. Les plantes ont des besoins différents pour vivre, comme de l'eau, du soleil et de l'air. Elles peuvent également être utilisées pour guérir des maladies ou soigner les blessures.