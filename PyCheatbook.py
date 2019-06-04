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
