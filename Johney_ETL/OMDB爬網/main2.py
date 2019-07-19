from OMDB_useApiKey import OMDB
import datetime
import time
from urllib.request import urlopen, urlretrieve
import json


def main():
    cont = 1

    with open("movie2011.csv", "r", encoding="utf-8") as f:
        a = f.read().splitlines()
        start_time = datetime.datetime.now()
        failcont = 1
        resultlist = []
        cont = 1
        for i in a:
            try:
                url = "http://www.omdbapi.com/?i=" +i+ "&apikey=b7bc0039"
                response = urlopen(url)
                info = json.load(response)
                json_tmp = json.dumps(info)
                resultlist.append(json_tmp)
                print("Now is number "+ str(cont) +" Movie")
                cont += 1
                spantime = datetime.datetime.now() - start_time
                print(spantime)
            except Exception as e :
                print(a.index(i))
                print("urlerror")
                with open("faillog.txt", "a", encoding="utf-8") as faillog:
                    faillog.write(i)
                    e = str(e)
                    faillog.write(e)
                    faillog.write("\n")

                spantime = datetime.datetime.now() - start_time
                continue
        with open("MovieInfo.json","a",encoding="utf-8") as re:
            re.writelines(resultlist)
            re.close()
        spantime = datetime.datetime.now()-start_time
        print(spantime)

if __name__=="__main__":
    main()
