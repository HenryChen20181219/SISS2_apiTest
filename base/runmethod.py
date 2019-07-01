import requests
import json


class RunMethod:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
    def run_main(self,method,url,data=None,header=None):
        if method == 'Post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False) #返回json字符串

    def post_main(self,url,data,header=None):
        if header != None:
            headers = dict(self.headers,**header)
            res = requests.post(url,json.dumps(data),headers=headers,verify=False)
        else:
            res = requests.post(url,json.dumps(data),headers=self.headers,verify=False)
        return res.json()

    def get_main(self,url,data=None,header=None):
        if header != None:
            res = requests.get(url, data, headers=header,verify=False) #verify验证https证书
        else:
            res = requests.get(url,data,verify=False)
        return res.json()
