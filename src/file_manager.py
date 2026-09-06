from pathlib import Path
import shutil
import json

LOG_FILE_NAME = "organization_log.json"


def scan_files(target_folder):
    """
    Return files directly inside the target folder.
    Subfolders are not scanned.
    """

    return [
        file
        for file in target_folder.iterdir()
        if file.is_file() and file.name != LOG_FILE_NAME
    ]


def organize_files(files, target_folder, get_category):
    """
    Move files into their appropriate category folders.

    Returns:
        moved_files, skipped
    """

    moved_files = []
    skipped = 0

    log_file = target_folder / LOG_FILE_NAME

    print("\nOrganizing files...\n")

    for file in files:
        category = get_category(file)

        destination_folder = target_folder / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file.name

        if destination.exists():
            print(f"SKIPPED: {file.name}")
            skipped += 1
            continue

        try:
            shutil.move(str(file), str(destination))

            moved_files.append({
                "original": str(file),
                "destination": str(destination)
            })

            print(f"MOVED: {file.name} -> {category}")

        except Exception as error:
            print(f"ERROR: {file.name} -> {error}")

    if moved_files:
        with open(log_file, "w", encoding="utf-8") as log:
            json.dump(moved_files, log, indent=4)

    print("\n========== RESULT ==========")
    print(f"Files moved: {len(moved_files)}")
    print(f"Files skipped: {skipped}")
    print("============================")

    return moved_files, skipped


def undo_last_organization(target_folder):
    """
    Restore the files from the most recent organization.
    """

    log_file = target_folder / LOG_FILE_NAME

    if not log_file.exists():
        print("\nNo organization history found for this folder.")
        return

    with open(log_file, "r", encoding="utf-8") as log:
        moved_files = json.load(log)

    if not moved_files:
        print("\nNothing to undo.")
        return

    print("\nUndoing last organization...\n")

    restored = 0
    skipped = 0

    for item in reversed(moved_files):
        original = Path(item["original"])
        destination = Path(item["destination"])

        if not destination.exists():
            print(f"SKIPPED: {destination.name} not found")
            skipped += 1
            continue

        if original.exists():
            print(f"SKIPPED: {original.name} already exists")
            skipped += 1
            continue

        try:
            shutil.move(str(destination), str(original))

            print(f"RESTORED: {destination.name}")
            restored += 1

        except Exception as error:
            print(f"ERROR: {destination.name} -> {error}")

    if restored > 0 and skipped == 0:
        log_file.unlink()

    print("\n========== UNDO RESULT ==========")
    print(f"Files restored: {restored}")
    print(f"Files skipped: {skipped}")
    print("=================================")

    return restored, skipped