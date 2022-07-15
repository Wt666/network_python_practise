import os
import time
import pandas as pd
import numpy as np

def unit_dig(tel):
    result_unit_dict = {
        'tel': tel,
        'spid':None
    }
    format_num = '.'.join(reversed(tel))
    dig_command = 'dig @10.91.201.15 -p 16053 ' + format_num + '.e164.arpa naptr'
    print(dig_command)
    rst = ''.join(os.popen(dig_command).readlines())
    rst = rst[rst.find('spid'): rst.find(';spname:Spri')].split()
    result_unit_dict['spid'] = rst[0]+rst[-1]
    # result_unit_dict['spid'] = rst[0][3:] + rst[-1]
    return result_unit_dict

def batch_dig(tels, printWithoutSave=False, result_path=f'result@ENUM@{time.strftime("%Y%m%d%H%M%S", time.localtime())}.xlsx'):
    result_dict_columns = ['tel', 'spid']
    result_df = pd.DataFrame(columns=result_dict_columns)  # empty dataframe
    for tel in tels:
        if printWithoutSave:
            print(unit_dig(tel))
        else:
            result_unit_df = pd.DataFrame(unit_dig(tel), index=[0])
            result_df = result_df.append(result_unit_df)
    if not printWithoutSave:
        result_df.to_excel(result_path, index=False)
        print(f'===== to_excel, finish, {result_path} ==== \n')
    else:
        print('batch_dig, finish.')

if __name__ == "__main__":
    print('program begin...')
    # tels = ['85263300013', '85262107007']
    tels = pd.read_excel(r'tels.xlsx', dtype=str)
    tels = tels['tel']
    batch_dig(tels, printWithoutSave=False)
    print('program done.')

