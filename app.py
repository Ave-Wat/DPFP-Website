import sys
import flask
from flask_mail import Mail, Message
from flask import request
import os

########### Initializing Flask ###########
app = flask.Flask(__name__, static_folder='src', template_folder='templates')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'afisherwatts@gmail.com'
app.config['MAIL_PASSWORD'] = str(os.environ.get('EMAILP'))
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


########### The website routes ###########
@app.route('/')
def get_main_page():
    return flask.render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first-name', 'default value')
    last_name = request.form.get('last-name', 'default value')
    long_question = request.form.get('long-question', 'default value')
    msg = Message(last_name + ", " + first_name, sender = 'afisherwatts@gmail.com', recipients = ['davis.pf.peace@gmail.com'])
    msg.body = first_name + ", " + last_name + ", " + long_question
    mail.send(msg)
    return flask.render_template('submitted.html')

@app.route('/application')
def application():
    return flask.render_template("application.html")

########### Running the website server ###########
if __name__ == '__main__':
    """if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)"""
    app.run()
