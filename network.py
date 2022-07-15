# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# # 文件名：server.py
#
# import socket  # 导入 socket 模块
#
# s = socket.socket()  # 创建 socket 对象
# host = socket.gethostname()  # 获取本地主机名
# port = 12345  # 设置端口
# s.bind((host, port))  # 绑定端口
#
# s.listen(5)  # 等待客户端连接
# while True:
#     c, addr = s.accept()  # 建立客户端连接
#     print('连接地址：', addr)
#     c.send('欢迎访问菜鸟教程！')
#     c.close()  # 关闭连接
#
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# # 文件名：client.py
#
# import socket  # 导入 socket 模块
#
# s = socket.socket()  # 创建 socket 对象
# host = socket.gethostname()  # 获取本地主机名
# port = 12345  # 设置端口号
#
# s.connect((host, port))
# print(s.recv(1024))
# s.close()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import StringIO

str_survey = '''Pattern Subject   Q1   Q2   Q3   Q4   Q5
1.0      1.5      4.5  4.0  1.0  1.5  1.0
3.0      1.5      4.0  4.0  4.0  4.0  5.0
7.0      1.5      5.0  4.0  1.5  1.5  1.5'''
df_survey = pd.read_csv(StringIO(str_survey), delim_whitespace=True)
pattern_palette = {1: 'crimson', 3: 'limegreen', 7: 'dodgerblue'}
df_survey_melted = df_survey.melt(id_vars=['Pattern', 'Subject'],
                                  var_name='Question', value_name='Mean Score')
ax = sns.pointplot(data=df_survey_melted, x='Question', y='Mean Score', join=False,
                   hue='Pattern', palette=pattern_palette)
plt.show()