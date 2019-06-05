import json
import subprocess

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
        if email not in emails_list:
            emails_list.append(email)
            set_config_value('recivers_emails', emails_list)


def wifi_connect(ssid, password):
    subprocess.run(f'./wifi_connection.sh {ssid} {password}', shell=True)
