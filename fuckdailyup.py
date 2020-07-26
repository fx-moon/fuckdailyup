import requests
import json
import os


def login(username, passwd):

    url = "https://xxcapp.xidian.edu.cn/uc/wap/login/check"

    payload = 'password='+passwd+'&username='+username
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.26 Safari/537.36 Edg/85.0.564.13',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        print(response.json()['m'])
        if not response.json()['e']:
            cookies = response.cookies
            print("cookies saved")
            return cookies
        else:
            return 0
    else:
        print("request failed")
        return 0


def getindex(cookies):
    url = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/index"

    payload = {}
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.26 Safari/537.36 Edg/85.0.564.13',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
    }

    response = requests.request(
        "GET", url, headers=headers, data=payload, cookies=cookies)
    if response.status_code == 200:
        print(response.json()['m'])
        if not response.json()['e']:
            return response.json()['d']
        else:
            return 0
    else:
        print("request failed")
        return 0


def getdataindex(payload=''):
    rdata = ['address', 'area', 'city', 'geo_api_info', 'province',
             'qtqk', 'sfcyglq', 'sfyzz', 'sfzx', 'tw', 'ymtys']
    if payload == '':
        dataindex = rdata
    else:
        dataindex = [i.split('=')[0] for i in payload.split('&')]
    if dataindex != rdata:
        print("## Alert! Data index changed!!!!")
    return dataindex

def getifsaved(index):
    if index['info']['geo_api_info'] == '':
        return False
    else:
        return True

def getsavedata(index={}):
    savedata = {}
    if index != {}:
        if index['info']['geo_api_info'] != '':
            fp = open('save.json', 'w', encoding='utf-8')
            json.dump(index, fp, ensure_ascii=False)
            print('Data saved')
    if not os.path.exists('save.json'):
        print('## Alert! No cached data!!!!')
        return 0
    fp = open('save.json', 'r', encoding='utf-8')
    index = json.load(fp)
    data = index['info']
    dataindex = getdataindex()
    for i in dataindex:
        if i in data:
            savedata[i] = data[i]
        else:
            print("## Alert! Missing Data index!!!!")
    return savedata


def postsave(cookies, savedata):
    url = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save"
    dataindex = getdataindex()
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.26 Safari/537.36 Edg/85.0.564.13',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
    }

    response = requests.request("POST", url, headers=headers, data=savedata, cookies=cookies)

    if response.status_code == 200:
        print(response.json()['m'])
        if not response.json()['e']:
            return 1
        else:
            return 0
    else:
        print("request failed")
        return 0