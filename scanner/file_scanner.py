import hashlib
import os

def scan_file(filepath):

    score = 0
    reasons = []

    size = os.path.getsize(filepath)

    if size > 100 * 1024 * 1024:
        score += 15
        reasons.append("Large file size")

    sha256 = hashlib.sha256()

    with open(filepath,"rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)

    file_hash = sha256.hexdigest()

    reasons.append(f"SHA256: {file_hash[:16]}...")

    malware_hashes = [
        "44d88612fea8a8f36de82e1278abb02f"
    ]

    if file_hash in malware_hashes:
        score += 80
        reasons.append("Known malware hash")

    ext = filepath.split(".")[-1].lower()

    suspicious = ["exe","bat","scr","js"]

    if ext in suspicious:
        score += 20
        reasons.append("Executable file")

    if score >= 70:
        status = "DANGER"
    elif score >= 40:
        status = "SUSPICIOUS"
    else:
        status = "SAFE"

    return status, score, reasons
