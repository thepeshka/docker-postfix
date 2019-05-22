import configparser
import argv
config = configparser.ConfigParser()
config.read('settings.ini')
domain = config['MAIN']['DOMAIN']
new_username = argv[1]
new_password = argv[2]
config['USERS'][new_username] = new_password
with open('settings.ini', 'w') as configfile:
    config.write(configfile)

users = ",".join([f"{username}:{config['USERS'][username]}" for username in config['USERS']])
with open('.env', 'w') as envfile:
    envfile.writelines([f'maildomain={domain}', f'smtp_user={users}'])
