from mock import mock
#模拟mock 封装
def mock_test(mock_method,request_data,url,method,response_data):
	'''伪造响应数据'''
	mock_method = mock.Mock(return_value=response_data) #大概意思是让这个方法始终指向这个返回值
	res = mock_method(url,method,request_data)  #执行这个方法，返回指向的返回值，最后返回
	return res