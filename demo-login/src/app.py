from flask import Flask, jsonify
from database.conector import get_users

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"response": "Hello word!"})


@app.route('/status')
def status():
    return jsonify({
        "AppName": "Flask-Docker",
        "Version": "1.0"})
 

@app.route('/auth/<name>')
def auth(name):
    user = get_users(name)
    if user is None:
        return "Usuario no existe"
    return jsonify({
        "name": user.user_name,
        "appName": "Flask-Docker",
        "version": "1.0",
        "tools" : ["Docker","Kubernets"]
        })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)