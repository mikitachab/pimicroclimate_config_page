import os

def save_data(**kwargs):
    print(kwargs)
    with open('data.txt', 'w') as f:
        for key, value in kwargs.items():
            f.write(f'{key}={value}' + '\n')
    
    wpa_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
    with open(wpa_file, 'a') as f:
        ssid = kwargs['ssid']
        password = kwargs['password']
        f.write('\n')
        f.write('network={' + '\n')
        f.write('\t' + f'ssid="{ssid}"' + '\n')
        f.write('\t' + f'psk="{password}"' + '\n')
        f.write('\t'+ 'key_mgmt=WPA-PSK' + '\n')
        f.write('}' + '\n')
    os.system('wpa_cli -i $INTERFACE reconfigure')
