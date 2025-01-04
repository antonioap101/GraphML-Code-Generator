from fastapi import APIRouter

from api.crud.src.parsing.CRUDGeneratorInput import CRUDGeneratorInput

router = APIRouter(prefix="/crud", tags=["CRUD"])


@router.get("/")
async def home():
    return {"message": "¡Bienvenido al Generador de código CRUD!"}


@router.post("/")
async def generate_crud(input_data: CRUDGeneratorInput):
    # Return the same input data parsed as json
    return input_data.dict()

