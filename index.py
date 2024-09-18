from bs4 import BeautifulSoup
from urllib import request

url = 'https://eshop-prices.com/games/popular?currency=EUR'
headers = {'User-Agent':'Chrome/128.0.0.0'}
response = request.Request(url,headers=headers)
html = request.urlopen(response)
soup = BeautifulSoup(html,'html.parser')
game_info = dict()

populars = soup.find_all('div',{'class':'flex flex-column gap-4 overflow-hidden width-full'})

for popular in populars:
    for game in popular.children:
        if game.name:
            h5_tag = game.find('h5')
            price_tags = game.find('span',{'class':'price-tag'})
            
            for price_tag in price_tags.children:
                if price_tag.name != 'del':
                    game_info[h5_tag.text] = {'price':price_tag.name}
                        
                            
for name,price in game_info.items():
    print(f"{name}:{price}")