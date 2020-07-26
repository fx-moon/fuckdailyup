import fuckmain
import fuckdailyup
import taskmain
import json
import os
import argparse

def adduser(username,passwd):
    cookies=fuckdailyup.login(username=username,passwd=passwd)
    if cookies==0:
        return 0
    users={}
    with open('users.json','r',encoding='utf-8') as fp:
        users=json.load(fp)
    users[username]=passwd
    with open('users.json','w',encoding='utf-8') as fp:
        json.dump(users,fp,ensure_ascii=False)
    taskmain.taskmain()
    return 1

def removeuser(username):
    users={}
    with open('users.json','r',encoding='utf-8') as fp:
        users=json.load(fp)
    if username in users:
        del users[username]
    else:
        return 0
    with open('users.json','w',encoding='utf-8') as fp:
        json.dump(users,fp,ensure_ascii=False)
        return 1
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--add',nargs=2,type=str,help='add user')
    parser.add_argument('-d','--delete',type=str,help='delete user')
    args=parser.parse_args()
    if args.add!=None:
        if adduser(args.add[0],args.add[1]) ==1:
            print('Success')
        else:
            print('Fail')
    if args.delete!=None:
        if removeuser(args.delete)==1:
            print('Success')
        else:
            print('Fail')