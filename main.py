from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from app import app
from app.models.models import Users

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se a requisição for do tipo POST, processa o login
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Busca o usuário no banco de dados 
        user = Users.query.filter_by(username=username).first()

        # Verifica se o usuario existe e se a senha esta correta
        if user and check_password_hash(user.password, password):
            return redirect(url_for('dashboard'))
        else:
            flash('Nome de usuário ou senha inválidos.')
            return redirect(url_for('login'))
    
    # Renderiza a página de login se o método for GET
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Renderiza a página do dashboard
    return render_template('dashboard.html')

if __name__ == '__main__':
    # Executa a aplicação Flask em modo debug
    app.run(debug=True)
    
