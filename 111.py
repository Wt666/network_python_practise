from importlib.util import MAGIC_NUMBER
import numbers
from operator import index
from tokenize import Number
import pandas as pd
import numpy as np
import time
# Path='/Users/wt/Desktop/network\ python\ \ practise/MCCMNC数据 源-220323.xlsx '
sourceDf=pd.read_excel('MCCMNC数据源-220323.xlsx')
# print(sourceDF)

dictCCNDC={}
zippedCCNDC=zip(sourceDf['CC'].apply(str),sourceDf['NDC'].apply(str))
dict_value=list(set(list(zippedCCNDC)))
dict_key=[''.join(i) for i in dict_value]
dict_data=dict(zip(dict_key,dict_value))

# print(dict_data['29950'])
def find_MCCMNC(phone_input):
    data = {
        'number': phone_input,
        'Operator_Name':None,
        'E212_MCC':None,
        'E212_MNC':None
    }
    phone_input=phone_input
    result=[j for i,j in dict_data.items() if phone_input[0:len(i)]==i]

    result_int=[tuple([int(j) for j in list(i)]) for i in result]
    Fin_result=sourceDf[sourceDf[['CC','NDC']].apply(tuple,axis=1).isin(result_int)]
# ON=Fin_result['Operator_Name']
# MCC=Fin_result['E212_MCC']
# MCN=Fin_result['E212_MNC']
    # data=Fin_result[['Operator_Name','E212_MCC','E212_MNC']]
    data['Operator_Name']=data['Operator_Name']
    data['E212_MCC']=data['E212_MCC']
    data['E212_MNC']=data['E212_MNC']
    # dict_result={'index':data.index,'result':data.values}
    # df_result=pd.DataFrame(dict_result)
    return data   
# print(find_MCCMNC('8613460624959'))
def batch_dig(tels, printWithoutSave=False, result_path=f'result@MNC@{time.strftime("%Y%m%d%H%M%S", time.localtime())}.xlsx'):
    result_dict_columns = ['number', 'Operator_Name','E212_MCC','E212_MNC']
    result_df = pd.DataFrame(columns=result_dict_columns)  # empty dataframe
    for phone_input in tels:
        if printWithoutSave:
            print(find_MCCMNC(phone_input))
        else:
            result_unit_df = pd.DataFrame(find_MCCMNC(phone_input), index=[0])
            result_df = result_df.append(result_unit_df)
    if not printWithoutSave:
        result_df.to_excel(result_path, index=False)
        print(f'===== to_excel, finish, {result_path} ==== \n')
    else:
        print('batch_dig, finish.')

if __name__ == "__main__":
    print('program begin...')
    # tels = ['85263300013', '85262107007']
    tels = pd.read_excel(r'tels.xlsx', dtype=str)['tel']
    # print(tels)
    batch_dig(tels, printWithoutSave=False)
    print('program done.')              


# print(find_MCCMNC('8613460624959'))
# phone_input='8613460624959'
# result=[j for i,j in dict_data.items() if phone_input[0:len(i)]==i]

# result_int=[tuple([int(j) for j in list(i)]) for i in result]
# Fin_result=sourceDf[sourceDf[['CC','NDC']].apply(tuple,axis=1).isin(result_int)]
# # ON=Fin_result['Operator_Name']
# # MCC=Fin_result['E212_MCC']
# # MCN=Fin_result['E212_MNC']
# data=Fin_result[['Operator_Name','E212_MCC','E212_MNC']].apply(list,axis=1)
# print(data)
# index=[1]
# # a=pd.DataFrame(data=data,index=index)
# df=pd.DataFrame(data=data,index=index)
# print(df)
# print(a)