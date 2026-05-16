# URL Safety Checker

## Overview

The URL Safety Checker is a simple web application developed using Python and Flask that helps users identify whether a URL appears safe, suspicious, or invalid. The project was created as a beginner-friendly cybersecurity application focusing on basic URL validation and phishing awareness.

## Features

- Checks whether a URL is properly formatted
- Detects suspicious keywords commonly used in phishing links
- Displays results using color indicators
- Simple and easy-to-use interface
- Helps users identify potentially unsafe links

## Technologies Used

- Python
- Flask
- HTML
- CSS

## How the Application Works

The user enters a URL into the web application. The system then:

1. Validates whether the entered text is a proper URL
2. Searches for suspicious keywords such as:
   - login
   - verify
   - secure
   - free
   - prize
3. Displays one of the following results:
   - Safe URL
   - Unsafe URL Detected
   - Invalid or Unsafe URL

## Example Inputs

### Safe URL
```text
https://google.com
```

### Suspicious URL
```text
https://free-login-prize.xyz
```

### Invalid Input
```text
google
```

## Project Structure

```text
project-folder/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

## Installation

Install Flask using:

```bash
pip install flask
```

## Running the Application

Run the following command:

```bash
python app.py
```

Then open the browser and visit:

```text
http://127.0.0.1:5000
```

## Future Improvements

- API integration for real-time URL reputation checking
- Improved phishing detection techniques
- Database support for blacklisted URLs
- Enhanced user interface

## Author

Fathima Abdul Jabbar
