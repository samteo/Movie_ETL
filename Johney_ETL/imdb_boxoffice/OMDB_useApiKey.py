from urllib.request import urlopen, urlretrieve
import json

def OMDB (IMDB_number ="tt0446029", apikey= "b7bc0039"):

    #f = open( filename, "a", encoding="utf-8")     #開啟檔案
    list = []
#        IMDB_number = "tt"+str(number).zfill(7)     #準備IMDB編號
    url = "http://www.omdbapi.com/?i=" + IMDB_number + "&apikey=" + apikey    # apikey= b7bc0039(100,000)   5ab10f1c(免費)
    response = urlopen(url)
    info = json.load(response)
    #json.dumps(info)
    #print(info)
    #list.append(json.dumps(info))
    return info

