from flask import Flask, request, jsonify

app = Flask(__name__)


# Crea una ruta raíz ("/") que responda con "¡Hola Mundo!"
@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'


# Crea una ruta que responda con "¡Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'


# Crea una ruta que responda con "Hola" y el nombre que esté en la URL después de /say/
@app.route('/Hola/<name>')
def hola(name):
    print(name)
    return f"Hola {name.capitalize()}!"

# Crea una ruta que responda con la palabra dada repetida tantas veces como se especifique en la URL


@ app.route('/repite/<int:num>/<string:str>')
def repite(num, str):
    imprime = ''
    for i in range(0, num):
        imprime += f"<p>{str}</p>"

    return imprime


@ app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Lo siento!, no hay respuesta. Intentalo otra vez."}), 404


if __name__ == "__main__":
    app.run(debug=True)
