# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:07:58 2019

@author: Big data
"""

import pandas as pd
import numpy as np
import re
regex_pat = re.compile(r"[^a-zA-Z0-9]+", flags=re.IGNORECASE)
df_big = pd.read_csv('Table1.csv')
df_big["regexname"] = df_big["name"].str.replace(regex_pat, '')
year = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
filled = {}
for y in year:
    print(y)
    file = "theater"+str(y)+".csv"
    df_small = pd.read_csv(file)
    
    df_small.loc[:,"regexname"] = df_small.loc[:,"Movie_name"].str.replace(regex_pat, '')
    df_small["year"] = df_small["regexname"].apply(lambda x:x[-4:])
    df_small["regexname"] = df_small["regexname"].apply(lambda x:x[0:-4])
    df_small = df_small[df_small["Theater_num"].notna()]
    
      
    
    for i, s in df_small.iterrows():
        #print(s["regexname"], s["Movie_name"])
        filled[s["regexname"]] = [s["Movie_name"],s["Domestic_box_office"],s["International_box_office"],
                                  s["Worldwide_box_office"],s["Theater_num"],s["year"]]
    
    for I, S in df_big.iterrows():
        
        if S["regexname"] in filled:
            df_big.loc[I, "Movie_name"] = filled[S["regexname"]][0]
            df_big.loc[I, "Domestic_box_office"] = filled[S["regexname"]][1]
            df_big.loc[I, "International_box_office"] = filled[S["regexname"]][2]
            df_big.loc[I, "Worldwide_box_office"] = filled[S["regexname"]][3]
            df_big.loc[I, "Theater_num"] = filled[S["regexname"]][4]
            del filled[S["regexname"]]
#        else:
#            for name in filled.keys():
#                
#                if name.find(s["regexname"]) != -1 and filled[name][5] == s["year"]:
#                    print(name,s["regexname"])
#                    findname = list(filled.keys())[list(filled.keys()).index(name)]
#                    df_big.loc[i, "Movie_name"] = filled[findname][0]
#                    df_big.loc[i, "Domestic_box_office"] = filled[findname][1]
#                    df_big.loc[i, "International_box_office"] = filled[findname][2]
#                    df_big.loc[i, "Worldwide_box_office"] = filled[findname][3]
#                    df_big.loc[i, "Theater_num"] = filled[findname][4]
#                    print(findname,"ok")
                    
                    
        
    if y == 2005:
        df_record =pd.DataFrame(columns=['year','theater_num'])
        df_record=df_record.append(pd.Series([file,df_big["Theater_num"].notna().sum()],index=["file","number"]),ignore_index=True)
        df_record.to_csv('record1.csv')
    else:
        df_record = pd.read_csv('record1.csv',)
        df_record=df_record.append(pd.Series([file,df_big["Theater_num"].notna().sum()],index=["file","number"]),ignore_index=True)
        df_record.to_csv('record1.csv')




#for i in list(filled.keys()):
#    if len(i)<4:
#        print(i,filled[i][0])
#        del filled[i]
#for I, S in df_big.iterrows():
#    
#    if np.isnan(S["Theater_num"]):
#        print(S["regexname"])
#        
#        for name in list(filled.keys()):
#                if name.find(S["regexname"]) != -1 and (len(name)-len(S["regexname"])<10):
#                    print(name,S["regexname"])
#                    findname = list(filled.keys())[list(filled.keys()).index(name)]
#                    df_big.loc[I, "Movie_name"] = filled[findname][0]
#                    df_big.loc[I, "Domestic_box_office"] = filled[findname][1]
#                    df_big.loc[I, "International_box_office"] = filled[findname][2]
#                    df_big.loc[I, "Worldwide_box_office"] = filled[findname][3]
#                    df_big.loc[I, "Theater_num"] = filled[findname][4]
#                    print(findname,"ok")
#                    #del filled[name]
                
        
df_big.to_csv("finalnew.csv",index=False,encoding="utf-8")





