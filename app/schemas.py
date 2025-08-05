from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from app.models import TipoPergunta


class PerguntaBase(BaseModel):
    titulo: str
    codigo: Optional[str]
    orientacao_resposta: Optional[str]
    ordem: Optional[int]
    obrigatoria: bool = False
    sub_pergunta: bool = False
    tipo_pergunta: TipoPergunta


class PerguntaCreate(PerguntaBase):
    pass


class Pergunta(PerguntaBase):
    id: int
    id_formulario: int

    model_config = ConfigDict(from_attributes=True)


class FormularioBase(BaseModel):
    titulo: str
    descricao: Optional[str]
    ordem: Optional[int]


class FormularioCreate(FormularioBase):
    pass


class Formulario(FormularioBase):
    id: int
    perguntas: List[Pergunta] = []

    model_config = ConfigDict(from_attributes=True)
