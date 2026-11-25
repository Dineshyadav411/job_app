# AI Job-Application Agent

A Python agent that matches job descriptions against a candidate profile using the Claude API, drafts tailored cover letters, and logs applications to CSV.

## Stack
Python, Claude API, Playwright, Google Sheets API

## Setup
```bash
pip install -r requirements.txt
Create .env:

text
ANTHROPIC_API_KEY=your_key
Usage
bash
python agent.py
Features
JD matching with Claude (0–100 fit score)

Tailored cover letter per job

CSV application log

Playwright browser automation (optional)

Note
Personal use only. Check job board terms before automating.