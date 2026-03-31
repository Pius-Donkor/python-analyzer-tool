from pathlib import Path
import sys

# print(sys.argv)

if len(sys.argv) != 3:
    print("USAGE: uv run main.py <folder_path> <extension>")
    sys.exit(1)

folder = Path(sys.argv[1])
target_suffix = sys.argv[2]

file_count = 0
total_lines = 0

largest_file_size = 0
largest_file_name = ""


# for item in folder.iterdir(): # .iterdir() only lets you get a surface level of the director not the subfolders
for item in folder.rglob(
    f"{target_suffix}"
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
