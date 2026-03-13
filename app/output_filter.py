# Output security filter for data leakage

sensitive_patterns = [
    "api key",
    "password",
    "secret",
    "confidential",
    "system prompt"
]

def detect_data_leakage(response: str):
    response_lower = response.lower()

    for pattern in sensitive_patterns:
        if pattern in response_lower:
            return True

    return False
