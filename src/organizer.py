from pathlib import Path

from classifier import (
    get_category,
    CATEGORIES,
    PROTECTED_FOLDERS,
)

from file_manager import (
    scan_files,
    organize_files,
    undo_last_organization,
)


def choose_folder():
    while True:
        folder_input = input(
            "\nEnter the folder path to organize:\n> "
        ).strip().strip('"')

        if not folder_input:
            print("Please enter a folder path.")
            continue

        folder = Path(folder_input).expanduser()

        if not folder.exists():
            print("Folder does not exist. Try again.")
            continue

        if not folder.is_dir():
            print("That path is not a folder. Try again.")
            continue

        return folder.resolve()


def show_scan_summary(target_folder, files):
    existing_folders = []
    protected_folders = []

    for item in target_folder.iterdir():
        if item.is_dir():
            if item.name in PROTECTED_FOLDERS:
                protected_folders.append(item.name)
            else:
                existing_folders.append(item.name)

    print("\n========== SCAN RESULT ==========\n")

    print("Folder:")
    print(f"  {target_folder}")

    print(f"\nFiles to organize: {len(files)}")

    if files:
        print("\nFiles:")
        for file in files:
            print(f"  {file.name}")

    print(f"\nExisting folders: {len(existing_folders)}")

    for folder in sorted(existing_folders):
        print(f"  {folder}")

    print(f"\nProtected organizer folders: {len(protected_folders)}")

    for folder in sorted(protected_folders):
        print(f"  {folder}")

    print("\n=================================\n")


def show_preview(files):
    print("\n========== PREVIEW ==========\n")

    for file in files:
        category = get_category(file)
        print(f"{file.name}")
        print(f"   -> {category}")

    print("\n=============================")
    print(f"Total files: {len(files)}")
    print("=============================\n")


def dry_run(files, target_folder):
    print("\n========== DRY RUN ==========\n")

    for file in files:
        category = get_category(file)
        destination = target_folder / category / file.name

        if destination.exists():
            print(f"SKIP: {file.name}")
            print("   Reason: destination already exists")
        else:
            print(f"{file.name}")
            print(f"   -> {category}\\{file.name}")

    print("\n=============================")
    print("DRY RUN COMPLETE")
    print("No files were changed.")
    print("=============================\n")


def main():
    print("\n================================")
    print("       PYTHON FILE ORGANIZER")
    print("================================")

    target_folder = choose_folder()

    print("\nSelected folder:")
    print(target_folder)

    while True:
        print("\n================================")
        print("       PYTHON FILE ORGANIZER")
        print("================================")

        print(f"\nFolder: {target_folder}")

        print("\n1. Organize files")
        print("2. Undo last organization")
        print("3. Dry Run")
        print("4. Scan summary")
        print("5. Change folder")
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            files = scan_files(target_folder)

            if not files:
                print("\nNo loose files found.")
                continue

            show_preview(files)

            confirm = input(
                "Do you want to organize these files? (yes/no): "
            ).strip()

            if confirm.lower() == "yes":
                organize_files(
                    files,
                    target_folder,
                    get_category
                )
            else:
                print("\nOperation cancelled.")

        elif choice == "2":
            undo_last_organization(target_folder)

        elif choice == "3":
            files = scan_files(target_folder)

            if not files:
                print("\nNo loose files found.")
                continue

            dry_run(files, target_folder)

        elif choice == "4":
            files = scan_files(target_folder)
            show_scan_summary(target_folder, files)

        elif choice == "5":
            target_folder = choose_folder()

            print("\nFolder changed to:")
            print(target_folder)

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print(
                "\nInvalid option. "
                "Please choose 1, 2, 3, 4, 5, or 6."
            )


if __name__ == "__main__":
    main()