from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
