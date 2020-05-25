import urllib
import requests
from bs4 import BeautifulSoup

def get_c5_lowest_price(item_name):
    cookie_c5_str = 'Hm_lvt_86084b1bece3626cd94deede7ecf31a8=1526418462; C5SessionID=ap7go5cti88ero31cmd89dsqn0; C5Lang=zh; Hm_lpvt_86084b1bece3626cd94deede7ecf31a8=1526418472'
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
    item_url = ('https://www.c5game.com/dota.html?min=&max=&k={0}&rarity=&quality=&hero=&tag=&sort='
                .format(urllib.parse.quote(item_name)))
    try:
        r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list = soup.find('ul', {'class':'list-item4'})
        name_list  = item_list.find_all('p', {'class':'name'})
        price_list = item_list.find_all('p', {'class':'info'})
        count = 0
        for item in name_list:
            if item.text.strip() == item_name:
                direct_url = 'https://www.c5game.com' + item.a.get('href')
                break
            else:
                count += 1
        lowest_price = float(price_list[count].find('span', {'class':'price'}).text.replace('￥', ''))
        current_volume = int(price_list[count].find('span', {'class':'num'}).text.replace('件在售', ''))
        return (lowest_price, current_volume, direct_url, 'C5GAME')
    except:
        return None

def get_c5_purchase_price(item_name):
    cookie_c5_str = 'Hm_lvt_86084b1bece3626cd94deede7ecf31a8=1526418462; C5SessionID=ap7go5cti88ero31cmd89dsqn0; C5Lang=zh; Hm_lpvt_86084b1bece3626cd94deede7ecf31a8=1526418472'
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
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list = soup.find('ul', {'class':'list-item4'})
        name_list  = item_list.find_all('p', {'class':'name'})
        price_list = item_list.find_all('p', {'class':'info'})
        count = 0
        for item in name_list:
            if item.text.strip() == item_name:
                break
            else:
                count += 1
        lowest_price = float(price_list[count].find('span', {'class':'price'}).text.replace('￥', ''))
        return lowest_price
    except:
        return None

