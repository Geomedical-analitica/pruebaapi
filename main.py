#main.py
from flask import Flask, jsonify, request
from db import get_songs, add_songs

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def padre():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Falta JSON en la solicitud"}), 400  

        add_padre(request.get_json())
        return 'Padre Agregado'

    return get_padre()    

if __name__ == '__main__':
    app.run()


