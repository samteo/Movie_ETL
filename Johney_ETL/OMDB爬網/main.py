from OMDB_useApiKey import OMDB
import datetime
import json
import time
def main():
    cont = 1
    with open("movie2006.csv", "r", encoding="utf-8") as f:
        a = f.read().splitlines()
        start_time = datetime.datetime.now()
        failcont = 1
        MovieInfoList = []
        for i in a:
            try:
                movie = OMDB(i)
                tmp ='BoxOffice": "N/A'
                if tmp not in movie and 'Response": "False' not in movie:
                    MovieInfoList.append(movie)
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

        with open("movieinfo2006","w",encoding="utf-8") as final:
            for i in MovieInfoList:
                if i == MovieInfoList[0]:
                    final.write("[")
                else:
                    final.write(",\n")
                final.write(str(i))
#                if i == MovieInfoList[-1]:
#                    final.write("]")

            #print(MovieInfoList)


        spantime = datetime.datetime.now()-start_time
        with open("faillog.txt", "a", encoding="utf-8") as faillog:
            faillog.write(str(spantime))
            faillog.write(str(f))
            faillog.write("\n")

if __name__=="__main__":
    main()
