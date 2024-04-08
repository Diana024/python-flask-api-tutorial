# Importacion de Flask - libreria de python para crear un servidor de web y Apis
# , método jsonify
from flask import Flask, jsonify # type: ignore
from flask import request # type: ignore
app = Flask(__name__)

# Crear variable
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# # convertir variable en una cadena json

@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text

add_new_todo = [{ "done": "true", "label": "Sample Todo 1" }]

@app.route('/todos', methods=['POST'])
def add_new_todo():
  request_body = request.json
  todos.append(request_body)
  print("Incoming request with the following body", request_body)
  return jsonify(todos)

#   # Respuesta para el POST todo jsonify
#   # json_text = jsonify(todos)
#   # return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  # todos.remove(position)¿?
  del todos[position]
  print("Array position removed: ", position)
  return jsonify(todos)

# Estas dos líneas siempre deben estar al final de tu archivo app.py. 
# Estas dos lineas, marcan el puerto
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

