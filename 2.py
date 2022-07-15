import os

# def num(number):
number = list(input(int()))
number.reverse()
new_num = '.'.join(number)
# print(a)

s='dig @10.91.201.15 -p 16053 '+new_num+'.e164.arpa naptr'

# print(s)
res = os.popen(s)
# res_l = list(res)
# for i in res.readlines():
    # print(i)
rt=res.readlines()
rst = ''.join(rt)
# print(rst)
tel = rst[rst.find('!tel')+1: rst.find(';rn')].split()
print(tel[0]+tel[-1])
rst = rst[rst.find('rn'): rst.find(';spid')].split()
print(rst[0]+rst[-1])
# print(a)
# print(type(res))
#     right=i[i.find('rn'):i.find('spid')]
#     left=i[i.find('5263300013'):i.find('spid')]
#     print(right)
#     print(left)
# print(str(right)+str(left))
# # print(type(res))
# print(res)
# print(right)
# print(type(i))
# print('End test')
# print(res)

# with open('1.txt', 'r') as res:
#     rt = res.readlines()
#     rst = ''.join(rt)
#     print(rst)
#     tel = rst[rst.find('!tel')+1: rst.find(';rn')].split()
#     print(tel[0]+tel[-1])
#     rst = rst[rst.find('rn'): rst.find(';spid')].split()
#     print(rst[0]+rst[-1])