# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:55:45 2019

@author: Big data
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:45:50 2019

@author: Big data
"""
#movie = {"Title":"Spider-Man: Homecoming","Year":"2017","Rated":"PG-13","Released":"07 Jul 2017",
#         "Runtime":"133 min","Genre":"Action, Adventure, Sci-Fi","Director":"Jon Watts","Writer":"Jonathan Goldstein (screenplay by), John Francis Daley (screenplay by), Jon Watts (screenplay by), Christopher Ford (screenplay by), Chris McKenna (screenplay by), Erik Sommers (screenplay by), Jonathan Goldstein (screen story by), John Francis Daley (screen story by), Stan Lee (based on the Marvel comic book by), Steve Ditko (based on the Marvel comic book by), Joe Simon (Captain America created by), Jack Kirby (Captain America created by)","Actors":"Tom Holland, Michael Keaton, Robert Downey Jr., Marisa Tomei","Plot":"Peter Parker balances his life as an ordinary high school student in Queens with his superhero alter-ego Spider-Man, and finds himself on the trail of a new menace prowling the skies of New York City.","Language":"English, Spanish","Country":"USA","Awards":"4 wins & 9 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.5/10"},{"Source":"Rotten Tomatoes","Value":"92%"},{"Source":"Metacritic","Value":"73/100"}],"Metascore":"73","imdbRating":"7.5","imdbVotes":"428,373","imdbID":"tt2250912","Type":"movie","DVD":"17 Oct 2017","BoxOffice":"$334,166,825","Production":"Sony Pictures",
#         "Website":"http://www.sonypictures.com/movies/spidermanhomecoming/","Response":"True"}
movie = m

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
name = movie["Title"].replace(":","").replace(" ","-")
result=[0,np.NaN,np.NaN,np.NaN,np.NaN]
dicttheater = {}
list_theater= []
notheater=[]
url= "https://www.the-numbers.com/movie/"+str(name)
response = requests.get(url)
html = BeautifulSoup(response.text)
moviename =html.find("h1") 
result[0]=moviename.text
content = html.find("table",id="movie_finances")
content1 = content.find_all("tr")
try:
   Dos = content1[1].find("td")
   if "Domestic Box Office" in Dos.text:
       result[1]=content1[1].find("td",class_="data").text
except:
   pass
try:
    Int = content1[2].find("td")
    if "International Box Office" in Int.text:
        result[2]=content1[2].find("td",class_="data").text
except:
    pass
try:
    Wor = content1[3].find("td")
    if "Worldwide Box Office" in Wor.text:
        result[3]=content1[3].find("td",class_="data").text
except:
    pass  
try:
    budget = html.find("div",id="summary")
    budget1 = budget.find_all("tr")
    for i in budget1:
        if "Production\xa0Budget" in i.text:
            budget2 = i.find_all("td")[1]
            budget2 = budget2.text
            result[4]=budget2
            print('ok')
except:
    pass

try:
    theater = html.find("div",id="box_office_chart")
    list_td = theater.find_all("tr")[1:]
    for i in list_td:
        theater_num=i.find_all('td')
        list_theater.append(theater_num[4].text)
    list_theater = [a.replace(',','') for a in list_theater]
    list_theater = [int(a) for a in list_theater if a.isdigit()]
    list_theater = max(list_theater)
    #print(list_theater)
    result.append(list_theater)
    #print(result)
except:
    if result[1]!= "$0":
        notheater.append(moviename.text)



    
df=pd.DataFrame(list_theater,columns=["Movie_name","Domestic_box_office",
                                    "International_box_office","Worldwide_box_office","Theater_num"])
df["Theater_num"]=np.where(df["Domestic_box_office"]=="$0",np.nan,df["Theater_num"])
df.to_csv("testtest.csv",index=False,encoding="utf-8")
df1=pd.DataFrame(notheater)
df1.to_csv("notesttest.csv",index=False,encoding="utf-8")