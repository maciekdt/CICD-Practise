from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify(status="ok", message="Service is healthy"), 200

if __name__ == '__main__':
    app.run(debug=True)