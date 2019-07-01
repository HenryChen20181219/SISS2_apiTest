import json


class OperationJson:

	def __init__(self,file_path=None):
		if file_path  == None:
			self.file_path = '../dataconfig/user.json'
		else:
			self.file_path = file_path
		self.data = self.read_data()

	#读取json文件
	def read_data(self):
		with open(self.file_path) as fp:
			data = json.load(fp)
			return data

	#根据关键字获取数据
	def get_data(self,id):
		print(type(self.data)) #应该是个字典
		return self.data[id]

	#写json
	def write_data(self,data):
		with open(self.file_path,'w') as fp:
			fp.write(json.dumps(data))


if __name__ == '__main__':
	opjson = OperationJson()
	print(opjson.get_data('shop')) #传入的shop要改，实际写入cookie字典获取关键参数获取