import fuckdailyup as fuck
def fuckmain(username,passwd):
    cookies=fuck.login(username,passwd)
    if(cookies==0):
        return 0
    index=fuck.getindex(cookies)
    if index==0:
        return 0
    savedata=fuck.getsavedata(index)
    if savedata==0:
        return 0
    if fuck.getifsaved(index):
        print('You have already saved!')
        return 1
    return fuck.postsave(cookies,savedata)