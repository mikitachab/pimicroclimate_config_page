from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, IPAddress, Optional


class ConfigForm(FlaskForm):
    ssid = StringField('Network Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    ip_address = StringField('Server IP address', validators=[Optional(), IPAddress()])
    submit = SubmitField('Submit')


class DeviceConfigForm(FlaskForm):
    measurements_count = IntegerField('Measurements Count', validators=[Optional()])
    submit = SubmitField('Submit')
