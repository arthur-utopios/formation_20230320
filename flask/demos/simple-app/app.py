from flask import Flask, abort, redirect, url_for
from flask import render_template
from flask import request

# On instancie un objet Flask avec le nom du fichier
app = Flask(__name__)

# Définition d'une route à l'aide d'un décorateur
@app.route('/')
# Définition d'une vue
def hello_world():
    # On peut récupérer des informations sur la requête
    print(request.method)

    return 'hello world!'

# Pour ajouter un paramètre à un URL on le met entre chevrons
@app.route('/say-hello/<name>')
def hello_name(name: str):
    return render_template('index.html', name=name)

# On peut définir des routes par rapport au type de requête HTTP
# Utilisation de plusieurs routes et de paramètres par défaut
@app.get('/goodbye', defaults={'name': None})
@app.get('/goodbye/<name>')
def goodbye(name: str):
    if name is None:
        return 'goodbye'
    return f'goodbye {name}'
    

@app.route('/aurevoir')
def aurevoir():
    # Redirection avec la fonction redirect et url_for pour faire référence à une vue
    return redirect(url_for('goodbye', name='default'))

# Lever une exception HTTP
@app.route('/secret')
def top_secret():
    abort(403)
