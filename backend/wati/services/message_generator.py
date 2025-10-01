# services/message_generator.py
import random

def generate_message(prompt: str, name: str = "{name}") -> str:
    """
    Generates a predefined message based on user prompt.
    """
    templates = {
        "diwali": [
            f"Hello {name}, wishing you a very Happy Diwali! 🪔✨",
            f"Dear {name}, may your Diwali be full of lights, happiness, and prosperity!",
            f"Namaste {name}, Diwali greetings! We wish you the best holiday."
        ],
        "new year": [
            f"Happy New Year {name}! 🎉 Wishing you success and happiness ahead.",
            f"Cheers to 2025 {name}! May this year bring joy and growth.",
        ],
        "default": [
            f"Hello {name}, thank you for being with us!",
            f"Dear {name}, we appreciate your support always."
        ]
    }

    prompt = prompt.lower()
    if "diwali" in prompt:
        return random.choice(templates["diwali"])
    elif "new year" in prompt:
        return random.choice(templates["new year"])
    else:
        return random.choice(templates["default"])
