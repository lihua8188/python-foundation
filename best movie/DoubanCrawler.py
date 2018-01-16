import expanddouban
import time
import csv
import codecs
import pandas as pd

from bs4 import BeautifulSoup

BaseUrl = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
myCategory = ["战争","科幻","剧情"]

"""
Task 1:
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
    url = BaseUrl + ",{},{}".format(category, location)
    return url

"""
Task 3:
set movie class
"""
def Movie(name, rate, location, category, info_link, cover_link):
    #creat movie info as list
    movie = []
    movie = [name, rate, location, category, info_link, cover_link]
    return movie

"""
Task 4:
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
    #return all movies info in the category
    MoviesInfo = []
    url = getMovieUrl(category, location)
    html = expanddouban.getHtml(url, True) #get whole page of the url
    soup = BeautifulSoup(html, "html.parser")
    MovieListDiv = soup.find(class_="list-wp").find_all(class_="item") #find the main div
    for item in MovieListDiv:
        name = ""
        name = item.find(class_="title").string
        rate = item.find(class_="rate").string
        info_link = item.get("href")
        cover_link = item.img.get("src")
        MoviesInfo.append(Movie(name, rate, location, category, info_link, cover_link))
    return MoviesInfo


"""
get location tag list in movie list page.
"""
def getLocationTags(url):
    #return a location tag list from the movie page
    ListLocation = []
    ListPageHtml = expanddouban.getHtml(url)
    soup = BeautifulSoup(ListPageHtml, "html.parser")
    LocationDiv = soup.find(string="全部地区")
    for name in LocationDiv.parent.parent.next_siblings:
        ListLocation.append(name.string)
    return ListLocation

"""
Task 5:
crawl Douban movie page and read movies info to movies.csv.
"""
MovieList = [] #creat total movie list
LocationList = getLocationTags(BaseUrl) #get all the location tag in movie page
for category in myCategory: #search for category with all location
    for location in LocationList:
        MovieList += getMovies(category,location)
        time.sleep(2)

# write the search result into csv
with codecs.open("movies.csv", "w", "utf_8_sig") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(MovieList)

"""
Task 6:
movie data analysis and write result to output.txt.
"""
f = open("output.txt", "w")
#get raw data from movies.csv as dataframe data
data = pd.read_csv("movies.csv",header=None, names=["name","score","location","category","link","img"])
for category in myCategory:
    # get summary by location for each category
    group = data.groupby(["category"]).get_group(category).groupby(["location",]).count().filter(items=["location","name"]).sort_values(by="name",ascending=False)
    totalNum = group["name"].sum() #total movies number in this category
    n = 1
    f.write("{} category top 3 locations are:\n".format(category))

    for i, row in group.iterrows():
        if n<=3:
            f.write("{}. {}: {}\n".format(n, i, format(row[0]/totalNum,".2%")))
            n +=1
        else:
            f.write("\n")
            break

f.close()
