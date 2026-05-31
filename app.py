import os
import random
import string
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) so your HTML frontend can safely call this API
CORS(app)

def generate_password(length=12):
    """
    Generates a secure, random password of a given length
    using letters, digits, and punctuation.
    """
    # Use letters, digits, and punctuation for strong passwords
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_password_strength(password):
    """
    Checks if a password meets the basic strength guidelines:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return has_upper and has_lower and has_digit and has_special

def get_suggestions(password):
    """
    Analyzes the password and returns up to 2 suggestions to make it stronger.
    """
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
    # Returning only up to 2 suggestions to keep UI clean
    return suggestions[:2]


# --- HOME ROUTE (FIXES THE "NOT FOUND" ERROR) ---

@app.route('/')
def home():
    """
    GET Endpoint: Serves your index.html webpage.
    This dynamically checks both the 'templates' folder and the root directory
    to ensure your interface loads successfully!
    """
    # Check if index.html is inside a templates directory
    if os.path.exists(os.path.join('templates', 'index.html')):
        return send_from_directory('templates', 'index.html')
    
    # Check if index.html is directly in the root directory
    elif os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    
    # Elegant fallback message if the front-end file is missing
    else:
        return """
        <div style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h1 style="color: #4f46e5;">VaultGuard API is Live! 🚀</h1>
            <p style="color: #64748b;">The backend server is up and running successfully.</p>
            <p style="color: #ef4444; font-weight: bold;">Notice: Please make sure your 'index.html' file is uploaded to GitHub inside either your main root directory or a folder named 'templates'.</p>
        </div>
        """, 200


# --- API ENDPOINTS ---

@app.route('/generate', methods=['POST'])
def api_generate():
    """
    POST Endpoint: Generates a random password based on requested length.
    Input JSON: { "length": 12 }
    """
    data = request.get_json() or {}
    try:
        # Get length from payload, defaulting to 12 if invalid or missing
        length = int(data.get('length', 12))
        if length < 4 or length > 64:
            length = 12
    except (ValueError, TypeError):
        length = 12

    password = generate_password(length)
    return jsonify({"password": password})

@app.route('/check', methods=['POST'])
def api_check():
    """
    POST Endpoint: Checks strength of incoming password and suggests 
    strong alternatives if it fails security criteria.
    Input JSON: { "password": "user_input" }
    """
    data = request.get_json() or {}
    password = data.get('password', '')

    is_strong = check_password_strength(password)
    suggestions = get_suggestions(password)
    
    # Generate 2 highly secure alternative passwords if the user's password is weak
    generated_alternatives = []
    if not is_strong:
        for _ in range(2):
            alt_pass = generate_password(12)
            # Ensure generated alternative is actually strong before recommending it
            while not check_password_strength(alt_pass):
                alt_pass = generate_password(12)
            generated_alternatives.append(alt_pass)

    return jsonify({
        "is_strong": is_strong,
        "suggestions": suggestions,
        "generated": generated_alternatives
    })

if __name__ == "__main__":
    # Runs local server on port 5000 for development testing
    app.run(debug=True, port=5000)