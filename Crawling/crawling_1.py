import bs4
import urllib.request as url

http = url.urlopen('https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
print(http)
page = bs4.BeautifulSoup(http,'lxml')

'''
div = page.find('div',class_='_3wU53n')
print(div.text)
'''

divList = page.find_all('div',class_='_3wU53n')
'''
for div in divList:
    print(div.text)
'''
priceList = page.find_all('div', class_='_1vC4OE')
'''
for item in priceList:
    print(item.text)
'''

'''
for i in range(len(divList)):
    print(divList[i].text)
    print(priceList[i].text)
    print("##############")
'''

for div, price in zip(divList, priceList):
    print(div.text)
    print(price.text)
    print("##############")

