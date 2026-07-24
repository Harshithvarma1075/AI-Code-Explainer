from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check():
    return {
        "status": "success",
        "message": "Backend is running successfully"
    }