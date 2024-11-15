import google.generativeai as genai

KEY_API = ""
genai.configure(api_key=KEY_API)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("traduit chien en anglais, la reponse ne doit contenir que la reponse")
print(response.text)