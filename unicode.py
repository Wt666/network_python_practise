import xlrd
import pandas as pd
data=pd.read_excel('/Users/wt/Downloads/参考.xlsx')
# worksheet=xlrd.open_workbook('/Users/wt/Downloads/参考.xlsx','rb')
# sheet_names=worksheet.sheet_names()
# print(sheet_names)
# print(data.head())
# a='****** - Huawei-Bestätigungscode. Nutzen Sie diesen, um eine E-Mail-Adresse mit Ihrer HUAWEI ID +** ********** zu verknüpfen. Geben Sie den Code aus Sicherheitsgründen nicht an andere weiter.'
# print(a.encode('unicode-escape').decode())
# for i in list(a):
#     print(i.encode('unicode-escape').decode())
'''
# print('max i='+max(i.encode('unicode-escape').decode()))
content=data[']
print(data['SMS Content'])
ls=list(content)
result=[]
for i in ls:
    for k in list(i):
        result.append(ord(k))
print(max(result))
print(chr(max(result)))
'''

def get_max(ctx):
    char_max = max(list(map(lambda x: ord(x), list(ctx))))
    return char_max

print(data['SMS Content'][0])
print(get_max(data['SMS Content'][0]))

data['char_max'] = data['SMS Content'].apply(get_max)
data['char'] = data['char_max'].apply(chr)
data.to_excel('b.xlsx')




#     for k in i:
#         data['unix'] = k.encode('unicode-escape').decode()
    # data['unix'] = ord('i')
# data['unix'] = data['SMS Content'].apply(str.encode('unicode-escape').decode())

# data['unix'] = data['SMS Content'].apply(str.upper)
# data.to_excel('b.xlsx')

    # for k in i:
        # un=k.encode('unicode-escape').decode()

# writer = pd.ExcelWriter('path_to_file.xlsx')
# un.to_excel(writer)
# writer.save()