CATEGORIES = {
    "Documents": {".pdf", ".doc", ".docx", ".txt"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Audio": {".mp3", ".wav", ".aac", ".flac"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Programs": {".exe", ".msi"},
    "Spreadsheets": {".xls", ".xlsx", ".csv"},
    "Presentations": {".ppt", ".pptx"},
}

PROTECTED_FOLDERS = set(CATEGORIES.keys()) | {"Others"}


def get_category(file):
    """
    Return the category for a file based on its extension.
    """

    extension = file.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"