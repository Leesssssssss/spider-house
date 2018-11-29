#!/usr/bin/env python   
# _*_ coding:utf-8 _*_  
import requests
import sys
import chardet
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import json 

# 存储数据的数组
data = []

def getData(url):
  try:
    html = requests.get(url).text.decode('utf-8').encode('mbcs')    # 根据url获取页面html并解决编码问题
    infos = BeautifulSoup(html, 'lxml')    # 解析html
    titles = infos.select("h3[class='tit'] a")  # 房源名称
    locations = infos.select("p[class='location'] span[class='community'] a")   # 房源位置
    params = infos.select("p[class=param]")   # 房源楼层、年代、朝向等信息
    areas = infos.select("div[class='i-infor'] i")    # 房源面积
    prices = infos.select("div[class='i-infor'] span[class='price'] b")   # 房源价格

    # 循环获取相应标签中需要的信息
    for (title,location,param,area,price) in zip(titles,locations,params,areas,prices):
      house_info = {
        'house_title': title.get('title'),
        'house_location': location.get('title'),
        'house_floor': param.contents[0].strip(),
        'house_year': param.contents[2].strip(),
        'house_toward': param.contents[4].strip(),
        'house_area': area.string,
        'house_price': price.contents[1].string.strip() + price.contents[2].string.strip()
      }
      data.append(house_info)
  except:
    print('数据获取失败！')
  return data     # 将获取到的信息返回给数组

if __name__ == "__main__":
  # 根据页数循环获取，可自行更改所需要的数据量
  for i in range(1,10):
    url = 'http://dl.goufang.com/2s/p{}'.format(i)
    getData(url)
    # print('{} page is ok!'.format(i))

print(json.dumps(data).decode("unicode-escape"))   # 最后的数据中文转码









