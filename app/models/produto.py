from flask_sqlalchemy import Model
from sqlalchemy import Column, BigInteger, String, Integer, Float, DateTime
from sqlalchemy.sql.functions import current_timestamp


class Produto(Model):

    __tablename__ = 'Produto'

    id = Column(BigInteger, primary_key=True)
    nome = Column(String(128), nullable=False)
    quantidade = Column(Integer, nullable=False, default=0)
    preco = Column(Float, nullable=False, default=0.0)

    criado_em = Column(DateTime, default=current_timestamp())
    modificado_em = Column(
        DateTime,
        default=current_timestamp(),
        onupdate=current_timestamp())






