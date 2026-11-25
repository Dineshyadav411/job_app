def match_jd(client, profile: str, jd: str):
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        messages=[{"role": "user", "content":
            f"Candidate:\n{profile}\n\nJob:\n{jd}\n\n"
            "Return two lines: first a score 0-100, second a one-line reason."}]
    )
    text = msg.content[0].text.strip().split("\n")
    score = int("".join(c for c in text[0] if c.isdigit()) or 0)
    reason = text[1] if len(text) > 1 else ""
    return score, reason