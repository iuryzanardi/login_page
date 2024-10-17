from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

# Recupera as variáveis de ambiente para configurar o banco de dados e a aplicação
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
secret_key = os.getenv('SECRET_KEY')

if not all([db_user, db_password, db_host, db_name, secret_key]):
    raise ValueError("Uma ou mais variáveis de ambiente não estão definidas corretamente")



# Cria a instância do Flask
app = Flask(__name__)

# Configura a URI de conexão com o banco de dados usando MySQL e o driver pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'

# Configura a chave secreta da aplicação (usada para sessões, proteção CSRF, etc.)
app.config['SECRET_KEY'] = secret_key

# Inicializa o SQLAlchemy, que gerencia o banco de dados
db = SQLAlchemy(app)
