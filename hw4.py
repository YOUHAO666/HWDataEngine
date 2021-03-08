# _*_coding : 
# 开发团队 ：
# 开发人员 ：WanYouhao
# 开发时间 ：2021/3/7 12:34
# 文件名称 ：Test.PY
# 开发工具 ：PyCharm


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from efficient_apriori import apriori

#1：数据加载
# header=None，不将第一行作为head
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)

print(dataset)


# 将数据存放到transactions中
transactions = []
# 按行进行遍历
for i in range(0, dataset.shape[0]):
    temp = []
    #按列进行遍历
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i, j]) != 'nan':
           temp.append(str(dataset.values[i, j]))
    transactions.append(temp)
#print(transactions)
# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(transactions, min_support=0.03,  min_confidence=0.3)
print("频繁项集：", itemsets)
print("关联规则：", rules)


