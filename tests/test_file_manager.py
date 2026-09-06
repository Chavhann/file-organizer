from pathlib import Path

from src.classifier import get_category
from src.file_manager import scan_files, organize_files, undo_last_organization


def test_scan_files(tmp_path):
    (tmp_path / "document.pdf").touch()
    (tmp_path / "photo.jpg").touch()

    (tmp_path / "MyProject").mkdir()
    (tmp_path / "MyProject" / "main.py").touch()

    files = scan_files(tmp_path)

    file_names = {file.name for file in files}

    assert file_names == {
        "document.pdf",
        "photo.jpg",
    }


def test_organize_files(tmp_path):
    pdf = tmp_path / "document.pdf"
    jpg = tmp_path / "photo.jpg"

    pdf.touch()
    jpg.touch()

    files = scan_files(tmp_path)

    moved_files, skipped = organize_files(
        files,
        tmp_path,
        get_category
    )

    assert len(moved_files) == 2
    assert skipped == 0

    assert (tmp_path / "Documents" / "document.pdf").exists()
    assert (tmp_path / "Images" / "photo.jpg").exists()

    assert not pdf.exists()
    assert not jpg.exists()


def test_undo_last_organization(tmp_path):
    pdf = tmp_path / "document.pdf"
    jpg = tmp_path / "photo.jpg"

    pdf.touch()
    jpg.touch()

    files = scan_files(tmp_path)

    organize_files(
        files,
        tmp_path,
        get_category
    )

    restored, skipped = undo_last_organization(tmp_path)

    assert restored == 2
    assert skipped == 0

    assert pdf.exists()
    assert jpg.exists()

    assert not (tmp_path / "Documents" / "document.pdf").exists()
    assert not (tmp_path / "Images" / "photo.jpg").exists()


def test_existing_destination_is_skipped(tmp_path):
    pdf = tmp_path / "document.pdf"
    pdf.touch()

    documents = tmp_path / "Documents"
    documents.mkdir()

    existing_pdf = documents / "document.pdf"
    existing_pdf.touch()

    files = scan_files(tmp_path)

    moved_files, skipped = organize_files(
        files,
        tmp_path,
        get_category
    )

    assert len(moved_files) == 0
    assert skipped == 1

    assert pdf.exists()
    assert existing_pdf.exists()