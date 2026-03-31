from pathlib import Path
import argparse


def analyze(folder: Path, suffix: str):
    file_count = 0
    total_lines = 0

    largest_file_size = 0
    largest_file_name = ""

    # for item in folder.iterdir(): # .iterdir() only lets you get a surface level of the director not the subfolders
    for item in folder.rglob(
        f"*{suffix}"
    ):  # you use .rglob If you want to find every .py file in a project, including all subfolders (like a recursive find),
        if item.is_file():
            try:
                with item.open(mode="r", encoding="utf-8") as f:
                    lines = f.readlines()
                    total_lines += len(lines)
            except Exception:
                continue
            file_count += 1
            file_size = item.stat().st_size
            if file_size > largest_file_size:
                largest_file_size = file_size
                largest_file_name = item.name

    print(f"Total files found: {file_count}")
    print(f"Total lines across files: {total_lines} ")
    print(f"largest file: {largest_file_name} ({largest_file_size} bytes)")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze files in a folder by extension"
    )

    parser.add_argument("folder", type=str, help="Path to folder")
    parser.add_argument("extension", type=str, help="File Extension (eg: .js .py .txt)")

    args = parser.parse_args()

    folder_path = Path(args.folder)
    suffix = args.extension

    if not folder_path.exists() or not folder_path.is_dir():
        print("Error: provided folder path invalid")
        return
    analyze(folder_path, suffix)


if __name__ == "__main__":
    main()
