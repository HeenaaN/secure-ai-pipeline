from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

# Import security modules
from app.input_filter import detect_prompt_injection
from app.output_filter import detect_data_leakage
from app.logger import log_security_event

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "Secure AI Pipeline running"}


@app.post("/chat")
def chat(request: PromptRequest):

    user_prompt = request.prompt

    # Prompt Injection Protection
    if detect_prompt_injection(user_prompt):
        log_security_event(f"Prompt injection attempt: {user_prompt}")
        return {"error": "Prompt blocked due to security policy"}

    # Simulated AI response
    response = f"AI Response: {user_prompt}"

    # Data Leakage Protection
    if detect_data_leakage(response):
        log_security_event(f"Sensitive data request: {user_prompt}")
        return {"error": "Sensitive information blocked"}

    return {"response": response}


# -------- Security Dashboard Endpoint --------
@app.get("/security-events")
def security_events():

    log_file = Path("security.log")

    if not log_file.exists():
        return {"events": []}

    with open(log_file, "r") as f:
        lines = f.readlines()

    events = [line.strip() for line in lines]

    return {"events": events}
