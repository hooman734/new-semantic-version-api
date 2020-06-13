from flask import Flask, jsonify
from helpers.retrieve_v3 import resolve_version

app = Flask(__name__)
message = """
    <div style="background-color:blue; color:white; text-align: center;">
    <h1>Welcome to NuGet.org api.</h1>
    <h2> <i> To use correctly, please request a path like: </i> </h2>
    <h2> <mark>/ api / {package_name} / {major | minor | patch} / json</mark></h2>
    <br />
    <hr /> 
    </div>
    """
error_message = """
    <div style="background-color:Tomato; color:white; text-align: center;">
    <h1>Error 404</h1>
    <h2> <i> It happened due to or your request path was not valid either the mentioned package not found. </i> </h2>
    <h2> <mark>Try again!</mark></h2>
    <br />
    <hr /> 
    </div>
    """


@app.route('/')
def index():
    return message, 200


@app.route('/api/<package_name>/<v_type>/json')
def handle_version(package_name, v_type):
    answer, code = resolve_version(package_name, v_type)
    if code == '404':
        return message + error_message, 404
    else:
        return jsonify(answer), 200


@app.errorhandler(404)
def page_not_found(error):
    return message + error_message, 404


if __name__ == "__main__":
    app.run(debug=False)

