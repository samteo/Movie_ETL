# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:19:27 2019

@author: Big data
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests
big_list=[]
url= "https://www.the-numbers.com/movies/production-companies/"
response = requests.get(url)
html = BeautifulSoup(response.text)
content = html.find("tbody")
content1 = content.find_all("tr")
for i in content1:
    single = []
    a = i.find_all("td")
    for o in a:
        single.append(o.text)
    big_list.append(single)


df = pd.DataFrame(big_list,columns = ["company",'movie_num','domestic',"international"])
df.to_csv('company_detail.csv',index=False)