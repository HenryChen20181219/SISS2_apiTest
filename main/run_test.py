# import sys
# sys.path.append("E:/办公/测试用例/接口自动化") #这句话没什么用，以后想在命令行运行，就加入项目目录到环境变量
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.send_email import SendEmail
from data.dependent_data import DependentData
from util.operation_header import OperationHeader
from util.operation_json import OperationJson


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()

    #程序执行
    def go_on_run(self):
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                #获取excel中填写的url
                url = self.data.get_request_url(i)
                # 获取excel中填写的请求类型
                method = self.data.get_request_method(i)
                #先获取excel填写的请求数据user,再从user.json获取user对应的值，是个字典,即请求参数，自己的要更改
                request_data = self.data.get_data_for_json(i)
                print(request_data)
                # expect = self.data.get_expect_data_for_mysql(i) #以后用数据库维护时再用sql语句
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data

                #保存请求头
                if header == "write":
                    res = self.run_method.run_main(method,url,request_data)
                    op_header = OperationHeader(res)
                    op_header.write_cookie()

                elif header == 'yes':
                    op_json = OperationJson('../dataconfig/token.json')
                    token = op_json.read_data()
                    cookies = {
                        'Authorization': 'Bearer '+token
                    }
                    print(cookies)
                    res = self.run_method.run_main(method, url, request_data, cookies)
                else:
                    res = self.run_method.run_main(method, url, request_data)

                expect = str(expect)

                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
                # self.send_mail.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()



