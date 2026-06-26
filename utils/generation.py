import random
import string
from datetime import datetime


def generate_email():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"user_{timestamp}@test.com"


def generate_username():
    random_part = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"user_{random_part}"


def generate_password():
    random_part = ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=12
        )
    )
    return random_part


def generate_note_title():
    random_part = ''.join(random.choices(string.ascii_letters, k=10))
    return f"{random_part}"


def generate_note_content():
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    return f"{random_part}"
