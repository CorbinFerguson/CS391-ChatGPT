import google.generativeai as genai
import config
import PIL.Image

genai.configure(api_key=config.GEMINI_API_KEY)

img = PIL.Image.open('zebra.jpg')
model = genai.GenerativeModel('gemini-1.5-flash')
#response = model.generate_content(img)

response = model.generate_content(["Count how many zebras are in the provided image. Your response should be a number detailing how many there are.", img], stream=True)
response.resolve()

print(response.text)



