# helper_title_case.py
# Author: areeshausmani93@gmail.com
# A small helper to clean and format blog titles before adding them to Google Sheets

def title_case(text: str) -> str:
    """
    Converts a topic string into clean title case.
    Example: "how to learn make.com workflows" -> "How to Learn Make.com Workflows"
    """
    return text.title()

if __name__ == "__main__":
    sample_topics = [
        "ai blogging tools",
        "how to automate content creation",
        "beginners guide to make.com"
    ]
    for topic in sample_topics:
        print(f"Original: {topic}")
        print(f"Formatted: {title_case(topic)}\n")
