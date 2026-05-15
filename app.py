from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "AIzaSyC97PdfVPtT6t1h5y4NkZ_yPfVLl3WezPI"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""

    if request.method == 'POST':
        url = request.form['url']

        api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

        payload = {
            "client": {
                "clientId": "url-safety-checker",
                "clientVersion": "1.0"
            },
            "threatInfo": {
                "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
                "platformTypes": ["ANY_PLATFORM"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [
                    {"url": url}
                ]
            }
        }

        response = requests.post(api_url, json=payload)

        data = response.json()

         if "matches" in data or "unsafe" in url or "phishing" in url:
            result = "⚠️ Unsafe Website Detected!"
        else:
            result = "✅ This URL Looks Safe"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
