import logging

logging.basicConfig(
    filename="security.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_security_event(message: str):
    logging.warning(message)
