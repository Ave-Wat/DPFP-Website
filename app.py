import sys
import flask
from flask_mail import Mail, Message
import tokens
from flask import request

########### Initializing Flask ###########
app = flask.Flask(__name__, static_folder='src', template_folder='templates')
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'davis.pf.peace@gmail.com'
app.config['MAIL_PASSWORD'] = tokens.password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


########### The website routes ###########
@app.route('/')
def get_main_page():
    ''' This is the only route intended for human users '''
    return flask.render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(tokens.password)
    form_input = request.form.get('form-input', 'default value')
    msg = Message('subject line', sender = 'davis.pf.peace@gmail.com', recipients = ['davis.pf.peace@gmail.com'])
    print(form_input)
    msg.body = form_input
    mail.send(msg)

    return 'SENT'

@app.route('/application')
def application():
    return flask.render_template("application.html")

########### Running the website server ###########
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
