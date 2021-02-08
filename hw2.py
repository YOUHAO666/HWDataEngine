# _*_coding : 
# 开发团队 ：
# 开发人员 ：WanYouhao
# 开发时间 ：2021/2/7 8:34
# 文件名称 ：Test.PY
# 开发工具 ：PyCharm

import  requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import xlwt





# 得到页面的内容
def get_page_content(request_url):
      print(request_url)
      headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
      html=requests.get(request_url,headers=headers,timeout=10)
      content = html.text
      # print(content)

    # 通过content创建BeautifulSoup对象
      soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
      return soup

# 分析当前页面的投诉信息内容
def analysis(soup):
    # 创建DATAFRAME
    df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    # 找到完整的投诉框
    temp = soup.find("div", class_= "tslb_b")
    #找到所有的tr，即行信息
    tr_list = temp.find_all("tr")
    for tr in tr_list:
        td_list = tr.find_all("td")
        #如果没有td，就是th表头
        if len(td_list)> 0:
            id,brand,car_model,type,desc,problem,datetime,status = \
                td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,\
                td_list[5].text,td_list[6].text,td_list[7].text
            # print(id,brand,car_model,type,desc,problem,datatime,status )
            temp = {}
            temp['id'] = id
            temp['brand'] = brand
            temp['car_model'] = car_model
            temp['type'] = type
            temp['desc'] = desc
            temp['problem'] = problem
            temp['datetime'] = datetime
            temp['status'] = status
            df=df.append(temp,ignore_index=True)
    return df

Statistics_result = pd.DataFrame(columns=['id','brand','car_model','type','desc','problem','datetime','status'])
# 请求URL
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
page_num = 6
for i in range(page_num):
    #拼接构建完整的网页URL
    request_url = base_url + str(i+1) + ".shtml"
    #解析
    soup = get_page_content(request_url)
    #得到dataframe
    df=analysis(soup)
    Statistics_result=Statistics_result.append(df)
    time.sleep(1)


print(Statistics_result)
Statistics_result.to_excel('car_complain_Wan.xlsx',index=False)


# #输出第一个 title 标签
# print(soup.title)
# #输出第一个 title 标签的标签名称
# print(soup.title.name)
# #输出第一个 title 标签的包含内容
# print(soup.title.string)




