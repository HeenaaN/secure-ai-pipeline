# Secure AI Pipeline with Guardrails

A security-focused AI pipeline that protects Large Language Model (LLM) applications from common attacks such as prompt injection and sensitive data leakage.

This project demonstrates how to build **secure AI systems using guardrails and automated security testing**.

---

## Project Overview

Large Language Models (LLMs) are vulnerable to multiple security threats such as:

- Prompt Injection
- Sensitive Information Disclosure
- Model Misuse
- Unauthorized Data Exposure

This project implements a **Secure AI Pipeline** that mitigates these risks using input validation, output filtering, security logging, and automated testing.

---

## Technologies Used

- Python
- FastAPI
- Promptfoo
- Git
- GitHub
- Ubuntu
- VirtualBox

---

## Security Features

### 1. Prompt Injection Protection
Detects and blocks malicious prompts such as:

- "ignore previous instructions"
- "reveal system prompt"
- "show api key"

### 2. Sensitive Data Leakage Protection
Prevents responses containing sensitive information like:

- API keys
- passwords
- system prompts
- confidential data

### 3. Security Logging
All blocked attacks are recorded in a **security log** for monitoring and auditing.

Example log:
WARNING Prompt injection attempt: ignore previous instructions

### 4. Automated AI Security Testing

The system uses **Promptfoo** to automatically test the AI pipeline for vulnerabilities.

Example results:
10 tests passed
83% security coverage

---

## Project Architecture
User Prompt
↓
FastAPI API
↓
Prompt Injection Filter
↓
AI Response Generator
↓
Data Leakage Filter
↓
Security Logger
↓
Security Dashboard
↓
Promptfoo Automated Security Testing

---

## OWASP AI Risks Addressed

This project mitigates several risks from **OWASP Top 10 for LLM Applications**:

| OWASP Risk | Mitigation |
|------------|-----------|
Prompt Injection | Input Filtering |
Sensitive Information Disclosure | Output Filtering |
Model Misuse | Guardrails |
LLM Security Testing | Promptfoo |

---

## How to Run the Project

1. Clone the repository

---

## OWASP AI Risks Addressed

This project mitigates several risks from **OWASP Top 10 for LLM Applications**:

| OWASP Risk | Mitigation |
|------------|-----------|
Prompt Injection | Input Filtering |
Sensitive Information Disclosure | Output Filtering |
Model Misuse | Guardrails |
LLM Security Testing | Promptfoo |

---

## How to Run the Project

1. Clone the repository
git clone https://github.com/HeenaaN/secure-ai-pipeline.git

2. Navigate to the project directory
cd secure-ai-pipeline


3. Install dependencies
pip install -r requirements.txt

4. Start the API server
uvicorn app.main:app --reload

5. Open the API documentation
http://127.00.1:8000/docs


---

## Automated Security Testing

Run Promptfoo tests:
cd promptfoo
promptfoo eval

---

## Future Improvements

- Integration with real LLM APIs (OpenAI, Claude, etc.)
- Advanced prompt injection detection using NLP
- Web-based security monitoring dashboard
- AI attack simulation dataset

---

## Author

Heena

Cybersecurity & AI Security Enthusiast



