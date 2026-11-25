import csv, os, datetime

CSV = "applications.csv"

def log_application(company, title, score, reason, status):
    new = not os.path.exists(CSV)
    with open(CSV, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["date", "company", "title", "score", "status", "reason"])
        w.writerow([datetime.datetime.now().isoformat(timespec="minutes"),
                    company, title, score, status, reason])