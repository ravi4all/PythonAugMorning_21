import urllib.request as url
import bs4

# response = url.urlopen("https://www.jansatta.com/")
response = url.urlopen("https://www.jansatta.com/khel/")
page = bs4.BeautifulSoup(response, 'html.parser')

# titles = page.find_all("h3", attrs={"class":"entry-title"})
titles = page.find_all("div", attrs={"class":"entry-title"})

for i in range(10):
    print(titles[i].text)
    print("*" * 40)