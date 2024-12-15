from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from api.src.GraphMLGenerator.GraphMLGenerator import GraphMLGenerator

app = FastAPI()


class XMLInput(BaseModel):
    xml_content: str


@app.get("/convert/")
async def home():
    return {"message": "¡Bienvenido al Convertidor XML a GraphML!"}


@app.post("/convert/")
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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
