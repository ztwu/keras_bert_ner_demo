# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 13:55
# @Author  : ztwu4
# @Email   : ztwu4@iflytek.com
# @File    : test.py
# @Software: PyCharm

# 测试句子
from load_data import read_data
from model_train import PreProcessInputData
from util import train_file_path, test_file_path

text = "经过工作人员两天的反复验证、严密测算，记者昨天从上海中心大厦得到确认：被誉为上海中心大厦“定楼神器”的阻尼器，在8月10日出现自2016年正式启用以来的最大摆幅。"
word_labels, seq_types = PreProcessInputData([text])
print(word_labels)
print(seq_types)

input_train, result_train = read_data(train_file_path)
for sent, tag in zip(input_train[:10], result_train[:10]):
    print(sent, tag)