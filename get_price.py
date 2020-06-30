import time
import urllib
import requests
from bs4 import BeautifulSoup

def get_c5_price_api(item_name):
    cookie_c5_str = 'device_id=da7765bbb48ad582540f1f1f76d10d08; Hm_lvt_86084b1bece3626cd94deede7ecf31a8=1592502558,1592789658,1592835898,1593338858; C5Lang=en; C5SessionID=ccq6id0927jst4g43ifm742isd; C5Sate=f5030ac95a7edc889ced2722d7a49d05bce42a38a%3A4%3A%7Bi%3A0%3Bs%3A7%3A%222849904%22%3Bi%3A1%3Bs%3A11%3A%2214715025859%22%3Bi%3A2%3Bi%3A86400%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D; C5Token=5ef8d07dcdb32; C5Login=2849904; c5IsBindPhone=1; c5user=14715025859; C5Appid=570; Hm_lpvt_86084b1bece3626cd94deede7ecf31a8=1593364607'
    cookie_c5_list = cookie_c5_str.split('; ')
    cookie_c5 = dict([p.split('=') for p in cookie_c5_list])
    header_c5 = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch, br',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Host':'www.c5game.com',
            'Pragma':'no-cache',
            'Referer':'https://www.c5game.com/user/purchase/index.html',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }
    item_url = ('https://www.c5game.com/dota.html?min=&max=&only=on&k={0}&rarity=&quality=&hero=&tag=&sort='
                .format(urllib.parse.quote(item_name)))
    try:
        r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        if r.status_code != 200:
            time.sleep(1.0)
            r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list = soup.find_all('li', {'class':'purchaseing'})
        for item in item_list:
            name = item.find('p', {'class':'name'}).a.span.text.strip()
            price = item.find('span', {'class':'price'}).text.split('￥')[-1].strip()
            price = float(price)
            if name != item_name:
                continue
            break
        return price, 'success'
    except Exception as e:
        return None, str(e)

def get_c5_csgo_price_api(item_name):
    cookie_c5_str = 'device_id=da7765bbb48ad582540f1f1f76d10d08; Hm_lvt_86084b1bece3626cd94deede7ecf31a8=1592502558,1592789658,1592835898,1593338858; C5Lang=en; C5SessionID=ccq6id0927jst4g43ifm742isd; C5Sate=f5030ac95a7edc889ced2722d7a49d05bce42a38a%3A4%3A%7Bi%3A0%3Bs%3A7%3A%222849904%22%3Bi%3A1%3Bs%3A11%3A%2214715025859%22%3Bi%3A2%3Bi%3A86400%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D; C5Token=5ef8d07dcdb32; C5Login=2849904; c5IsBindPhone=1; c5user=14715025859; C5Appid=570; Hm_lpvt_86084b1bece3626cd94deede7ecf31a8=1593364607'
    cookie_c5_list = cookie_c5_str.split('; ')
    cookie_c5 = dict([p.split('=') for p in cookie_c5_list])
    header_c5 = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch, br',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Host':'www.c5game.com',
            'Pragma':'no-cache',
            'Referer':'https://www.c5game.com/csgo/default/result.html',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }
    if '★' in item_name and '|' not in item_name:
        item_url = ('https://www.c5game.com/csgo/default/result.html?min=&max=&only=on&k={0}&csgo_filter_category=&rarity=&quality=&exterior=WearCategoryNA&sort=&type=&tag='
                    .format(urllib.parse.quote(item_name)))
    else:
        item_url = ('https://www.c5game.com/csgo/default/result.html?min=&max=&only=on&k={0}&csgo_filter_category=&rarity=&quality=&exterior=&sort=&type=&tag='
                    .format(urllib.parse.quote(item_name)))
    try:
        r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        if r.status_code != 200:
            time.sleep(1.0)
            r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list = soup.find_all('li', {'class':'purchaseing'})
        for item in item_list:
            api_url = ''
            purchase_url = 'https://www.c5game.com' + item.a.get('href')
            name = item.find('p', {'class':'name'}).a.span.text.strip()
            price = item.find('span', {'class':'price'}).text.split('￥')[-1].strip()
            price = float(price)
            if name != item_name:
                continue
            price_list = []
            need_list = []
            break
        return price, 'success'
    except Exception as e:
        return None, str(e)

if __name__ == '__main__':
    print(get_c5_csgo_price_api('★ M9 Bayonet'))
    print(get_c5_price_api('Dragonclaw Hook'))
