import sys
import flask
from flask_mail import Mail, Message
from flask import request
import os

########### Initializing Flask ###########
app = flask.Flask(__name__, static_folder='src', template_folder='templates')

########### The website routes ###########
@app.route('/')
def get_main_page():
    return flask.render_template('index.html')

@app.route('/home')
def home():
    return flask.render_template('index.html')

@app.route('/application')
def application():
    return flask.render_template("application.html")

@app.route('/projects')
def projects():
    return flask.render_template("projects.html")

@app.route('/projectImmigration')
def projectImmigration():
    return flask.render_template("CarterGeorge_GabbyWatson_Final Draft.html")

@app.route('/<path:path>')
def shared_header_catchall(path):
    return flask.render_template(path)

########### Running the website server ###########
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
    app.run()
