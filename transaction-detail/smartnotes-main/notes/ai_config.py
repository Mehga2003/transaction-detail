from decouple import config
import google.generativeai as genai


genai.configure(

    api_key=config(
        'GEMINI_API_KEY'
    )
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)