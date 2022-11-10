import subprocess

LSSID = []

info = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='cp858')

for line in info.split('\n'):
    if 'Todos os Perfis de Usuários' in line:
        pos2d = line.find(':')
        LSSID.append(line[pos2d+2:])

print(f'{"Wifi Passwords":>30} \n','_--_'*10,'\n', f'{"SSID":22}|{"PASSWORD":>10} \n','-_-_'*10)


for SSID in LSSID:
    ssid_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', SSID, 'key', '=', 'clear'], encoding='cp858')
    for line in ssid_data.split('\n'):
        if 'Conteúdo da Chave' in line:
            pos2d = line.find(':')
            password = line[pos2d+2:]
    print (f'{SSID:22} -->   {password}')

print('_-_-_'*10)