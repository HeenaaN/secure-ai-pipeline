blocked_patterns = [
    "ignore previous instructions",
    "reveal system prompt",
    "show api key",
    "display confidential data",
    "bypass security",
    "api key",
    "system prompt",
    "secret key",
    "internal prompt"
]

def detect_prompt_injection(prompt: str):
    prompt_lower = prompt.lower()

    for pattern in blocked_patterns:
        if pattern in prompt_lower:
            return True

    return False
