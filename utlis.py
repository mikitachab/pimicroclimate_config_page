import json
import subprocess


def set_config_value(key, value):
    config_path = 'config.json'
    with open(config_path) as config_file:
        config = json.loads(config_file.read())

    config[key] = value

    with open(config_path, 'w') as config_file:
        config_file.write(json.dumps(config, indent=2))


def wifi_connect(ssid, password):
    subprocess.run(f'./wifi_connection.sh {ssid} {password}', shell=True)
