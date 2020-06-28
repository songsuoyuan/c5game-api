import time
import urllib
import requests
from bs4 import BeautifulSoup

def get_c5_price_api(item_name):
    cookie_c5_str = 'MEIQIA_EXTRA_TRACK_ID=0rYfHD2wcmHCOZN6nfkVSh76hoo; isNewUser=-1; C5Lang=en; device_id=97c3f2c992b8e5ea33ec6c85d40207d9; Hm_lvt_86084b1bece3626cd94deede7ecf31a8=1578829961; C5SessionID=ostfu5kldqkhgnsa267p99p627; C5Sate=6f29823b8ef2ea1e8e8bc36b255eeeba6212e197a%3A4%3A%7Bi%3A0%3Bs%3A7%3A%222849904%22%3Bi%3A1%3Bs%3A11%3A%2214715025859%22%3Bi%3A2%3Bi%3A259200%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D; C5Token=5e1b08914daf8; C5Login=2849904; c5IsBindPhone=1; c5user=14715025859; C5Appid=570; C5NewHome=1; Hm_lpvt_86084b1bece3626cd94deede7ecf31a8=1578830029'
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
        time.sleep(0.5)
        r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list = soup.find('div', {'class':'keys'})
        span_list = item_list.find_all('span')
        for span in span_list:
            span = span.text
            api_url = 'https://www.c5game.com/api/product/purchase.json?id={0}&page=1&_=1578838056651'.format(span)
            time.sleep(0.5)
            r_json = requests.get(api_url, cookies=cookie_c5, headers=header_c5, timeout=10)
            purchase_list = r_json.json()['body']['items']
            hash_name = purchase_list[0]['item']['market_hash_name']
            if hash_name != item_name:
                continue
            first_price = purchase_list[0]['price']
            price_list = []
            need_list = []
            for item in purchase_list:
                price = item['price']
                need = item['need_num']
                if price < 0.9*first_price:
                    break
                price_list.append(price)
                need_list.append(need)
            break
        avg_price = sum([price_list[i]*need_list[i] for i in range(len(price_list))])/sum(need_list)
        avg_price = round(avg_price, 2)
        return avg_price, price_list, need_list
    except:
        return None, None, None

def get_c5_csgo_price_api(item_name):
    cookie_c5_str = 'MEIQIA_EXTRA_TRACK_ID=0rYfHD2wcmHCOZN6nfkVSh76hoo; isNewUser=-1; C5Lang=zh; device_id=97c3f2c992b8e5ea33ec6c85d40207d9; Hm_lvt_86084b1bece3626cd94deede7ecf31a8=1578829961; C5SessionID=ostfu5kldqkhgnsa267p99p627; C5Sate=6f29823b8ef2ea1e8e8bc36b255eeeba6212e197a%3A4%3A%7Bi%3A0%3Bs%3A7%3A%222849904%22%3Bi%3A1%3Bs%3A11%3A%2214715025859%22%3Bi%3A2%3Bi%3A259200%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D; C5Token=5e1b08914daf8; C5Login=2849904; c5IsBindPhone=1; c5user=14715025859; C5Appid=570; C5NewHome=1; Hm_lpvt_86084b1bece3626cd94deede7ecf31a8=1578830029'
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
        time.sleep(0.5)
        r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list = soup.find_all('li', {'class':'purchaseing'})
        for item in item_list:
            purchase_url = 'https://www.c5game.com' + item.a.get('href')
            time.sleep(0.5)
            r_item = requests.get(purchase_url, cookies=cookie_c5, headers=header_c5, timeout=10)
            soup_item = BeautifulSoup(r_item.text, 'html.parser')
            hash_name = soup_item.find('div', {'class':'steamUrl'}).a.get('href').split('/730/')[1]
            if hash_name != item_name:
                continue
            api_url = 'https://www.c5game.com' + soup_item.find('tbody', {'data-tpl':'purchase-tpl'}).get('data-url')
            r_json = requests.get(api_url, cookies=cookie_c5, headers=header_c5, timeout=10)
            purchase_list = r_json.json()['body']['items']
            first_price = purchase_list[0]['price']
            price_list = []
            need_list = []
            for item in purchase_list:
                price = item['price']
                need = item['need_num']
                if price < 0.9*first_price:
                    break
                price_list.append(price)
                need_list.append(need)
            break
        avg_price = sum([price_list[i]*need_list[i] for i in range(len(price_list))])/sum(need_list)
        avg_price = round(avg_price, 2)
        return avg_price, price_list, need_list, api_url, purchase_url
    except:
        return None, None, None, None, None


if __name__ == '__main__':
    print(get_c5_csgo_price_api('★ M9 Bayonet'))
    print(get_c5_price_api('Dragonclaw Hook'))
