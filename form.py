from flask import Flask, render_template, session, url_for
from wtforms import StringField, SubmitField, BooleanField, DateTimeField
from wtforms import RadioField, SelectField, TextField, TextAreaField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InputMethod(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired(message="*Required")])
    submit = SubmitField("Submit")

class SignUpForm(FlaskForm):
    name = StringField("Enter your name.", validators=[DataRequired()])
    username = StringField("Create a username.", validators=[DataRequired(message="*Required")])
    #password = PasswordField("Create a password.", validators=[DataRequired(message="*Required")])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def index():
    name = False
    form = InputMethod()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""

    return render_template('index.html', name=name, form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        #password = form.password.data

        form.name.data = ""
        form.username.data = ""
        #form.password.data = ""
        return render_template('signup.html', name=name, form=form, username=username)

    return render_template('signup.html', form=form)
