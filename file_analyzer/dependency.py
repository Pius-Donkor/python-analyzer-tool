from pathlib import Path
from fastapi import HTTPException
from datetime import datetime


def validate_folder(folder: Path) -> Path:
    if not folder.exists() or not folder.is_dir():
        raise HTTPException(status_code=400, detail="Invalid folder path")
    return folder


def validate_top(top: int) -> int:
    if top < 1:
        raise HTTPException(status_code=400, detail="top must be greater than 0")
    return top


def get_request_time():
    return {"timestamp": datetime.now().isoformat()}
