# _*_coding : 
# 开发团队 ：
# 开发人员 ：WanYouhao
# 开发时间 ：2021/3/14 19:56
# 文件名称 ：HomeWork5.PY
# 开发工具 ：PyCharm

import pandas as pd
from wordcloud import WordCloud

# from nltk.tokenize import word_tokenize

#加载Market_Basket_Optimisation

#去除虚词
def remove_stop_words(f):
    stop_word = []
    for stop_word in stop_word:
        f.replace(stop_word,'')
    return f

#  创造词云函数
def create_word_cloud(f):
	# f = remove_stop_words(f)
    text  = ''
    for value in f:
        text = text + '' + value
    wc = WordCloud(max_words=100, width=2000, height=1200)
    wordcloud = wc.generate(text)
    wordcloud.to_file("wordcloud.jpg")

#################################################################

data= pd.read_csv('./Market_Basket_Optimisation.csv',header=None)
# print(data)

#数据存放，transactions
transactions= []
#存储词语的频次，用字典
item_count={}

for i in range(data.shape[0]):
    temp=[]
    for j in range(data.shape[1]):
        item = str(data.values[i,j])
        if item !='nan':
            temp.append(item)
            if item not in item_count:
                item_count[item]=1
            else:
                item_count[item]+=1
    transactions.append(temp)
print(transactions)

#  创造词云函数

def fetchwords(transactions):
    goods = []
    for record in transactions:
        for good in record:
            goods = goods + [good]
    return goods

#生成词云
# all_word = ''.join('%s' %item for item in transactions)
all_goods = fetchwords(transactions)

create_word_cloud(all_goods)

#打印排名前十的商品
print(sorted(item_count.items(),key= lambda x:x[1],reverse=True)[:10])