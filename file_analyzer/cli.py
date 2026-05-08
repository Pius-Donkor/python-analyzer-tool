from pathlib import Path
import argparse
import json
from file_analyzer.core import analyze


def main():
    parser = argparse.ArgumentParser(
        description="Analyze files in a folder by extension"
    )

    parser.add_argument("folder", type=str, help="Path to folder")
    parser.add_argument("extension", type=str, help="File Extension (eg: .js .py .txt)")
    parser.add_argument(
        "--json", action="store_true", help="Output results in JSON format"
    )
    parser.add_argument(
        "--min-lines",
        type=int,
        help="Minimum number of lines a file must have to be included",
    )
    parser.add_argument(
        "--top",
        type=int,
        help="Show N largest files",
    )
    args = parser.parse_args()

    folder_path = Path(args.folder)
    suffix = args.extension

    if not folder_path.exists() or not folder_path.is_dir():
        print("Error: provided folder path invalid")
        return
    results = analyze(folder_path, suffix, args.min_lines, args.top)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"Total files found: {results['file_count']}")
        print(f"Total lines across files found: {results['total_lines']}")
        print(
            f"Largest file: {results['largest_file']['name']} "
            f"({results['largest_file']['size']} bytes)"
        )
        if args.top:
            print("\nTop files:")
            for f in results["top_files"]:
                print(f"{f['name']} - {f['size']} bytes ({f['lines']} lines)")
