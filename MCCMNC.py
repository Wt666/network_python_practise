from importlib.util import MAGIC_NUMBER
from operator import index
from cv2 import pencilSketch
import pandas as pd
import numpy as np
# Path='/Users/wt/Desktop/network\ python\ \ practise/MCCMNC数据 源-220323.xlsx '
sourceDf=pd.read_excel('MCCMNC数据源-220323.xlsx')
# print(sourceDF)

dictCCNDC={}
zippedCCNDC=zip(sourceDf['CC'].apply(str),sourceDf['NDC'].apply(str))
dict_value=list(set(list(zippedCCNDC)))
dict_key=[''.join(i) for i in dict_value]
dict_data=dict(zip(dict_key,dict_value))

# print(dict_data['29950'])

phone_input='88249'
result=[j for i,j in dict_data.items() if phone_input[0:len(i)]==i]

result_int=[tuple([int(j) for j in list(i)]) for i in result]
Fin_result=sourceDf[sourceDf[['CC','NDC']].apply(tuple,axis=1).isin(result_int)]
# ON=Fin_result['Operator_Name']
# MCC=Fin_result['E212_MCC']
# MCN=Fin_result['E212_MNC']
data=Fin_result[['Operator_Name','E212_MCC','E212_MNC']]
# data=Fin_result[['Operator_Name','E212_MCC','E212_MNC']].apply(list,axis=1)
print(data)
# print(type(data))
# dict_result={'index':data.index,'result':data.values[0]}
# df_result=pd.DataFrame(dict_result)
# print(df_result)
# print(data.to_excel())