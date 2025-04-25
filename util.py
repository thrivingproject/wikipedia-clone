import os
import re

base_path = os.path.join(os.path.dirname(__file__), "entries")


def save_article(filename: str, content):
    """
    Save content to a markdown file.
    """
    if not filename.endswith(".md"):
        filename += ".md"
    file_path = os.path.join(base_path, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def get_article(filename: str):
    """
    Read content from a markdown file.
    """
    try:
        if not filename.endswith(".md"):
            filename += ".md"
        file_path = os.path.join(base_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


def list_entries():
    """
    List all markdown files in the directory.
    """
    return sorted(
        [
            re.sub(r"\.md$", "", f)
            for f in os.listdir(base_path)
            if f.endswith(".md")
        ]
    )
