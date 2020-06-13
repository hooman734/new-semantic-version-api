from flask import Flask, jsonify
from helpers.retrieve_v3 import resolve_version

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <div style="background-color:Tomato; color:white; text-align: center;">
    <h1>Welcome to NuGet.org api.</h1>
    <h2> <i> To use correctly, please request a path like: </i> </h2>
    <h2> <mark>/ api / {package_name} / {major | minor | patch} / json</mark></h2>
    <br />
    <hr /> 
    </div>
    """


@app.route('/api/<package_name>/<v_type>/json')
def handle_version(package_name, v_type):
    answer, code = resolve_version(package_name, v_type)
    if code == '404':
        return "404 not found."
    else:
        return jsonify(answer)


if __name__ == "__main__":
    app.run(debug=False)