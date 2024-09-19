import time
import os
from bs4 import BeautifulSoup
from urllib import request




def main():
    base_url = 'https://eshop-prices.com/games/popular?currency=EUR&page='
    page = 1
    page_size = 2
    headers = {'User-Agent':'Chrome/128.0.0.0'}
    game_info = dict()
    names_arr = list()
    price_arr = list()
    loading = 'Cargando.'
    while page <= page_size:
        response = request.Request(base_url + str(page),headers=headers)
        html = request.urlopen(response)
        soup = BeautifulSoup(html,'html.parser')
        populars = soup.find_all('div',{'class':'flex flex-column gap-4 overflow-hidden width-full'})

        print(loading)
        # Buscando juegos por nombre y precio
        for popular in populars:
            for game in popular.children:
                if game.name:
                    h5_tag = game.find('h5')
                    price_tags = game.find('span',{'class':'price-tag'})
                    
                    if h5_tag:
                        names_arr.append(h5_tag.text)
                    if price_tags:
                        for price_tag in price_tags.children:
                            if price_tag.name != 'del':
                                    price_arr.append(price_tag.text.strip())

        page += 1
        time.sleep(0.001)
        loading += '.'

    # Formando los precios
    price_arr = [item for item in price_arr if item]

    for i in range(0,len(names_arr)):
        name = names_arr[i]
        price = price_arr[i]
        game_info[name] = price
        
    
    #Ordenando precios
    sorted_prices_dict = sort_prices(game_info)

    #Mostrando precios
    os.system('cls')
    for name,price in sorted_prices_dict.items():
        print(f"{name} - {price}")

    
    
def sort_prices(game_info):
    temp_data_tuple = tuple()
    temp_price = 0.0
    sorted_prices_list = list()
    sorted_prices_dict = dict()
    for name,price in game_info.items():
        temp_price = price.replace("€","").replace(',','.').strip()
        temp_price = float(temp_price)
        temp_data_tuple = (temp_price,name) 
        sorted_prices_list.append(temp_data_tuple)
    
    for price,name in sorted(sorted_prices_list):
        sorted_prices_dict[name] = f"€{price:.2f}"
        
    return sorted_prices_dict
    

if __name__ == '__main__':
    main()