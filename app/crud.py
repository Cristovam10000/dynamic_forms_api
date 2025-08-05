from sqlalchemy.orm import Session
from app import models, schemas


# ---------------------------------------------------------------------------
# Formulários
# ---------------------------------------------------------------------------

def create_formulario(db: Session, form: schemas.FormularioCreate):
    db_f = models.Formulario(**form.dict())
    db.add(db_f)
    db.commit()
    db.refresh(db_f)
    return db_f


def get_formulario(db: Session, form_id: int):
    return db.query(models.Formulario).filter(models.Formulario.id == form_id).first()


def list_formularios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Formulario).offset(skip).limit(limit).all()


def update_formulario(
    db: Session, db_form: models.Formulario, new_data: schemas.FormularioCreate
):
    for field, value in new_data.dict(exclude_unset=True).items():
        setattr(db_form, field, value)
    db.commit()
    db.refresh(db_form)
    return db_form


def delete_formulario(db: Session, db_form: models.Formulario):
    db.delete(db_form)
    db.commit()


# ---------------------------------------------------------------------------
# Perguntas
# ---------------------------------------------------------------------------

def create_pergunta(db: Session, perg: schemas.PerguntaCreate, form_id: int):
    db_p = models.Pergunta(**perg.dict(), id_formulario=form_id)
    db.add(db_p)
    db.commit()
    db.refresh(db_p)
    return db_p


def get_pergunta(db: Session, pergunta_id: int):
    return db.query(models.Pergunta).filter(models.Pergunta.id == pergunta_id).first()


def list_perguntas(
    db: Session,
    form_id: int,
    tipo: schemas.TipoPergunta = None,
    obrigatoria: bool = None,
    skip: int = 0,
    limit: int = 10,
    order_by: str = "ordem",
):
    q = db.query(models.Pergunta).filter(models.Pergunta.id_formulario == form_id)
    if tipo:
        q = q.filter(models.Pergunta.tipo_pergunta == tipo)
    if obrigatoria is not None:
        q = q.filter(models.Pergunta.obrigatoria == obrigatoria)
    total = q.count()
    itens = (
        q.order_by(getattr(models.Pergunta, order_by)).offset(skip).limit(limit).all()
    )
    return total, itens


def update_pergunta(
    db: Session, db_perg: models.Pergunta, new_data: schemas.PerguntaCreate
):
    for field, value in new_data.dict(exclude_unset=True).items():
        setattr(db_perg, field, value)
    db.commit()
    db.refresh(db_perg)
    return db_perg


def delete_pergunta(db: Session, db_perg: models.Pergunta):
    db.delete(db_perg)
    db.commit()
