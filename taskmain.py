import fuckmain as fuck
import json
import os
def taskmain():
    if not os.path.exists('users.json'):
        print('No config file')
    users={}
    with open('users.json','r',encoding='utf-8') as fp:
        users=json.load(fp)
    for user in users:
        passwd=users[user]
        if not os.path.exists(user):
            os.mkdir(user)
        os.chdir(user)
        try:
            if fuck.fuckmain(user,passwd):
                print('##### Success: {} with {}'.format(user,passwd))
            else:
                print('##### Failure: {} with {}'.format(user,passwd))
        except Exception as e:
            print('##### Failure: {} with {} exception'.format(user,passwd))
            print(e)
        finally:
            os.chdir('..')