import requests
import socket
from urllib.parse import urlparse

def scan_url(url):

    score = 0
    reasons = []

    try:

        parsed = urlparse(url)
        domain = parsed.netloc

        socket.gethostbyname(domain)

        if parsed.scheme != "https":
            score += 25
            reasons.append("Website not using HTTPS")

        if "@" in url:
            score += 20
            reasons.append("Suspicious '@' symbol")

        if "-" in domain:
            score += 10
            reasons.append("Hyphen in domain")

        if len(url) > 80:
            score += 10
            reasons.append("Long URL")

        keywords = [
            "login","secure","verify",
            "bank","account","update","free"
        ]

        for k in keywords:
            if k in url.lower():
                score += 8
                reasons.append(f"Keyword detected: {k}")

        r = requests.get(url, timeout=5)

        if r.status_code >= 400:
            score += 15
            reasons.append("Website response abnormal")

    except:
        score = 90
        reasons.append("Domain unreachable")

    if score >= 70:
        status = "DANGER"
    elif score >= 40:
        status = "SUSPICIOUS"
    else:
        status = "SAFE"

    return status, score, reasons
