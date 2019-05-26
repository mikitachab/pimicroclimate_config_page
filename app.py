import subprocess
import sys
import time
import os
from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, IPAddress, Optional

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


class LoginForm(FlaskForm):
    ssid = StringField('Network Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    ip_address = StringField('Server IP address', validators=[Optional(), IPAddress()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('requested for user {}, {}'.format(
            form.ssid.data, form.email.data))
        print(form.ssid.data, form.email.data, form.ip_address.data)
        ssid = form.ssid.data
        password = form.password.data
        wifi_connect(ssid, password)
        sys.exit(0)
        return redirect('/')
    else:
        for field, error in form.errors.items():
            flash(f'Troubles with field {getattr(form, field).label.text}: {" ".join(error)}')
    return render_template('config.html', title='config', form=form)


def wifi_connect(ssid, password):
    subprocess.run(f'./wifi_connection.sh {ssid} {password}', shell=True)


if __name__ == '__main__':
    subprocess.Popen('sudo ./start_hotspot.sh', shell=True)
    time.sleep(10)
    app.run(host='192.168.0.10')
