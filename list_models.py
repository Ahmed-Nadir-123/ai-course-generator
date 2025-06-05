import google.generativeai as genai

genai.configure(api_key="AIzaSyCSofsvvNBMp-Ivq8DRgF0yv_ayxbcIxVU")
models = genai.list_models()
for m in models:
    print(m.name)
