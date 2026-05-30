
from flask import Flask, request, jsonify, render_template
import random
import string
from password import generate_password, check_password_strength, get_suggestions

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    length = data.get('length', 12)
    try:
        length = int(length)
    except (ValueError, TypeError):
        length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return jsonify({'password': password})

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    password = data.get('password', '')
    is_strong = check_password_strength(password)
    suggestions = get_suggestions(password) if not is_strong else []
    generated = [generate_password() for _ in range(2)]
    return jsonify({
        'is_strong': is_strong,
        'suggestions': suggestions,
        'generated': generated
    })

if __name__ == '__main__':
    app.run(debug=True)
