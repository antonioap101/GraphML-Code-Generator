from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.graphml.src.GraphMLGenerator import GraphMLGenerator

router = APIRouter(prefix="/graphml", tags=["GraphML"])


class XMLInput(BaseModel):
    xml_content: str


@router.get("/")
async def home():
    return {"message": "¡Bienvenido al Convertidor XML a GraphML!"}


@router.post("/")
async def convert_to_graphml(input_data: XMLInput):
    """
    Convierte contenido XML en GraphML.
    """
    try:
        graphml = GraphMLGenerator.from_string(input_data.xml_content, "xml")
        graphml_content = GraphMLGenerator.to_string(graphml)
        return {"graphml": graphml_content}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
