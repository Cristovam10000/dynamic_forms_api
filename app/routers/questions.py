from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session
from typing import Optional
from app import crud, schemas
from app.db import get_db

router = APIRouter(prefix="/formularios/{form_id}/perguntas", tags=["perguntas"])

@router.post("/", response_model=schemas.Pergunta)
def create_pergunta(
    form_id: int,
    perg: schemas.PerguntaCreate,
    db: Session = Depends(get_db),
):
    if not crud.get_formulario(db, form_id):
        raise HTTPException(404, "Formulário não encontrado")
    return crud.create_pergunta(db, perg, form_id)

@router.get("/", response_model=dict)
def read_perguntas(
    form_id: int,
    tipo: Optional[schemas.TipoPergunta] = Query(None),
    obrigatoria: Optional[bool] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    order_by: str = Query("ordem"),
    db: Session = Depends(get_db),
):
    total, itens = crud.list_perguntas(db, form_id, tipo, obrigatoria, skip, limit, order_by)
    return {"total": total, "items": itens}


@router.get("/{pergunta_id}", response_model=schemas.Pergunta)
def read_pergunta(form_id: int, pergunta_id: int, db: Session = Depends(get_db)):
    perg = crud.get_pergunta(db, pergunta_id)
    if not perg or perg.id_formulario != form_id:
        raise HTTPException(404, "Pergunta não encontrada")
    return perg


@router.put("/{pergunta_id}", response_model=schemas.Pergunta)
def update_pergunta(
    form_id: int,
    pergunta_id: int,
    perg_in: schemas.PerguntaCreate,
    db: Session = Depends(get_db),
):
    perg = crud.get_pergunta(db, pergunta_id)
    if not perg or perg.id_formulario != form_id:
        raise HTTPException(404, "Pergunta não encontrada")
    return crud.update_pergunta(db, perg, perg_in)


@router.delete("/{pergunta_id}", status_code=204)
def delete_pergunta(form_id: int, pergunta_id: int, db: Session = Depends(get_db)):
    perg = crud.get_pergunta(db, pergunta_id)
    if not perg or perg.id_formulario != form_id:
        raise HTTPException(404, "Pergunta não encontrada")
    crud.delete_pergunta(db, perg)
    return Response(status_code=204)
