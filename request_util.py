import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get(url: str = None):
    try:
        if url is None or url == '':
            raise Exception('Invalid url!')
        
        return requests.get(url=url, verify=False)
    except Exception as e:
        print(f'get requests exception:: {e}')
        return None
    finally:
        print('get requests finally!')
        
        
def getWithUserAgent(url: str = None, headers: dict = None):
    try:
        if url is None or url == '':
            raise Exception('Invalid url!')
        
        if headers is None or url == {}:
            raise Exception('Invalid headers!')
        
        return requests.get(url=url, headers=headers, verify=False)
    except Exception as e:
        print(f'getWithUserAgent requests exception:: {e}')
        return None
    finally:
        print('getWithUserAgent requests finally!')