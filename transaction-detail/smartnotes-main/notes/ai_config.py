import google.generativeai as genai


# =========================================
# GEMINI API KEY
# =========================================

genai.configure(

    api_key="YOUR_GEMINI_API_KEY"
)


# =========================================
# GEMINI MODEL
# =========================================

model = genai.GenerativeModel(

    "gemini-1.5-flash"
)