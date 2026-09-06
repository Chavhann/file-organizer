from pathlib import Path

from src.classifier import get_category


def test_pdf_is_document():
    assert get_category(Path("report.pdf")) == "Documents"


def test_jpg_is_image():
    assert get_category(Path("photo.jpg")) == "Images"


def test_mp4_is_video():
    assert get_category(Path("movie.mp4")) == "Videos"


def test_mp3_is_audio():
    assert get_category(Path("song.mp3")) == "Audio"


def test_zip_is_archive():
    assert get_category(Path("backup.zip")) == "Archives"


def test_exe_is_program():
    assert get_category(Path("program.exe")) == "Programs"


def test_csv_is_spreadsheet():
    assert get_category(Path("data.csv")) == "Spreadsheets"


def test_pptx_is_presentation():
    assert get_category(Path("slides.pptx")) == "Presentations"


def test_unknown_extension_is_others():
    assert get_category(Path("file.xyz")) == "Others"


def test_extension_is_case_insensitive():
    assert get_category(Path("PHOTO.JPG")) == "Images"