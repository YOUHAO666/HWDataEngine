# _*_coding : 
# 开发团队 ：
# 开发人员 ：WanYouhao
# 开发时间 ：2021/1/31 11:02
# 文件名称 ：HW3.PY
# 开发工具 ：PyCharm

import pandas as pd

df = pd.DataFrame
# 读取csv文件
df = pd.read_csv('car_complain.csv')
print(df)

# 写csv文件,index=False，表明不保存index
# pd.to_csv('car_complain.csv', index=False)

df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
# print(df)


# 数据清洗
def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return  x
df['brand']=df['brand'].apply(f)
df2 = df.groupby(['brand'])['id'].agg(['count'])
# print(df2)

tags = df.columns[7:]
# print(tags)

# 问题总数统计
df3 = df.groupby(['brand'])[tags].agg(['sum'])
print(df3)

# df3 = df2.merge(df3, left_index = True, right_index = True,how = 'left')
#
#
# df3.reset_index(inplace=True)
# print(df3)
# df3.to_csv('result1.csv')

# 按品牌投诉量进行排序
df4=df3.sort_values('count',ascending=False)
print(df4)

# 按指定的问题进行排序
query = ('A11','sum')
df5=df3.sort_values(query,ascending=False)