import configparser
import sys

domain = sys.argv[1]
config = configparser.ConfigParser()
config['MAIN'] = {}
config['MAIN']['domain'] = domain
config['USERS'] = {}
i = 2
while i < len(sys.argv):
    config['USERS'][sys.argv[i]] = sys.argv[i+1]
    i += 2
with open('settings.ini', 'w+') as configfile:
    config.write(configfile)
    
users = ",".join([f"{username}:{config['USERS'][username]}" for username in config['USERS']])
with open('.env', 'w') as envfile:
    envfile.writelines([f'maildomain={domain}', f'smtp_user={users}'])
