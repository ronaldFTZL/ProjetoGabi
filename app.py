from flask import Flask, render_template, request, Response, url_for
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
db = SQLAlchemy(app)


class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    cnpj = db.Column(db.String(12))
    cidade = db.Column(db.String(20))
    estado = db.Column(db.String(20))
    ramo = db.Column(db.String(20))
    conduta = db.Column(db.String(20))

    def to_json(self):
        return {"id": self.id, "nome": self.nome_empresa, "cnpj": self.cnpj, "cidade": self.cidade,
                "estado": self.estado, "ramo": self.ramo, "conduta": self.conduta}


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if (mensagem):
        body["mensagem"] = mensagem

        return Response(json.dumps(body), status=status, mimetype="application/json")


@app.route("/", methods=["GET"])
def seleciona_empresas():
    empresas_objetos = Empresa.query.all();
    empresas_json = [empresa.to_json() for empresa in empresas_objetos]
    return  render_template("index.html", empresas=empresas_objetos)

#
# @app.route("/empresa/<id>", methods=["GET", "POSt"])
# def seleciona_empresa(id):
#     empresa_objeto = Empresa.query.filter_BY(id=id).first()
#     empresa_json = empresa_objeto.to_json()
#     return gera_response(200, "usuarios", empresa_json)
#
#
# @app.route("/Empresa", methods=["POST"])
# def insere_empresa():
#     body = request.get_json()
#
#     try:
#         empresa = Empresa(nome_empresa=body["nome"], cnpj=body["cnpj"], cidade=body["cidade"], estado=body["estado"]
#                           , ramo=["ramo"], conduta=["conduta"])
#         db.session.add(empresa)
#         db.session.commiit()
#
#         return gera_response(201, "empresa", empresa.to_json(), "Criado com sucesso")
#     except Exception as e:
#         print(e)
#         return gera_response(400, "Empresa", {}, "erro ao cadastrar")
#
#

#
# @app.route('/', methods=['POST', 'GET'])
# def index():
#     # if request.method == 'GET':
#     #     return "pega empresa"
#     # else:
#     return render_template("index.html")
#
#
# @app.route('/empresa', methods=['POST', 'GET'])
# def index():
#     if request.method == '/empresa/GET':
#         #     return "pega empresa"   32:52pip
#         # else:
#         return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
