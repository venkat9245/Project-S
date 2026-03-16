# ai/phishing_detector.py

def detect_phishing(url):
    phishing_patterns = [
        "secure-login",
        "verify-account",
        "bank-update"
    ]
    for p in phishing_patterns:
        if p in url.lower():
            return True
    return False
