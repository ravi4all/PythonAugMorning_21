import bs4
import urllib.request as url

def search(movieName):
    # movieName = input("Enter movie name : ")
    movieName = movieName.replace(" ", "+")
    response = url.urlopen("https://www.imdb.com/find?q={}&ref_=nv_sr_sm".format(movieName))
    page = bs4.BeautifulSoup(response, 'lxml')

    td = page.find("td", {"class": "result_text"})
    a_tag = td.find('a')
    href = a_tag['href']
    newUrl = "https://www.imdb.com" + href

    response2 = url.urlopen(newUrl)

    page2 = bs4.BeautifulSoup(response2, 'lxml')

    title = page2.find('h1')
    # print(title.text)
    rating = page2.find("span", {"class": "AggregateRatingButton__RatingScore-sc-1ll29m0-1"})
    # print(rating.text)
    summary = page2.find("p", class_="GenresAndPlot__Plot-cum89p-6 bUyrda")
    summary_span = summary.find("span")
    # print(summary_span.text)
    return title.text, summary_span.text, rating.text
