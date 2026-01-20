from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "testdb")
}

@app.route("/")
def home():
    return "Docker Mini Project (Python + Flask) Running"

@app.route("/db")
def db_check():
    try:
        conn = mysql.connector.connect(**db_config)
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
@app.route("/health")
def health_check():
    return "OK",200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
