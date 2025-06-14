from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify(status="ok", message="Service is healthy"), 200

@app.route('/add/<float:a>/<float:b>', methods=['GET'])
def add_numbers(a, b):
    result = a + b
    return jsonify(result=result), 200

@app.route('/hello', methods=['GET'])
def healthcheck():
    return jsonify(status="ok", message="Hello"), 200

if __name__ == '__main__':
    app.run(debug=True)