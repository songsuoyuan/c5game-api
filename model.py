from flask import request, jsonify
from flask import Flask

from datetime import datetime
from get_price import get_c5_price_api, get_c5_csgo_price_api

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/api/price', methods=['GET'])
def c5_price():
    item_name = request.args.get('hash_name')
    if item_name is None:
        return jsonify({'hash_name':None, 'steam_prices_net_price':None, 'message':'empty hash_name!'})
    # if csgo
    if '|' in item_name:
        price, info = get_c5_csgo_price_api(item_name)
    # try dota
    else:
        price, info = get_c5_price_api(item_name)
        # try csgo again
        if price is None:
            price, info = get_c5_csgo_price_api(item_name)
    if price is None:
        return jsonify({'hash_name':item_name, 
                        'steam_prices_net_price':None, 
                        'message':info})
    else:
        return jsonify({'hash_name':item_name, 
                        'steam_prices_net_price':price, 
                        'message':info})

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(debug=True)

