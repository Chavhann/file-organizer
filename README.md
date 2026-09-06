# Python File Organizer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-14%20passed-brightgreen)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A safe and modular Python CLI tool that automatically organizes files into categorized folders based on their file extensions.

The tool is designed with safety in mind and includes **Dry Run**, **collision protection**, **organization history**, and **Undo** support.

## Features

* Automatically organizes files by extension
* Supports multiple file categories
* Preview file movements before making changes
* Dry Run mode with no file modifications
* Prevents overwriting existing files
* Records successful file movements
* Undo the most recent organization
* Safely handles duplicate filenames
* Supports unknown file extensions through `Others`
* Does not recursively modify files inside subfolders
* Includes automated tests using `pytest`
* Simple interactive command-line interface

## Supported Categories

| Category      | Extensions                                        |
| ------------- | ------------------------------------------------- |
| Documents     | `.pdf`, `.doc`, `.docx`, `.txt`                   |
| Images        | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.tiff` |
| Videos        | `.mp4`, `.mkv`, `.avi`, `.mov`                    |
| Audio         | `.mp3`, `.wav`, `.aac`, `.flac`                   |
| Archives      | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`              |
| Programs      | `.exe`, `.msi`                                    |
| Spreadsheets  | `.xls`, `.xlsx`, `.csv`                           |
| Presentations | `.ppt`, `.pptx`                                   |
| Others        | Unknown or unsupported extensions                 |

## How It Works

The application follows a simple workflow:

1. Select a folder.
2. Scan files directly inside the selected folder.
3. Preview how files will be categorized.
4. Organize files into category folders.
5. Record successful file movements in a JSON log.
6. Optionally undo the most recent organization.

Existing files are never overwritten.

## Project Structure

```text
file-organizer/
|-- README.md
|-- LICENSE
|-- .gitignore
|
|-- src/
|   |-- classifier.py
|   |-- file_manager.py
|   `-- organizer.py
|
`-- tests/
    |-- test_classifier.py
    `-- test_file_manager.py
```

## Modules

### `src/classifier.py`

Responsible for:

* File extension classification
* Category definitions
* Protected organizer folders

Main function:

```python
get_category(file)
```

### `src/file_manager.py`

Responsible for:

* Scanning files
* Moving files
* Collision protection
* Organization history
* Undo functionality

Main functions:

```python
scan_files(...)
organize_files(...)
undo_last_organization(...)
```

### `src/organizer.py`

Provides the interactive command-line interface.

Available options:

```text
1. Organize files
2. Undo last organization
3. Dry Run
4. Scan summary
5. Change folder
6. Exit
```

## Safety

The organizer is designed to avoid accidental data loss.

### Dry Run

Dry Run shows what would happen without changing any files.

```text
example.pdf
   -> Documents\example.pdf
```

No files are moved during Dry Run.

### Collision Protection

If a destination file already exists, the application skips the file instead of overwriting it.

```text
SKIPPED: example.pdf
```

### Undo

The application records successful file movements in:

```text
organization_log.json
```

The most recent organization can be reversed using the **Undo last organization** option.

### Subfolder Protection

Only files directly inside the selected folder are processed.

Files inside existing subfolders are not recursively scanned or modified.

## Requirements

* Python 3.10 or newer
* Windows, Linux, or macOS
* `pytest` for running tests

The project was tested on:

```text
Windows
Python 3.13.2
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Chavhann/file-organizer.git
```

Enter the project directory:

```bash
cd file-organizer
```

No external packages are required to run the application.

## Running the Application

From the project root:

### Windows

```powershell
py src\organizer.py
```

### Linux / macOS

```bash
python3 src/organizer.py
```

The application will ask you to enter the folder you want to organize.

Example:

```text
Enter the folder path to organize:
> C:\Users\Ganes\Downloads
```

## Running Tests

Install `pytest` if it is not already installed:

```powershell
py -m pip install pytest
```

Run the complete test suite:

```powershell
py -m pytest -v
```

Current test result:

```text
14 passed
```

## Testing

The project includes automated tests covering:

* File extension classification
* Unknown extensions
* Extensionless files
* Archive classification
* File scanning
* File movement
* Duplicate destination protection
* Undo functionality
* Undo collision protection
* Organization history handling

Manual testing was also performed for:

* Basic organization
* Undo
* Dry Run
* Scan Summary
* Change Folder
* Invalid menu input
* Empty folders
* Invalid folder paths
* File paths supplied instead of folders
* Quoted Windows paths
* Uppercase confirmation input
* Cancelled operations
* Existing destination files
* Unknown file types
* Files with no extension
* Nested subfolder protection

## Example

Before organization:

```text
Downloads/
|-- photo.jpg
|-- report.pdf
|-- song.mp3
|-- video.mp4
`-- archive.zip
```

After organization:

```text
Downloads/
|-- Documents/
|   `-- report.pdf
|
|-- Images/
|   `-- photo.jpg
|
|-- Audio/
|   `-- song.mp3
|
|-- Videos/
|   `-- video.mp4
|
`-- Archives/
    `-- archive.zip
```

## Future Improvements

Possible future enhancements include:

* Recursive folder organization as an optional mode
* Custom category configuration
* File naming conflict resolution
* GUI interface
* Configuration file support
* More detailed logging
* Undo history with multiple organization sessions
* Command-line arguments for automation

## License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

## Author

**Chavhann**

GitHub: https://github.com/Chavhann
