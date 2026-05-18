from .ai_config import model


# =========================================
# AI CATEGORY PREDICTION
# =========================================

def predict_category(text):

    text_lower = text.lower()

    # =====================================
    # FOOD
    # =====================================

    food_keywords = [

        "pizza",
        "burger",
        "food",
        "restaurant",
        "cafe",
        "coffee",
        "tea",
        "biryani",
        "lunch",
        "dinner",
    ]

    # =====================================
    # TRAVEL
    # =====================================

    travel_keywords = [

        "uber",
        "ola",
        "bus",
        "train",
        "flight",
        "taxi",
        "petrol",
        "fuel",
    ]

    # =====================================
    # ENTERTAINMENT
    # =====================================

    entertainment_keywords = [

        "movie",
        "netflix",
        "spotify",
        "game",
        "cinema",
    ]

    # =====================================
    # BILLS
    # =====================================

    bills_keywords = [

        "electricity",
        "water",
        "internet",
        "bill",
        "recharge",
    ]

    # =====================================
    # HEALTH
    # =====================================

    health_keywords = [

        "hospital",
        "medicine",
        "doctor",
        "clinic",
    ]

    # =====================================
    # EDUCATION
    # =====================================

    education_keywords = [

        "book",
        "course",
        "college",
        "school",
        "fees",
    ]

    # =====================================
    # KEYWORD MATCHING
    # =====================================

    for word in food_keywords:

        if word in text_lower:

            return "Food"

    for word in travel_keywords:

        if word in text_lower:

            return "Travel"

    for word in entertainment_keywords:

        if word in text_lower:

            return "Entertainment"

    for word in bills_keywords:

        if word in text_lower:

            return "Bills"

    for word in health_keywords:

        if word in text_lower:

            return "Health"

    for word in education_keywords:

        if word in text_lower:

            return "Education"

    # =====================================
    # GEMINI FALLBACK
    # =====================================

    prompt = f"""

Categorize this expense into ONE category only.

Categories:
Food
Travel
Shopping
Entertainment
Bills
Health
Education
Other

Expense:
{text}

Return ONLY category name.

"""

    try:

        response = model.generate_content(
            prompt
        )

        category = response.text.strip()

        return category

    except Exception as e:

        print(e)

        return "Other"