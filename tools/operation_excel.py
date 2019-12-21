#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: operation_excel.py
@time: 2019/12/19 16:54
@desc:
'''
import xlrd
class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        # 如果file_name存在
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
            self.data = self.get_data()
        else:
            self.file_name = '../dataconfig/indence.xlsx'
            self.sheet_id = 0
            self.data = self.get_data()

    def get_data(self):
        """
        获取sheets的内容
        :return:
        """
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """
        获取单元格的行数
        :return:
        """
        tables = self.data
        return tables.nrows

    def get_cell_value(self,row,col):
        """
        获取某一个单元格的内容
        :param row: 行
        :param col: 列
        :return:
        """
        return self.data.cell_value(row,col)





if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_cell_value(1,3))
