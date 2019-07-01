import xlrd
from xlutils.copy import copy


class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/case1.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
# ②根据sheet_by_index()读取
# sheet2=table.sheet_by_index(0)
# ③根据sheet_by_name()读取
# sheet3=table.sheet_by_name("Sheet1")

    #获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取单元格列数
    def get_cols(self):
        return self.data.ncols

    #获取某个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    #写入数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data= write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #根据对应行case_id 找到对应行号
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num+1

    #根据列数获取某列的内容，如果不传就返回第一列
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

    #根据行号找到该行的内容
    def get_row_values(self,row_num):
        tables = self.data
        row_data = tables.row_values(row_num)
        return row_data

    #根据对应的case_id 找到对应行的内容
    def get_row_data(self,case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)


