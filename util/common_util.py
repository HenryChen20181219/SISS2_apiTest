# import json
# import  operator


class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''判断一个str_one字符串是否在另一个字符串str_two中'''
        flag = False
    #文件中读取出的是字节， 可能需要转换字节成字符串
        # if isinstance(str_one,str):
        #     str_one.encode("utf-8")
        if str_one in str_two:
            flag = True
        return flag

    def is_equal_dict(self,dict_one,dict_two):
        '''判断两个字典是否相等'''
        # if isinstance(dict_one,str):
        #     dict_one = json.load(dict_one)
        # if isinstance(dict_two,str):
        #     dict_two = json.load(dict_two)
        # return operator.eq(dict_one,dict_two)
        return dict_one == dict_two
        #好像用==也可以，就不用导包了


#别人写的字典相等
# def get_cmp_dict(self, src_data, dst_data):
#     if isinstance(src_data, str):
#         src_data = json.dumps(src_data)
#     if isinstance(dst_data, str):
#         dst_data = json.dumps(dst_data)
#     if len(src_data) != len(dst_data):
#         return False
#     else:
#         src_key = list(src_data.keys())
#         dst_key = list(dst_data.keys())
#         if operator.eq(src_key, dst_key):
#             src_val = list(src_data.values())
#             dst_val = list(dst_data.values())
#             if operator.eq(src_val, dst_val):
#                 for key in src_data.keys():
#                     if src_data[key] != dst_data[key]:
#                         # print(src_data1[key])
#                         return False
#                 return True
#             else:
#                 return False
#         else:
#             return False