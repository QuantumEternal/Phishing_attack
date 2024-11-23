from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Define the path to the 'users.txt' file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = os.path.join(BASE_DIR, "database")
USERS_FILE = os.path.join(DATABASE_DIR, "users.txt")

# Ensure the database folder exists
os.makedirs(DATABASE_DIR, exist_ok=True)

# Initialize the file with a table header if it doesn't exist
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as file:
        file.write(f"{'Email':<30} | {'Password':<20}\n")
        file.write("-" * 50 + "\n")

@app.route("/")
def index():
    return render_template("index.html")  # Ensure your index.html is in a 'templates/' folder

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email")
    password = request.form.get("password")

    if email and password:
        # Save the email and password in table format
        with open(USERS_FILE, "a") as file:
            file.write(f"{email:<30} | {password:<20}\n")

    return "User data saved successfully!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
