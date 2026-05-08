from fastapi import APIRouter, HTTPException, Depends
from httpx import AsyncClient
from pathlib import Path

# from pathlib import Path
from file_analyzer.core import analyze
from file_analyzer.schemas import AnalyzeResponse, AnalyzeRequest
from file_analyzer.dependency import validate_folder, validate_top, get_request_time

router = APIRouter()


@router.get("/")
def root():
    return {"message": "File Analyzer API is running"}


@router.get("/github")
async def get_github_user():
    async with AsyncClient() as client:
        response = await client.get("https://api.github.com/users/octocat")

    return response.json()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_files(
    request: AnalyzeRequest,
    request_info: dict = Depends(get_request_time),
):

    print(request_info)
    # if not request.folder.exists() or not request.folder.is_dir():
    #     raise HTTPException(status_code=400, detail="Invalid folder path")
    results = analyze(request.folder, request.extension, request.min_lines, request.top)
    return results


# @app.get("/analyze", response_model=AnalyzeResponse)
# def analyze_files(
#     folder: Path, extension: str, min_lines: int | None = None, top: int | None = None
# ):

#     if not folder.exists() or not folder.is_dir():
#         raise HTTPException(status_code=400, detail="Invalid folder path")
#     results = analyze(folder, extension, min_lines, top)
#     return results


# if __name__ == "__main__":

#     main()
