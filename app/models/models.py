from app import db

# Define a classe 'Users', que representa a tabela de usuários no banco de dados
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False) 
    password = db.Column(db.String(120), nullable=False) 

    def __repr__(self):
        return f'<Usuario {self.username}, {self.password}>'