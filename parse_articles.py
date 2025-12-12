# parse_articles.py

def parse_article(raw_text: str) -> dict:
    """
    Very simple article parser:
    - First non-empty line is the title.
    - Everything after a blank line is the body.
    """
    parts = raw_text.split("\n\n", 1)
    title = parts[0].strip()
    body = parts[1].strip() if len(parts) > 1 else ""
    return {"title": title, "body": body}


if __name__ == "__main__":
    sample = "Breaking News\n\nThis is the article body."
    parsed = parse_article(sample)
    print(parsed)
