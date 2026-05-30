import random
import string

def generate_password(length=12):
    # Use letters, digits, and punctuation for strong passwords
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_password_strength(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return has_upper and has_lower and has_digit and has_special

def get_suggestions(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Make your password at least 8 characters long.")
    if not any(c.isupper() for c in password):
        suggestions.append("Include at least one uppercase letter.")
    if not any(c.islower() for c in password):
        suggestions.append("Include at least one lowercase letter.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Include at least one number.")
    if not any(c in string.punctuation for c in password):
        suggestions.append("Include at least one special character.")
    # Returning only up to 2 suggestions
    return suggestions[:2]

if __name__ == "__main__":
    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12
    password = generate_password(length)
    print(f"Generated password: {password}")