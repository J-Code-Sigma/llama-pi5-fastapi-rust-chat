# FastAPI/filter.py
from better_profanity import profanity

# Load default words
profanity.load_censor_words()

# You can also add custom words if needed
CUSTOM_BAD_WORDS = ["how to build a bomb", "explosives", "illegal drugs"]
profanity.add_censor_words(CUSTOM_BAD_WORDS)

def is_harmful(prompt: str) -> bool:
    """
    Checks if a prompt contains any blocked keywords using better-profanity.
    """
    return profanity.contains_profanity(prompt)
