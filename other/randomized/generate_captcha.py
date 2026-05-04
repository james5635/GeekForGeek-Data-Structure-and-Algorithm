import random
import string


def generate_captcha(length: int = 6) -> str:
    """Generate a random captcha string using alphanumeric characters."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


def verify_captcha(generated: str, user_input: str) -> bool:
    """Verify if user input matches the generated captcha."""
    return generated == user_input


if __name__ == "__main__":
    captcha = generate_captcha(6)
    print(f"Captcha: {captcha}")
    user_input = input("Enter captcha: ")
    if verify_captcha(captcha, user_input):
        print("Verified!")
    else:
        print("Failed!")
