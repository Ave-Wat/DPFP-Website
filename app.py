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
    name = request.form.get('name', 'default value')
    age = request.form.get('age', 'default value')
    school = request.form.get('school', 'default value')
    location = request.form.get('location', 'default value')
    ideaology = request.form.get('ideaology', 'default value')
    news = request.form.get('news', 'default value')
    long_question_1 = request.form.get('long-question1', 'default value')
    long_question_2 = request.form.get('long-question2', 'default value')
    msg = Message(name, sender = 'afisherwatts@gmail.com', recipients = ['davis.pf.peace@gmail.com'])
    msg.body = name + ", " + age + ", " + school + ", " + location + ", " + ideaology + "\n" + news + "\n" + long_question_1 + "\n" + long_question_2
    mail.send(msg)
    return flask.render_template('submitted.html')

@app.route('/application')
def application():
    return flask.render_template("application.html")

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
