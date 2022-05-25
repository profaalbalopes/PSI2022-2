from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/contato')
def exibir_contato():
  return render_template('contato.html', nome="José", email="meu@email")

@app.route('/usuario', defaults={"nome": "usuario comum", "email": "sem email"})
@app.route('/usuario/<nome>/<email>')
def usuario(nome, email):
  return render_template('usuario.html', nome=nome, email=email)


@app.route('/soma', defaults={"op1": "0", "op2": "0"})
@app.route('/soma/<op1>/<op2>')
def soma(op1, op2):
  r = int(op1) + int(op2)
  return "Soma {}".format(r)


@app.route('/galeria/<id>')
def galeria(id):
  return render_template('galeria.html', id=id)


@app.route('/novagaleria/<id>')
def novagaleria(id):
  return render_template('galeria.html', id=id)


app.run(host='0.0.0.0', port=81)