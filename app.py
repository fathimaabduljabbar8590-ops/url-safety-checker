from flask import Flask, render_template, request
from urllib.parse import urlparse

app = Flask(__name__)

# Function to check valid URL
def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

# Function to check suspicious keywords
def check_url(url):
    suspicious_keywords = ["login", "verify", "bank", "secure", "free", "prize"]

    # Check if URL is valid
    if not is_valid_url(url):
        return "Invalid or Unsafe URL", "red"

    # Check suspicious words
    for word in suspicious_keywords:
        if word in url.lower():
            return "Unsafe URL Detected!", "red"

    return "Safe URL", "green"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    color = ""

    if request.method == "POST":
        url = request.form["url"]
        result, color = check_url(url)

    return render_template("index.html", result=result, color=color)

if __name__ == "__main__":
    app.run(debug=True)
