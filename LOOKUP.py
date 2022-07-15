import pandas as pd
import numpy as np
import time
import os
PATH=r''
# load data
sourceDf=pd.read_excel('MCCMNC数据源-220323.xlsx')
tels = pd.read_excel('tels.xlsx', dtype=str)['tel']
# setting
l_columnofSearch=['Operator_Name','E212_MCC','E212_MNC','CC','NDC']
l_clueofColumn1='CC'
l_clueofColumn2='NDC'
l_rename_dict={'Operator_Name':'Operator Name','E212_MCC':'E212 MCC','E212_MNC':'E212 MNC','CC':'CC','NDC':'NDC'}
printWithoutSave=False
l_custom_exportName='MCCMNC'

# load group data
# output:GroupofMCCMNC{'883130': {'CC': 883, 'NDC': 130},...}
def build_GroupofCCNDC(dataSource,clueofColumn1,clueofColumn2):
    GroupofCCNDC={}
    dict_value=list(set(list(zip(dataSource[clueofColumn1].apply(str),dataSource[clueofColumn2].apply(str)))))
    for i in dict_value:
        GroupofCCNDC[''.join(i)]=dict(zip([clueofColumn1,clueofColumn2],list([int(j) for j in i])))
    return GroupofCCNDC


# dataSource df,dataSearch df,columnofSearch list,clueofColumn1 str,clueofColumn2 str,GroupofMCCMNC dict
def find_MCCMNC(dataSource,dataSearch,columnofSearch,clueofColumn1,clueofColumn2,GroupofMCCMNC):
    dfCCNDC=pd.DataFrame(columns=['tel',clueofColumn1,clueofColumn2])
    for phone in dataSearch:
        dictMCCMNC=[j for i,j in GroupofMCCMNC.items() if phone[0:len(i)]==i]
#        this loop:should do just once
        for temp in dictMCCMNC:
            temp['tel']=phone
            dfCCNDC=dfCCNDC.append(temp,ignore_index=True)
    return pd.merge(dfCCNDC,dataSource,on=[clueofColumn1,clueofColumn2]).loc[:,columnofSearch+['tel']]

# rename_dict{'Operator_Name':'Operator Name','E212_MCC':'E212 MCC','E212_MNC':'E212 MNC','CC':'CC','NDC':'NDC'}
# suggest printWithoutSave put out of function WritetoExcel:
#    do WritetoExcel if !printWithoutSave
def WritetoExcel(export_info,export_folder,custom_exportName=None,rename_dict=None):
    export_info.columns=[rename_dict[i] if i in rename_dict.keys() else i 
    for i in list(export_info.columns)] if rename_dict!=None else export_info.columns
    export_path=export_folder+(r'result@MNC@{time.strftime("%Y%m%d%H%M%S", time.localtime())}.xlsx' 
    if custom_exportName==None else custom_exportName+'.xlsx')  
    try:
        if not os.path.exists(export_path):
            export_info.to_excel(export_path, index=False)
        else:
            with pd.ExcelWriter(export_path,mode='w') as writer:
                export_info.to_excel(writer,index=False,sheet_name=time.strftime("%Y%m%d%H%M%S",time.localtime()))
                # writer.save()
                # writer.close()
    except:
        print(f'===== to_excel, failed, please check it==== \n')
    else:
        print(f'===== to_excel, finished, {export_path} ==== \n')
    return

def searchMCCMNC(dataSource,dataSearch,columnofSearch,clueofColumn1,clueofColumn2,export_folder,printWithoutSave=False,rename_dict=None,custom_exportName=None):
    if printWithoutSave:
        print(find_MCCMNC(dataSource,dataSearch,columnofSearch,clueofColumn1,clueofColumn2,
                            build_GroupofCCNDC(dataSource,clueofColumn1,clueofColumn2)))
    else:
        WritetoExcel(find_MCCMNC(dataSource,dataSearch,columnofSearch,clueofColumn1,clueofColumn2,
                            build_GroupofCCNDC(dataSource,clueofColumn1,clueofColumn2)),export_folder,custom_exportName,rename_dict)
    return
searchMCCMNC(sourceDf,tels,l_columnofSearch,l_clueofColumn1,l_clueofColumn2,PATH,printWithoutSave=printWithoutSave,rename_dict=l_rename_dict,custom_exportName=l_custom_exportName)