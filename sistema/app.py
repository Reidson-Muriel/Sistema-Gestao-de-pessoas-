import os
from flask import Flask, render_template
from flask_cors import CORS
from sistema.routes.contatos_routes import contato_bp
from sistema.database import conexao

app = Flask(__name__, template_folder="templates", static_folder="static")
conexao.criar_tabela()
CORS(app)
app.register_blueprint(contato_bp)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/buscar")
def buscar():
    return render_template("buscar_dados.html")
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")
    
## rota para exercutar no dispositivo moveis
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) 