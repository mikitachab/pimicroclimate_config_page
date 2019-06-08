import json
import subprocess
from validate_email import validate_email
from flask import flash

config_path = 'config.json'


def get_config_json():
    with open(config_path) as config_file:
        return json.loads(config_file.read())


def save_config(config):
    with open(config_path, 'w') as config_file:
        config_file.write(json.dumps(config, indent=2))


def set_config_value(key, value):
    config = get_config_json()
    config[key] = value
    save_config(config)


def get_config_value(key):
    config = get_config_json()
    return config[key]


def udpate_emails_list(emails):
    emails = emails.split(',')
    print(emails)
    for email in emails:
        email = email.strip()
        emails_list = get_config_value('recivers_emails')
        if email not in emails_list and validate_email(email):
            emails_list.append(email)
            set_config_value('recivers_emails', emails_list)
            flash(f'email {email} added')

        else:
            flash(f'invalid email: "{email}"')


def config_delete_mail(index):
    mails = get_config_value('recivers_emails')
    mail = mails[index]
    del mails[index]
    flash(f'email {mail} deleted')
    set_config_value('recivers_emails', mails)


def wifi_connect(ssid, password):
    subprocess.run(f'./wifi_connection.sh {ssid} {password}', shell=True)
