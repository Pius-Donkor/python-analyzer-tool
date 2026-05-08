from pydantic import BaseModel
from pathlib import Path


class FileInfo(BaseModel):
    name: str
    size: int
    lines: int


class LargestFile(BaseModel):
    name: str
    size: int


class AnalyzeResponse(BaseModel):
    file_count: int
    total_lines: int
    largest_file: LargestFile
    top_files: list[FileInfo]


class AnalyzeRequest(BaseModel):
    folder: Path
    extension: str
    min_lines: int | None = None
    top: int | None = None