def get_ig_lowest_price(item_name):
    cookie_str_ig = 'my_game=730; _ga=GA1.2.1160849148.1483030504; __cfduid=d498a5f4a768706be8ce32e8ea76108801526208573; notetop12563=close; my_steam_game=570; aliyungf_tc=AQAAAD4w60ZJJQIAEAWLaubjYQneH+q5; _gid=GA1.2.1742622629.1528036675; Hm_lvt_fe0238ac0617c14d9763a2776288b64b=1526208577,1526208672,1528036679; _gat=1; myDateMinutes=2; csrftoken=goxZPpILj1JpzG9At4nkoIETjfMiEpHZ; sessionid=ljiqvj93vdtnb5t064y8kdkojwm33rwf; Hm_lpvt_fe0238ac0617c14d9763a2776288b64b=1528113812'
    cookie_list_ig = cookie_str_ig.split('; ')
    cookie_ig = dict([p.split('=') for p in cookie_list_ig])
    header_ig = {
            'Accept':'text/html, application/xhtml+xml, image/jxr, */*',
            'Accept-Encoding':'gzip',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2',
            'Connection':'keep-alive',
            'Host':'www.igxe.cn',
            'Referer':'https://www.igxe.cn/dota2/570?keyword=',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }
    item_url = 'https://www.igxe.cn/dota2/570?keyword={0}'.format(urllib.parse.quote(item_name))
    try:
        r = requests.get(item_url, headers=header_ig, cookies=cookie_ig, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        items = soup.find('div', {'class':'dataList'})
        items = items.find_all('div', {'class':'single'})
        # items = soup.find_all('li', {'class':'dota-item'})
        for item in items:
            # first_name = item.find('a',{'class':'e-name'}).text
            first_name = item.div.a.text.strip()
            # direct_url = ('https://www.igxe.cn/product/570/' + 
            #               item.find('a',{'class':'e-name'}).get('href').replace('/dota2/product-', ''))
            direct_url = ('https://www.igxe.cn' +
                          item.div.a.get('href'))
            if first_name != item_name:
                continue
            else:
                # e_nums = item.find('div', {'class':'sum'})
                lowest_price = float(item.find('span', {'class':'c-4'}).text.replace('￥', ''))
                current_volume = int(item.find('span', {'class':'c-2'}).text)
                break
        return (lowest_price, current_volume, direct_url, 'IGXE')
    except:
        return None

def get_buff_lowest_price(item_name):
    cookie_str_buff = 'locale=zh; csrf_token=d2a40caeeb217c2ab925c917f0c7d2cc7b87964b; client_id=nqgFlUkfWfeMSyTVBDSdFQ; game=dota2; _ga=GA1.2.1925186173.1526441888; _gid=GA1.2.2107881256.1526441888'
    cookie_list_buff = cookie_str_buff.split('; ')
    cookie_buff = dict([p.split('=') for p in cookie_list_buff])
    header_buff = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,es;q=0.5',
            'Connection':'keep-alive',
            'Host':'buff.163.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }
    item_url = 'https://buff.163.com/api/market/goods?game=dota2&page_num=1&search={0}'.format(urllib.parse.quote(item_name))
    try:
        r = requests.get(item_url, headers=header_buff, cookies=cookie_buff, timeout=10)
        r_json = r.json()
        if 'code' in r_json and r_json['code'] == 'OK':
            for item in r_json['data']['items']:
                if item['name'] == item_name:
                    lowest_price = float(item['sell_min_price'])
                    current_volume = item['sell_num']
                    direct_url = 'https://buff.163.com/market/goods?goods_id={0}&from=market#tab=selling'.format(item['id'])
                    if lowest_price > 0:
                        return (lowest_price, current_volume, direct_url, 'BUFF')
                    else:
                        return None
        else:
            return None
    except:
        return None

def get_v5_lowest_price(item_name):
    cookie_str_v5 = 'aliyungf_tc=AQAAANkVLgQRBQkAjBn62ghr4Gf2th1+; JSESSIONID=EBE69F7BA1C7B524B5620ED22BDF6858; Hm_lvt_18959c73cdc8a1ef3068d6fcdaf0fa95=1526452929; Hm_lpvt_18959c73cdc8a1ef3068d6fcdaf0fa95=1526452929'
    cookie_list_v5 = cookie_str_v5.split('; ')
    cookie_v5 = dict([p.split('=') for p in cookie_list_v5])
    header_v5 = {
            'Accept':'text/html, application/xhtml+xml, image/jxr, */*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2',
            'Connection':'keep-alive',
            'Host':'www.v5fox.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }
    item_url = 'https://www.v5fox.com/dota2/0-0-0-0-0?keyword={0}'.format(urllib.parse.quote(item_name))
    try:
        r = requests.get(item_url, headers=header_v5, cookies=cookie_v5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list  = soup.find('div', {'class':'list-box'})
        for item in item_list.find_all('a',{'class':'list-item'}):
            first_name = item.get('title').strip()
            direct_url = 'https://www.v5fox.com' + item.get('href').strip()
            if first_name == item_name:
                box = item.find('div', {'class':'list-text-box'})
                lowest_price = float(box.p.span.text)
                current_volume = int(item.find('div', {'class':'r'}).text.replace('件 在售',''))
                break
        return (lowest_price, current_volume, direct_url, 'V5FOX')
    except:
        return None

def get_stm_lowest_price(item_name):
    cookie_str_stm = 'UM_distinctid=16332dee0b44cf-04d305a074d833-f373567-1fa400-16332dee0b5780; STMBUYSESSID=bdv6scsi28aqpiq89k2kst28q7; CNZZDATA1263263488=1839271337-1525561803-null%7C1528315112; Hm_lvt_9fa25625cfedf0974d032c99c64dbcb5=1527264354,1527304141,1528317471; __SDID=4802522b6bb4a57d; member_gotourl=%2Fdota2%3Fkeywords%3D%25E9%25BE%2599%25E7%2588%25AA%25E5%25BC%25AF%25E9%2592%25A9%2509; Hm_lpvt_9fa25625cfedf0974d032c99c64dbcb5=1528317515; utime=1528317514714'
    cookie_list_stm = cookie_str_stm.split('; ')
    cookie_stm = dict([p.split('=') for p in cookie_list_stm])
    header_stm = {
            'Accept':'text/html, application/xhtml+xml, image/jxr, */*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2',
            'Connection':'keep-alive',
            'Host':'www.stmbuy.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }
    item_url = 'http://www.stmbuy.com/dota2?keywords={}'.format(urllib.parse.quote(item_name))
    try:
        r = requests.get(item_url, headers=header_stm, cookies=cookie_stm, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list  = soup.find('ul', {'class':'goods-list'})
        for item in item_list.find_all('a', {'target':'_self'}):
            first_name = item.div.p.text.strip()
            direct_url = 'http://www.stmbuy.com' + item.get('href').strip()
            if first_name == item_name:
                box = item.find('div', {'class':'goods-bottom'})
                lowest_price = box.p.span.next_sibling.next_sibling.text
                lowest_price = float(lowest_price.replace('¥', ''))
                current_volume = item.find('p', {'class':'sec-tit'})
                current_volume = int(current_volume.span.text)
                if current_volume == 0:
                    return None
                break
        return (lowest_price, current_volume, direct_url, 'STMBUY')
    except:
        return None

def get_steam_lowest_price(item_market_hash_name):
    header_info = {
                'Accept':'text/html, application/xhtml+xml, image/jxr, */*',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
                'Connection':'Keep-Alive',
                'Cookie': 'ActListPageSize=10; _ga=GA1.2.1034459796.1527050091; _gid=GA1.2.590684032.1527050091; timezoneOffset=28800,0; steamMachineAuth76561198099311044=F5D1D172843ED5299BB6E21615A2BB99DF374EB7; strInventoryLastContext=570_2; sessionid=cf60fc29ee29d450ee92e493; tsTradeOffersLastRead=1527144436; steamCountry=HK%7C9290562ede90d797e187dc64abadbf2d',
                'Host':'steamcommunity.com',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
                }
    price_ext_url='https://steamcommunity.com/market/listings/570/{0}/render/'.format(item_market_hash_name.replace(' ', '%20').replace(':', '%3A').replace('?', '%3F'))
    params = {'start':0, 'count':1, 'country':'CN', 'currency':23, 'language':'schinese'}
    try:
        r = requests.get(price_ext_url, params=params, headers=header_info, timeout=10)
        r_json = r.json()
        lowest_price = list(r_json['listinginfo'].values())[0]['converted_price']/100*1.15
        lowest_price = round(lowest_price, 2)
        direct_url = 'https://steamcommunity.com/market/listings/570/{0}'.format(item_market_hash_name.replace(' ', '%20').replace(':', '%3A').replace('?', '%3F'))
        current_volume = 0
        return (lowest_price, current_volume, direct_url, 'STEAM')
    except:
        return None

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
        r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list = soup.find('div', {'class':'keys'})
        span_list = item_list.find_all('span')
        for span in span_list:
            span = span.text
            api_url = 'https://www.c5game.com/api/product/purchase.json?id={0}&page=1&_=1578838056651'.format(span)
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

def get_c5_lowest_price_api(item_name):
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
    item_url = ('https://www.c5game.com/dota.html?min=&max=&k={0}&rarity=&quality=&hero=&tag=&sort='
                .format(urllib.parse.quote(item_name)))
    try:
        r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list = soup.find_all('li', {'class':'selling'})
        for item in item_list:
            price_item = item.find('span', {'class':'price'})
            name = item.find('p', {'class':'name'}).a.span.text.strip()
            #print(name, item)
            #print(name, item_name, name == item_name)
            if name == item_name:
                #print(item)
                #price_item = item.find('span', {'class':'price'})
                #print(price_item)
                price = price_item.text.replace('￥', '')
                price = float(price)
                return price, [], []
        else:
            return None, None, None
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
    item_url = ('https://www.c5game.com/csgo/default/result.html?min=&max=&only=on&k={0}&csgo_filter_category=&rarity=&quality=&exterior=&sort=&type=&tag='
                .format(urllib.parse.quote(item_name)))
    try:
        r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_list = soup.find_all('li', {'class':'purchaseing'})
        for item in item_list:
            purchase_url = 'https://www.c5game.com' + item.a.get('href')
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
        return avg_price, price_list, need_list
    except:
        return None, None, None

def get_c5_csgo_lowest_price_api(item_name):
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
    item_url = ('https://www.c5game.com/csgo/default/result.html?min=&max=&k={0}&csgo_filter_category=&rarity=&quality=&exterior=&sort=&type=&tag='
                .format(urllib.parse.quote(item_name)))
    try:
        r = requests.get(item_url, cookies=cookie_c5, headers=header_c5, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        sell_list = soup.find('li', {'class':'selling'})
        item_list = sell_list.find_all('span', {'class':'price'})
        for item in item_list:
            price = item.text.replace('￥', '')
            price = float(price)            
            return price, [], []
        else:
            return None, None, None
    except:
        return None, None, None



if __name__ == '__main__':
    print(get_c5_csgo_lowest_price_api('AK-47 | Hydroponic (Factory New)'))
    print(get_c5_csgo_price_api('AK-47 | Hydroponic (Factory New)'))
    print(get_c5_lowest_price_api('Dragonclaw Hook'))
    print(get_c5_price_api('Dragonclaw Hook'))
