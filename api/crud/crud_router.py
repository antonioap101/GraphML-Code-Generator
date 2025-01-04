from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/crud", tags=["CRUD"])


class XMLInput(BaseModel):
    xml_content: str


@router.get("/")
async def home():
    return {"message": "¡Bienvenido al Generador de código CRUD!"}
