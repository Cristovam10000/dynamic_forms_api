from sqlalchemy import (
    Column, Integer, String, Boolean, Enum, ForeignKey, Numeric, Text
)
from sqlalchemy.orm import relationship
from app.db import Base
import enum

class TipoPergunta(str, enum.Enum):
    sim_nao = "sim_nao"
    mult_escolha = "mult_escolha"
    unica_escolha = "unica_escolha"
    texto_livre = "texto_livre"
    inteiro = "inteiro"
    decimal = "decimal"

class Formulario(Base): 
    __tablename__ = "formulario"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(Text)
    ordem = Column(Integer)

    perguntas = relationship(
        "Pergunta",
        back_populates = "formulario",
        cascade = "all, delete-orphan"
    )

class Pergunta(Base):
    __tablename__ = "pergunta"
    id = Column(Integer, primary_key=True, index=True)
    id_formulario = Column(Integer, ForeignKey("formulario.id", ondelete="CASCADE"), nullable=False)
    titulo = Column(String, nullable=False)
    codigo = Column(String, unique=True, index=True)
    orientacao_resposta = Column(Text)
    ordem = Column(Integer)
    obrigatoria = Column(Boolean, default=False)
    sub_pergunta = Column(Boolean, default=False)
    tipo_pergunta = Column(Enum(TipoPergunta), nullable=False)

    formulario = relationship("Formulario", back_populates="perguntas")
    opcoes = relationship(
        "OpcaoResposta", back_populates="pergunta", cascade="all, delete-orphan"
    )

class OpcaoResposta(Base):
    __tablename__ = "opcoes_respostas"
    id            = Column(Integer, primary_key=True)
    id_pergunta   = Column(Integer, ForeignKey("pergunta.id", ondelete="CASCADE"))
    resposta      = Column(String, nullable=False)
    ordem         = Column(Integer)
    resposta_aberta = Column(Boolean, default=False)
    pergunta      = relationship("Pergunta", back_populates="opcoes")

class OpcaoRespostaPergunta(Base):
    __tablename__ = "opcoes_resposta_pergunta"
    id               = Column(Integer, primary_key=True)
    id_opcao_resposta = Column(Integer, ForeignKey("opcoes_respostas.id"))
    id_pergunta      = Column(Integer, ForeignKey("pergunta.id"))
    # se quiser back_populates ou só deixe como tabela de associação
