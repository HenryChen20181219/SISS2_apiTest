import requests
import json
from util.operation_json import OperationJson


class OperationHeader:
    def __init__(self,response):
        self.response = json.loads(response)

    def get_response_url(self):
        '''获取登录返回的token的url'''
        url = self.response['data']['url'][0]
        # print(url)
        return url

    def get_token(self):
        print(self.response)
        token = self.response["data"]["access_token"]
        print(token)
        return token

    def write_token(self):
        op_json = OperationJson("../dataconfig/token.json")
        op_json.write_data(self.get_token())

    def get_cookie(self):
        '''获取cookie的jar文件'''
        # token令牌登录，后面可能不用这个方法
        url = self.get_response_url()+"&callback='callback=jQuery210046899129685102703_1561516109616&_=1561516109618'" #拼接的地方要更改,这个回调暂时还不知道是什么意思
        cookie = requests.get(url).cookies
        print(cookie)
        return cookie

    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OperationJson()
        op_json.write_data(cookie)


if __name__ == "__main__":
    url = "http://apilabnn.ufwl.net/login"
    data = {"username":"super",
            "password":"123456",
            "agree":"true",
            "authtype":"user"}
    headers = {'Content-Type': 'application/json'}
    res = json.dumps(requests.post(url, data=json.dumps(data),headers=headers,verify=False).json())
    op_header = OperationHeader(res)
    # op_header.write_cookie() #写入cookie成功
    op_header.write_token()  #保存本项目的token令牌

