from instance import config

# Declaração para habilitar o ambiente de desenvolvimento
DEBUG = True

# Definição do Banco de Dados MySQL
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db}'

DATABASE_CONNECT_OPTIONS = {}

SQLALCHEMY_TRACK_MODIFICATIONS = False