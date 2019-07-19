from OMDB_useApiKey import OMDB
import datetime
import csv
import pandas as pd
import time
def main():
    cont = 1
    start_time = datetime.datetime.now()
    ListFileName = ["imdb2005.csv", "imdb2006.csv", "imdb2007.csv", "imdb2008.csv", "imdb2009.csv"]
    for i in ListFileName:
        with open( i , "r", encoding="utf-8") as data:
            rows = csv.reader(data)
            # MovieInfoList = []

            appendlist = ["release_date_USA", "Genre", "Director", "Writer", "Actors", "Language", "Awards", "Country", "Production", "imdbVotes", "IMDBscore", "TomatoesScore", "Metascore"]
            #新增的欄位
            n = 0
            with open("score" + i, "w", encoding="utf-8", newline='') as result:
                for row in rows:
                    if row[0] == "id":
                        newfirstRow = row + appendlist
                        print(newfirstRow)
                        writer = csv.writer(result)
                        writer.writerow(newfirstRow)
                    else:
                        i = row[0]
                        movie = OMDB(i)

                        n += 1
                        print(n)
                        row[1] = movie.get("Title")
                        row.append(movie.get("Released"))
                        row.append(movie.get("Genre"))
                        row.append(movie.get("Director"))
                        row.append(movie.get("Writer"))
                        row.append(movie.get("Actors"))
                        row.append(movie.get("Language"))
                        row.append(movie.get("Awards"))
                        row.append(movie.get("Country"))
                        row.append(movie.get("Production"))
                        row.append(movie.get("imdbVotes"))

                        tmplist_score = movie.get("Ratings")
    #取出meta分數
                        scorelist =["", "", ""]
                        for i in range(len(tmplist_score)):
                            if tmplist_score[i].get("Source") == "Internet Movie Database":
                                a, b = tmplist_score[i].get("Value").split("/")
                                scorelist[0] = round(float(a) / float(b), 2)
                            elif tmplist_score[i].get("Source") == "Rotten Tomatoes":
                                a = tmplist_score[i].get("Value").replace("%", "")
                                a = float(a) / 100
                                scorelist[1] = a
                            elif tmplist_score[i].get("Source") == "Metacritic":
                                a, b = tmplist_score[i].get("Value").split("/")
                                scorelist[2] = round(float(a) / float(b), 2)
                        print(row)
                        row = row + scorelist
                        writer = csv.writer(result)
                        writer.writerow(row)
if __name__=="__main__":
    main()
