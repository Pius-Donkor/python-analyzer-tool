from pathlib import Path


def analyze(folder: Path, suffix: str, min_lines: None | int, top: int | None):

    files = []
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
                    line_count = sum(1 for _ in f)
                if min_lines is not None and line_count < min_lines:
                    continue
                total_lines += line_count
            except Exception as e:
                print(e)
                continue
            file_count += 1
            file_size = item.stat().st_size
            files.append({"name": str(item), "size": file_size, "lines": line_count})
            if file_size > largest_file_size:
                largest_file_size = file_size
                largest_file_name = item.name

    if top is not None:
        files = sorted(files, key=lambda file: file["size"], reverse=True)[:top]
    return {
        "file_count": file_count,
        "total_lines": total_lines,
        "largest_file": {"name": largest_file_name, "size": largest_file_size},
        "top_files": files if top is not None else [],
    }
