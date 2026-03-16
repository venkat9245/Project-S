# scanner/apk_scanner.py

import subprocess

def scan_apk(apk_file):
    result = subprocess.run(
        ["apktool","d",apk_file,"-o","apk_output"],
        capture_output=True
    )

    if result.returncode == 0:
        return "APK ANALYZED"
    return "ERROR ANALYZING APK"
