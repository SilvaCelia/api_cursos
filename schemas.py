from pydantic import BaseModel

class CursoBase(BaseModel):
    titulo: str
    descricao: str
    carga_horaria: int
    instituicao: str

class CursoRequest(CursoBase):
    ...

class CursoResponse(CursoBase):
    id: int

    class Config:
        orm_mode = True
