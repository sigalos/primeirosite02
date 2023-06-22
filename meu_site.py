from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/quina", methods=["post"])
def quina():
    return render_template("quina.html")

@app.route("/mega", methods=["post"])
def mega():
    return render_template("mega.html")

@app.route("/usuarios/<nome_usuario>", methods=["post"])
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
