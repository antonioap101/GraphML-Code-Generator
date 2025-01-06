from fastapi import APIRouter

from api.crud.src.generator.CRUDCodeGenerator import CRUDCodeGenerator
from api.crud.src.parsing.CRUDCodeGeneratorInput import CRUDCodeGeneratorInput

router = APIRouter(prefix="/crud", tags=["CRUD"])


@router.get("/")
async def home():
    return {"message": "¡Bienvenido al Generador de código CRUD!"}


@router.post("/")
async def generate_crud(input_data: CRUDCodeGeneratorInput):
    code = CRUDCodeGenerator.generate_code(input_data)
    print("Generated code:")
    print(code)

    # Return the same input data parsed as json
    # return input_data.dict()
    return {"code": code}
