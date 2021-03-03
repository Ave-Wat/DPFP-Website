import sys
import flask

########### Initializing Flask ###########
app = flask.Flask(__name__, static_folder='src', template_folder='templates')

########### The website routes ###########
@app.route('/')
def get_main_page():
    ''' This is the only route intended for human users '''
    return flask.render_template('index.html')

@app.route('/submit')
def handle_app_submission():
    #hopefully will be able to send an email from an admin account to itself containing the form contents
    pass

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
