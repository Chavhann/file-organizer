# Python File Organizer

A safe and modular Python utility that automatically organizes loose files into categorized folders based on their file extensions.

The project is designed with safety and reversibility in mind. It provides preview, dry-run, collision protection, organization history, and undo functionality.

## Features

* Organize files by extension
* Preview files before moving them
* Dry Run mode with zero filesystem modifications
* Undo the most recent organization
* Scan only files directly inside the selected folder
* Leave existing subfolders and their contents untouched
* Skip files when a destination with the same name already exists
* Prevent Undo from overwriting an existing original file
* Save successful file movements in JSON history
* Treat unknown and extensionless files as `Others`
* Change the target folder without restarting
* Accept quoted Windows folder paths
* Validate invalid, missing, and non-folder paths
* Modular architecture with automated tests

## Supported Categories

| Category      | File Types                                        |
| ------------- | ------------------------------------------------- |
| Documents     | `.pdf`, `.doc`, `.docx`, `.txt`                   |
| Images        | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.tiff` |
| Videos        | `.mp4`, `.mkv`, `.avi`, `.mov`                    |
| Audio         | `.mp3`, `.wav`, `.aac`, `.flac`                   |
| Archives      | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`              |
| Programs      | `.exe`, `.msi`                                    |
| Spreadsheets  | `.xls`, `.xlsx`, `.csv`                           |
| Presentations | `.ppt`, `.pptx`                                   |
| Others        | Unknown and unsupported extensions                |

## How It Works

```text
Choose Folder
     |
     v
Scan Loose Files
     |
     +----> Scan Summary
     |
     +----> Preview
     |         |
     |         v
     |      Confirm
     |         |
     |         v
     |      Organize
     |         |
     |         v
     |   Save Movement History
     |
     +----> Dry Run
     |         |
     |         v
     |   Preview Without Changes
     |
     +----> Undo Last Organization
```

## Project Structure

```text
file-organizer/
├── README.md
├── src/
│   ├── classifier.py
│   ├── file_manager.py
│   └── organizer.py
└── tests/
    ├── test_classifier.py
    └── test_file_manager.py
```

### Modules

**`classifier.py`**

* Defines supported file categories
* Classifies files by extension
* Handles unknown and extensionless files as `Others`

**`file_manager.py`**

* Scans loose files
* Moves files into category folders
* Handles filename collisions
* Saves organization history
* Restores files during Undo

**`organizer.py`**

* Provides the command-line interface
* Handles folder selection
* Displays previews and scan summaries
* Provides Dry Run, Organize, Undo, and folder-management options

## Safety

The organizer is intentionally conservative:

* It scans only files directly inside the selected folder.
* Files inside existing subfolders are not recursively scanned.
* Existing destination files are never overwritten.
* Dry Run performs no file modifications.
* Organization requires explicit confirmation.
* Undo will not overwrite an existing original file.
* Only successfully moved files are recorded in organization history.

## Requirements

* Python 3.10 or newer
* `pytest` for running automated tests

## Running the Application

From the project directory:

```powershell
py src\organizer.py
```

The program will ask for the folder you want to organize.

## Running Tests

Run the complete automated test suite:

```powershell
py -m pytest -v
```

Current verified result:

```text
14 passed
```

## Testing

The project has been manually and automatically tested for:

* File classification
* All supported categories
* Unknown extensions
* Extensionless files
* Case-insensitive extensions
* Multi-extension files
* Loose-file scanning
* Existing project-folder protection
* File organization
* Filename collision protection
* Undo functionality
* Undo collision protection
* Dry Run behavior
* Organization cancellation
* Empty folders
* Undo with no history
* Reserved organization log handling
* Folder validation
* Quoted Windows paths
* Changing the target folder
* Invalid menu choices
* Uppercase and whitespace-tolerant confirmation input

### Automated Test Result

```text
14 passed
```

## Platform Tested

* Windows
* Python 3.13.2
* pytest 9.1.1

## Future Improvements

Possible future improvements include:

* Recursive organization as an optional mode
* More file-extension categories
* Configurable category rules
* Improved logging and history management
* GUI interface
* Windows executable packaging
* Configuration file support
