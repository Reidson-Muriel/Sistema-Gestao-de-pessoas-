import os
from flask import Flask, render_template, session, redirect
from flask_cors import CORS
from sistema.routes.contatos_routes import contato_bp
from sistema.routes.usuarios_routes import usuario_bp
from sistema.database.conexao import criar_tabela, criar_tabela_usuarios, conectar

app = Flask(__name__, template_folder="templates", static_folder="static")
criar_tabela()
criar_tabela_usuarios()
app.secret_key = "chave_secreta"
CORS(app)
app.register_blueprint(contato_bp)
app.register_blueprint(usuario_bp)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/index")
def index():
    if "usuario" not in session:
        return redirect("/login")
        
    return render_template("index.html")
@app.route("/buscar")
def buscar():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("buscar_dados.html")
@app.route("/cadastro")
def cadastro():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("cadastro.html")
@app.route("/login")
def pagina_login():
    return render_template("login.html")
@app.route("/criar-login")
def cadastro_login():
    return render_template("cadastro_login.html")
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/")
# proteger o login em cache

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store"
    return response
    
## rota para exercutar no dispositivo moveis
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False) 