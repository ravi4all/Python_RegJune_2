import bs4
import urllib.request as url

http = url.urlopen('https://www.flipkart.com/general-knowledge-lucent-gk-book/p/itme9hgjrbd6zvm8?pid=9789384761547&lid=LSTBOK97893847615471ZZQFZ&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=2f0ccca8-233e-4f73-bd5e-58d23cf2ab57.9789384761547.SEARCH&ppt=sp&ppn=sp&ssid=lzjdmrg1v40000001561369994776&qH=7d8949bcbf85067f')

page = bs4.BeautifulSoup(http, 'lxml')

div = page.find('div', class_='_39LH-M')
a_tag = div.find_all('a')
reviewhref = a_tag[-1]['href']

for i in range(1,11):
    print("Page {}".center(30,'-').format(i))
    path = 'https://www.flipkart.com' + reviewhref + '&page={}'.format(i)
    http = url.urlopen(path)
    page = bs4.BeautifulSoup(http, 'lxml')

    ratingList = page.find_all('div', class_='hGSR34')
    reviewList = page.find_all('p', class_='_2xg6Ul')

    if len(reviewList) < 1:
        reviewList = page.find_all('div', class_='_2t8wE0')

    '''
    for rating in ratingList:
        print(rating.text)
    '''
    del ratingList[0]
    
    for rating, review in zip(ratingList, reviewList):
        print(rating.text)
        print(review.text.encode())
        print("---------------")
    






