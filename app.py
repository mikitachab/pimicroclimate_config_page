import subprocess
import sys
import time
import os
from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, IPAddress
from save_config import save_data

app = Flask(__name__)
app.config['SECRET_KEY'] = '00b596b981ee3a3d89afbd5b'


class LoginForm(FlaskForm):
    ssid = StringField('Network Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    ip_address = StringField('Server IP address', validators=[IPAddress()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('requested for user {}, {}'.format(
                form.ssid.data, form.email.data))
        
        ssid = form.ssid.data
        password = form.password.data
        wifi_connect(ssid, password)
        sys.exit(0)
        return redirect('/')
    return render_template('config.html', title='config', form=form)


def wifi_connect(ssid, password):
    subprocess.run(f'./wifi_connection.sh {ssid} {password}', shell=True)

if __name__ == '__main__':
    subprocess.Popen('sudo ./start_hotspot.sh', shell=True)
    time.sleep(10)
    app.run(host='192.168.0.10')




