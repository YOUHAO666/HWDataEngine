# _*_coding : 
# 开发团队 ：
# 开发人员 ：WanYouhao
# 开发时间 ：2021/1/31 8:22
# 文件名称 ：HW2.PY
# 开发工具 ：PyCharm

import numpy as np


import numpy as np
from pandas import Series, DataFrame

data = {'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])

print(df2)

print(df2.describe())

df3 = df2
df3['总成绩'] = df2.iloc[:,1:4].sum(axis=1)
print(df3)

# tags = df2.columns[0:3]
# # print(tags)
#
# df3 = df2.groupby(['总成绩'])[tags].agg(['sum'])
# print(df3)

# # 新建一列作为总成绩
# df2.insert(3,'总成绩',[0,0,0,0,0],True)
#
# # df2 = df2.insert(columns=['总成绩'])
#
# # print(df2)
#
# df2['总成绩'] = df2['语文'] + df2['数学'] + df2['英语']
# #按总成绩排序
# df4=df2.sort_values('总成绩',ascending=False)
# print(df4)

# result = df2.groupby('总成绩').agg([np.sum])
# print(result)
