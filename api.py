from flask import Flask, jsonify
from datetime import datetime
import yaml


def get_app_version():
    with open("application_properties.yaml") as ymlfh:
        cfg = yaml.load(ymlfh)
    return cfg['app']['version']
    
app = Flask(__name__)
started = datetime.now()

@app.route("/")
def hello():
    return "Hello!"

@app.route("/healthz")
def health():
    json_data = {
        "status": "OK",
        "version": get_app_version(),
        "uptime": "up since "+ started.strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(host="localhost", port=8080)
    # app.run(host="localhost", port=8080, debug=True)

