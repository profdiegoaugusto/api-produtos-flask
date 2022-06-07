# Visão Geral

| HTTP | URL | Descrição | Corpo da Solicitação | Corpo da Resposta |
| --- | --- | --- | --- | --- |
| GET | `/api/v1/produtos` | Obter todos os produtos. | Nenhum | Lista de produtos |
| GET | `/api/v1/produtos/{id}` | Obter um produto por ID. | Nenhum | Item de produto |
| POST | `/api/v1/produtos` | Adicionar um novo produto. | Produto | Item de produto |
| PUT | `/api/v1/produtos/{id}` | Atualizar um produto existente. | Produto | Nenhum |
| DELETE | `/api/v1/produtos/{id}` | Excluir um produto. | Nenhum | Nenhum |

# Pré-Requisitos

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [FlaskSQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [PyMySQL](https://pypi.org/project/PyMySQL/)
- [Flask Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)

```
pip3 install -r requirements.txt

```

# Organizando o Projeto

Quando você está trabalhando em um projeto um pouco mais complexo, um único módulo pode ficar confuso. Você precisará definir classes para modelos e formulários, e eles serão misturados com o código para suas rotas e configuração. Tudo isso pode frustrar o desenvolvimento. Para resolver esse problema, podemos decompor os diferentes componentes do nosso aplicativo em um grupo de módulos interconectados, ou seja, um pacote.

```
config.py
requirements.txt
run.py
instance/
    config.py
app/
    __init__.py
    controllers/
    models/
```

| Arquivo | Descrição |
| --- | --- |
| config.py | Este arquivo contém a maioria das variáveis de configuração que seu aplicativo precisa. |
| requirements.txt | Este arquivo lista todos os pacotes Python dos quais seu aplicativo depende. Você pode ter arquivos separados para dependências de produção e desenvolvimento. |
| app.py | Este é o arquivo principal da sua aplicação. Aqui, todos os outros módulos são carregados e a aplicação é definida. |
| /instance/config.py | Este arquivo contém variáveis de configuração que não devem estar no controle de versão. Ele inclui coisas como chaves de API e URIs de banco de dados contendo senhas. Também contém variáveis específicas para essa instância específica do seu aplicativo. Por exemplo, você pode ter DEBUG = False em config.py, mas defina DEBUG = True em instance/config.py em sua máquina local para desenvolvimento. Como este arquivo será lido após o config.py, ele o substituirá e definirá DEBUG = True. |
| /models | É aqui que você define os modelos de seu aplicativo. Ele gerencia diretamente os dados, a lógica e as regras de negócio da aplicação. |
| /controllers | O controlador responde à entrada do usuário e realiza interações nos objetos do modelo de dados. O controlador recebe a entrada, valida-a opcionalmente e depois passa a entrada para o modelo. |
| /db |  |

