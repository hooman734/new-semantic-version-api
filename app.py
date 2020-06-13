from flask import Flask, jsonify
from flask_cors import CORS
from helpers.retrieve_v3_semver import resolve_version

app = Flask(__name__)
CORS(app)
message = """
    <html>
	<div style="background-color:blue; color:white; text-align: center;">
		<h1>Welcome to NuGet.org api.</h1>
		<h2>
			<i> To use correctly, please request a path like: </i>
		</h2>
		<h2>
			<mark>/ api / {package_name} / {major | minor | patch} / json</mark>
		</h2>
		<br />
		<hr />
	</div>
</html>
    """
error_message = """
    <html>
	<div style="background-color:Tomato; color:white; text-align: center;">
		<h1>Error 404</h1>
		<h2>
			<i> It happened due to either your request path was not valid or the mentioned package not found. </i>
		</h2>
		<h2>
			<mark>Try again!</mark>
		</h2>
		<br />
		<hr />
	</div>
</html>
    
    """


@app.route('/')
def index():
    return message, 200


@app.route('/api/<package_name>/<v_type>/json')
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
    app.run(debug=False)
