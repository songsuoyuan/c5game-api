from flask import request, jsonify
from flask import Flask

from get_price import get_c5_lowest_price, get_buff_lowest_price, get_v5_lowest_price, get_ig_lowest_price, get_stm_lowest_price, get_steam_lowest_price, get_c5_purchase_price, get_c5_price_api, get_c5_csgo_price_api
from get_price import get_c5_lowest_price_api, get_c5_csgo_lowest_price_api

app = Flask(__name__)

@app.route('/api/price', methods=['GET'])
def c5_price():
    item_name = request.args.get('hash_name')
    if item_name is None:
        return jsonify({'hash_name':None, 'steam_prices_net_price':None, 'message':'Empty hash_name params!'})
    # if csgo
    if '|' in item_name:
        avg_price, price_list, need_list = get_c5_csgo_price_api(item_name)
        if avg_price is None:
            avg_price, price_list, need_list = get_c5_csgo_lowest_price_api(item_name)
    # try dota
    else:
        avg_price, price_list, need_list = get_c5_price_api(item_name)
        if avg_price is None:
            avg_price, price_list, need_list = get_c5_lowest_price_api(item_name)
            # try csgo again
            if avg_price is None:
                avg_price, price_list, need_list = get_c5_csgo_price_api(item_name)
                if avg_price is None:
                    avg_price, price_list, need_list = get_c5_csgo_lowest_price_api(item_name)
    if avg_price is None:
        return jsonify({'hash_name':item_name, 
                        'steam_prices_net_price':None, 
                        'message':'Either c5game.com is temporaryly unavailable or hash_name params is not correct!'})
    else:
        return jsonify({'hash_name':item_name, 
                        'steam_prices_net_price':avg_price, 
                        'message':('Success! price_list: '+str(price_list)+' and need_num_list: '+str(need_list))})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
