import sys
import time
import os
from flask import Flask, render_template, flash, redirect
from forms import ConfigForm, DeviceConfigForm
from utlis import set_config_value
from utlis import wifi_connect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def config_page():
    form = ConfigForm()
    if form.validate_on_submit():
        flash('requested for user {}, {}'.format(
            form.ssid.data, form.email.data))
        print(form.ssid.data, form.email.data, form.ip_address.data)
        ssid = form.ssid.data
        password = form.password.data
        if on_raspi:
            wifi_connect(ssid, password)
            sys.exit(0)
        return redirect('/')
    else:
        for field, error in form.errors.items():
            flash(f'Troubles with field {getattr(form, field).label.text}: {" ".join(error)}')
    return render_template('config.html', title='config', form=form)


@app.route('/dev', methods=['GET', 'POST'])
def dev_config_page():
    form = DeviceConfigForm()
    if form.validate_on_submit():
        if form.measurements_count.data:
            set_config_value('min_measurements_count', form.measurements_count.data)
            flash('config value was set')
            return redirect('/')
    else:
        for field, error in form.errors.items():
            flash(f'Troubles with field {getattr(form, field).label.text}: {" ".join(error)}')
    return render_template('dev_config.html', title='dev-config', form=form)


if __name__ == '__main__':
    on_raspi = False
    if on_raspi:
        subprocess.Popen('sudo ./start_hotspot.sh', shell=True)
        time.sleep(10)
        app.run(host='192.168.0.10')
    else:
        app.run()
