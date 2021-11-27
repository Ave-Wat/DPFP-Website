import sys
import flask
from flask import request
import os
import logging

########### Initializing Flask ###########
app = flask.Flask(__name__, static_folder='src', template_folder='templates')

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

########### The website routes ###########

@app.route('/')
def home():
    return flask.render_template('index.html', title='Panorama Project')

@app.route('/application')
def application():
    return flask.render_template("application.html", title="Panorama Project Application")

@app.route('/projects')
def projects():
    return flask.render_template("projects.html", title="Our Completed Projects")

@app.route('/projects/<project_name>')
def project(project_name):
    return flask.render_template("{project}.html".format(project=project_name), title=project_name)

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
