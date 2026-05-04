import random
import string


def generate_strong_password(length: int = 12) -> str:
    """Generate a strong password with uppercase, lowercase, digits, and special characters."""
    if length < 4:
        raise ValueError("Password length must be at least 4")

    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?")

    remaining = "".join(
        random.choices(
            string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?",
            k=length - 4,
        )
    )

    password = list(uppercase + lowercase + digit + special + remaining)
    random.shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    for length in [8, 12, 16]:
        print(f"Password (length={length}): {generate_strong_password(length)}")
