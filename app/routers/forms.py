from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db import get_db

router = APIRouter(prefix="/formularios", tags=["formularios"])

@router.post("/", response_model=schemas.Formulario, status_code=status.HTTP_201_CREATED)
def create_form(f: schemas.FormularioCreate, db: Session = Depends(get_db)):
    return crud.create_formulario(db, f)

@router.get("/", response_model=list[schemas.Formulario])
def read_forms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.list_formularios(db, skip, limit)

@router.get("/{form_id}", response_model=schemas.Formulario)
def read_form(form_id: int, db: Session = Depends(get_db)):
    db_f = crud.get_formulario(db, form_id)
    if not db_f:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")
    return db_f

@router.put("/{form_id}", response_model=schemas.Formulario)
def update_form(
    form_id: int,
    f: schemas.FormularioCreate,
    db: Session = Depends(get_db),
):
    db_f = crud.get_formulario(db, form_id)
    if not db_f:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")
    return crud.update_formulario(db, db_f, f)

@router.delete("/{form_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_form(form_id: int, db: Session = Depends(get_db)):
    db_f = crud.get_formulario(db, form_id)
    if not db_f:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")
    crud.delete_formulario(db, db_f)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
