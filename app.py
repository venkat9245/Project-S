from flask import Flask, render_template, request
from scanner.url_scanner import scan_url
from scanner.file_scanner import scan_file
from scanner.yara_scanner import yara_scan
import os
import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def dashboard():

    result = None

    if request.method == "POST":

        url = request.form.get("url")
        file = request.files.get("file")

        # URL SCAN
        if url:

            status,score,reasons = scan_url(url)

            result = {
                "target": url,
                "status": status,
                "score": score,
                "reasons": reasons
            }

        # FILE SCAN
        elif file and file.filename != "":

            filepath = os.path.join(UPLOAD_FOLDER,file.filename)
            file.save(filepath)

            f_status,f_score,f_reasons = scan_file(filepath)

            yara_status = yara_scan(filepath)

            if yara_status == "DANGER":
                f_status = "DANGER"
                f_score = max(f_score,80)
                f_reasons.append("Malware signature detected (YARA)")

            result = {
                "target": file.filename,
                "status": f_status,
                "score": f_score,
                "reasons": f_reasons
            }

        # SAVE REPORT
        if result:
            with open("scan_report.log","a") as log:
                log.write(f"{datetime.datetime.now()} | {result}\n")

    return render_template("dashboard.html",result=result)

if __name__ == "__main__":
    app.run(debug=True)
