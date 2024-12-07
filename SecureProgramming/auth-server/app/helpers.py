import random
import string
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def validate_password(password):
    if len(password) < 12:
        return False, "Password must be at least 12 characters long."
    if not any(char.islower() for char in password):
        return False, "Password must include at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return False, "Password must include at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return False, "Password must include at least one digit."
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in password):
        return False, "Password must include at least one special character."
    return True, "Password is strong."


def hash_password(password: str) -> str:
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    return hashed_password


def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.check_password_hash(hashed_password.encode('utf-8'), password)


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
