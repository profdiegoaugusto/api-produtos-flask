from sqlalchemy import Column, BigInteger, String, Integer, Numeric, DateTime, CheckConstraint
from sqlalchemy.sql.functions import current_timestamp

from app import db


class Produto(db.Model):

    __tablename__ = 'Produto'

    id = Column(BigInteger, primary_key=True)
    nome = Column(String(128), nullable=False)
    quantidade = Column(Integer, CheckConstraint('quantidade >= 0'), nullable=False, server_default="0")
    preco = Column(Numeric(10, 2), CheckConstraint('preco >= 0.0'), nullable=False, server_default="0.0")

    criado_em = Column(DateTime, server_default=current_timestamp())
    modificado_em = Column(
        DateTime,
        server_default=current_timestamp(),
        onupdate=current_timestamp())

    def __init__(self, nome: str = "", quantidade: int = 0, preco: float = 0.0) -> None:
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Produto: {self.nome}>'
    
class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produto
        sqla_session = db.session
        load_instance = True

    id = ma.auto_field()
    nome = ma.auto_field()
    preco = ma.auto_field()
    quantidade = ma.auto_field()
