from coupang import Coupang

if __name__ == '__main__':
    print(f'{__name__}:: main enty ponit start!')
    
    coupang_obj = Coupang()
    coupang_obj.searchProduct(words='컴퓨터')