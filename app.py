from flask import Flask, jsonify
from flask_cors import CORS
from codecs import open as open_html
from helpers.retrieve_v3_semver import resolve_version
from helpers.query_package import fetch_data
message = open_html("views/message.html", "r", "utf-8").read()
error_message = open_html("views/error_message.html", "r", "utf-8").read()

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return message, 200


@app.route('/api/query/<package_name>/json')
def handle_query(package_name):
    return jsonify(fetch_data(package_name))


@app.route('/api/version/<package_name>/<v_type>/json')
def handle_version(package_name, v_type):
    answer, code = resolve_version(package_name.lower(), v_type.lower())
    if code == '404':
        return message + error_message, 404
    else:
        return jsonify(answer), 200


@app.errorhandler(404)
def page_not_found(error):
    return message + error_message, 404


if __name__ == "__main__":
    app.run(debug=True)
