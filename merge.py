import pandas as pd
data1=pd.read_excel('/Users/wt/Desktop/EBST06.xlsx')
data2=pd.read_excel('/Users/wt/Desktop/202106_EBEST.xlsx')
dataMerge=pd.merge(data1,data2,left_on='SendTime',right_on='SUBMISSION_TIME',how='inner')
dataMerge.to_excel('/Users/wt/Desktop/EBSTmerge06.xlsx')