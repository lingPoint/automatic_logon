# coding=utf-8
#天信校园网自动登录3.0
import time
import webbrowser
import requests

# 打开文本文件
fp = open('path', 'r')
# 使用readlines读取
lines = fp.readlines()
list = {}

for line in lines:
    # 将读取的每行内容过滤掉换行符,如果不加这个条件，输入的内容中将会添加换行符\n
    line = line.strip('\n')
    ss = line.split(':')  # 将每行内容根据:分割
    list[ss[0]] = ss[1]
user = ss[0]
password = ss[1]
#print(user)
#print(password)
fp.close()

url = 'http://10.102.1.35/eportal/InterFace.do?method=login'
data = {
        'userId': user,
        'password': password,
        'service': '',
        'queryString': 'wlanuserip%25',
        'operatorPwd': '',
        'operatorUserId': '',
        'validcode': 'false',
        'passwordEncrypt': 'false'
    }
r = requests.post(url,data)
r.encoding='utf-8'           
#print(r)
print(r.text)
if '"result":"fail"' in r.text:
        print('检查配置文件账号密码是否正确！！')
else:
        print('登录成功')
        time.sleep(1)
        #browser = webbrowser.open("http://10.102.1.35/")