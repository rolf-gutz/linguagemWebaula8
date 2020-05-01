from aplicacao import app
from flask import render_template


@app.route('/')
def index():
    context = {'titulo':'Pagina flask',
                'outro': 'Novo Texto',
                'lista': ['a','b','c']}
    retorno = render_template('index.html',**context)
    print(retorno)
    return retorno

app.run(debug=True)
