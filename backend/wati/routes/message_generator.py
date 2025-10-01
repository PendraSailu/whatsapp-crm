from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

def generate_message(prompt: str) -> str:
    text = prompt.lower()
    if "diwali" in text:
        return "Hello {name}, Diwali greetings! We wish you the best holiday. Namaste!"
    elif "new year" in text:
        return "Hello {name}, Happy New Year! Wishing you joy, success, and prosperity!"
    elif "birthday" in text:
        return "Hello {name}, wishing you a wonderful birthday filled with happiness!"
    else:
        return f"Hello {{name}}, {prompt}"

@router.post("/generate-message")
def generate_prompt_message(req: PromptRequest):
    return {"prompt": req.prompt, "message": generate_message(req.prompt)}
