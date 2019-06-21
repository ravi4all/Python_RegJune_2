import bs4
import urllib.request as url

path = 'https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
x = url.urlopen(path)
#print(x)

#lxml - parser library

page = bs4.BeautifulSoup(x,'lxml')
#title = page.find('div', class_='_3wU53n')
#print(title.text)

titles = page.find_all('div', class_='_3wU53n')
for item in titles:
    print(item.text)
