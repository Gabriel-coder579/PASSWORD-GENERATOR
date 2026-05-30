# Password Generator

Hey there! This is my little password generator project. I built this web app to help people create strong, secure passwords easily. It's simple to use and runs right in your browser.

## What it does

This app generates random passwords based on your preferences. You can choose:
- How long you want the password to be
- Whether to include uppercase letters, lowercase letters, numbers, and special characters
- It excludes confusing characters like 'l' and '1' or 'O' and '0' to make it easier to read

The frontend is a clean HTML page with some JavaScript to handle the user input and display the generated password. The backend is a Python Flask app that does the actual password generation logic.

## How to run it

1. Make sure you have Python installed on your machine.
2. Clone or download this project to your computer.
3. Open a terminal and navigate to the project folder.
4. Install the required dependencies (if any) - I used Flask, so run `pip install flask`.
5. Run the app with `python app.py`.
6. Open your browser and go to `http://localhost:5000` (or whatever port it's set to).

That's it! The app should be up and running.

## Technologies I used

- **Python** with Flask for the backend
- **HTML/CSS** for the frontend structure and styling
- **JavaScript** for handling user interactions and API calls

I kept it lightweight and didn't use any fancy frameworks - just vanilla stuff to keep things simple.

## Why I made this

I wanted to practice building a full-stack web app with Python. Password generators are useful, and it's a good way to learn about random string generation and web development basics.

If you find any bugs or have suggestions, feel free to let me know. Enjoy generating secure passwords!