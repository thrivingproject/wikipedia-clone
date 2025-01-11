import os

base_path = os.path.join(os.path.dirname(__file__), "entries")


def save_entry(filename, content):
    """
    Save content to a markdown file.
    """
    filename += ".md"
    file_path = os.path.join(base_path, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def get_entry(filename):
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
    return [f for f in os.listdir(base_path) if f.endswith(".md")]
