import os
from dotenv import load_dotenv
import anthropic
from matcher import match_jd
from tracker import log_application

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

PROFILE = "Name: Karri Dinesh | Skills: Python, FastAPI, RAG, FAISS, Claude API | B.Tech CSE, CGPA 8.52"

def run():
    sample_jd = "Looking for AI Engineer with Python, RAG, LLM experience."
    score, reason = match_jd(client, PROFILE, sample_jd)
    print(f"Score: {score} — {reason}")
    log_application("SampleCo", "AI Engineer", score, reason, "dry_run")

if __name__ == "__main__":
    run()