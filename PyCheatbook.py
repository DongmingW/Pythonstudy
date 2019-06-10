#SQL Server数据库操作
import pandas as pd
import pymssql
from sqlalchemy import create_engine
server = '域名或IP地址'
user = '用户名'
password = '密码'
conn = 'mssql+pymssql://{}:{}@{}:{}/{}?charset=utf8'.format(user, password, server, '端口', '库名称')
engine = create_engine(conn)
SQLcmd = "SQL语句"
result = pd.read_sql(sql = SQLcmd, con = engine)
pd.io.sql.to_sql(dfgc4g2, name = 'L_all', con = engine, if_exists = 'replace', index = False)

#PD显示格式设置
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.6f' % x)

#PD Excel文件读取并设置列格式
g2 = pd.read_excel('./2.xls',sheet_name='Sheet1',dtype={'BCCH':str,'挂高':str})
g4 = pd.read_excel('./4.xlsx',sheet_name='LTE Project Parameters',skiprows=2,dtype={'Downlink Center Frequency':str,'ANTHeight':str})

#PD 数值列合并
g2['NCCBCC'] = g2['NCC'].map(str) + g2['BCC'].map(str)
g2['cellname'] = g2['bts_name'].map(str) + '方位角' + g2['方位角'].map(str) + '下倾角' + g2['下倾角'].map(str) + '挂高' + g2['挂高'].map(str)

#PD 筛选列并存放到另一个df
gc2 = g2[['Gen','MCC','MNC','CI','LAC','BTS','NCCBCC','经度','纬度','cellname','BCCH']]

#PD 列批量更名
gc2.columns = ['Gen','MCC','MNC','CellID','xAC','NodeBID','PCI','Lon','Lat','Cellname','Freq']

#PD 竖向合并df
netm = pd.concat([gc2,gc3,gc4],ignore_index=True,axis=0)

#根据时间修改文件名
import time
time = time.strftime("%Y%m%d")
outputfilename = './Netmonster%s.csv' % time

#PD csv文件写入
netm.to_csv(outputfilename,index=0,header=0,encoding='utf-8')

#替换文件中特定字符
f = open(outputfilename,'r',encoding='utf-8')
f_new = open(outputfilename2,'w',encoding='utf-8')
for line in f:
    # 进行判断
    if "," in line:
        line = line.replace(',',';')
    # 如果不符合就正常的将文件中的内容读取并且输出到新文件中
    f_new.write(line)
f.close()
f_new.close()

#Json解析，可以嵌套解析，下面代码就是解析的r->data->list
from pandas.io.json import json_normalize
j = pd.DataFrame(json.loads(r.data.decode('utf-8'))['data']['list'])

#PD多条件筛选并赋值
df.loc[(df['BBB'] > 25) | (df['CCC'] >= 75), 'AAA'] = 0.1

#SQL的Pandas实现
UPDATE tips
SET tip = tip*2
WHERE tip < 2;
In [38]: tips.loc[tips['tip'] < 2, 'tip'] *= 2
