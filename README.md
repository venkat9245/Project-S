# 🛡️ Project-S — Cybersecurity Scanner Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-green)
![Security](https://img.shields.io/badge/Cybersecurity-Scanner-red)

---

## 🔍 Overview

Project-S is a cybersecurity tool that scans URLs and files for malicious content using advanced detection techniques.

---

## ✨ Features

- URL scanning
- File malware scanning
- YARA rule detection
- Logging system
- Web dashboard

---
### 🌐 Live Demo
https://project-s-fisz.onrender.com


## 🖥️ Screenshots

### Dashboard
![Dashboard](/home/strawhat/Project-S/assets/dashboard.png)

### File Scan
![File Scan](/home/strawhat/Project-S/assets/filescan.png)

---
📂 Project Structure
Project-S/
│
├── app.py                  # Main Flask application
├── scanner/               # Scanning modules
│   ├── url_scanner.py
│   ├── file_scanner.py
│   ├── yara_scanner.py
│
├── templates/             # HTML templates
│   └── dashboard.html
│
├── uploads/               # Uploaded files
├── assets/                # Images for README
├── scan_report.log        # Logs
├── requirements.txt
└── README.md

## ⚙️ Installation

```bash
git clone https://github.com/venkat9245/Project-S.git
cd Project-S
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#▶️ Running the Application

🔹 Development Mode
python3 app.py

Open:

http://127.0.0.1:5000

#🚀 Production Mode (Recommended)

Install Gunicorn:

pip install gunicorn

Run:

gunicorn -b 0.0.0.0:5000 app:app

Access:

http://<your-ip>:5000

#🛠️ Technologies Used
Python 🐍
Flask 🌐
YARA 🧬
HTML/CSS 🎨

#👨‍💻 Author

Venkat

GitHub: https://github.com/venkat9245

#📜 License

This project is licensed under the MIT License.
