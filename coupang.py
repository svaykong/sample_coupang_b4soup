from urllib.parse import unquote, quote
from bs4 import BeautifulSoup

from request_util import get, getWithUserAgent

class Coupang:
    def __init__(self):
        print("Coupang construct!")
        self.host = 'https://www.coupang.com'
        self.url = ''
        self.param = ''
        self.user_agent = None
        pass
    
    
    def searchProduct(self, words: str = None):
        print("Coupang searchProduct call!")
        try:    
            if words is None or words == '':
                raise Exception('Please search text!')
                            
            self.user_agent = {            
                'Host': 'www.coupang.com',
                'Connection': 'keep-alive',
                'sec-ch-ua': '"Chromium";v="130", "Whale";v="4", "Not.A/Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Whale/4.29.282.15 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://www.coupang.com/',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,ko;q=0.7,ja;q=0.6',
            }
            
            self.url = '/np/search?'
            self.param = 'component=' 
            self.param += '&q='       + quote(words)
            self.param += '&channel=' + 'user'
            rsltObj = getWithUserAgent(url=self.host + self.url + self.param, headers=self.user_agent)
            print(rsltObj.status_code)
            
            if rsltObj.status_code == 200:
                soup = BeautifulSoup(rsltObj.text, 'html.parser')
                
                # ul#productList
                product_list = soup.find(name='ul', attrs={'id': 'productList'})
                if product_list is None:
                    raise Exception("product_list is empty!")
                      
                '''
                    product_name
                    product_base_price
                    product_sell_price
                    delivery_fee
                    total_rating
                    product_image
                '''          
                for list in product_list.find_all(name='li', recursive=False): # Set recursive=False to avoid deeper nested items
                    product_name = list.find(name='div', attrs={'class': 'name'})
                    if product_name:
                        product_name = product_name.text.strip() # Strip to remove extra spaces
                    print(f'name: {product_name}')
                    
                    product_price = list.find(name='div', attrs={'class': 'price'})
                    
                    product_base_price = product_price.find(name='del', attrs={'class': 'base-price'})
                    if product_base_price:
                        product_base_price = product_base_price.text.replace(',', '')
                        product_base_price = product_base_price.strip() # Strip to remove extra spaces
                    else:
                        product_base_price = ''
                    print(f'base price: {product_base_price}')
                    
                    product_sell_price = product_price.find(name='strong', attrs={'class': 'price-value'})
                    if product_sell_price:
                        product_sell_price = product_sell_price.text.replace(',', '')
                        product_sell_price = product_sell_price.strip() # Strip to remove extra spaces
                    else:
                        product_sell_price = ''
                    print(f'sell price: {product_sell_price}')
                    
                    delivery_fee = list.find(name='span', attrs={'class': 'badge-delivery'})
                    if delivery_fee:
                        delivery_fee = delivery_fee.text.strip() # Strip to remove extra spaces
                    else:
                        delivery_fee = ''
                    print(f'delivery fee: {delivery_fee}')
                    
                    total_rating = list.find(name='span', attrs={'class': 'rating-total-count'})
                    if total_rating:
                        total_rating = total_rating.text.strip() # Strip to remove extra spaces
                        total_rating = total_rating.replace('(', '').replace(')', '')
                    print(f'total rating: {total_rating}')
                    
                    product_image = list.find(name='img', attrs={'class': 'search-product-wrap-img'})
                    if product_image:
                        product_image = 'https:' + product_image.get('src')
                    print(f'product image: {product_image}')
                
        except Exception as e:
            print(f"Coupang searchProduct exception:: {e}")
    
    def __del__(self):
        print("Coupang destruct!")
        pass