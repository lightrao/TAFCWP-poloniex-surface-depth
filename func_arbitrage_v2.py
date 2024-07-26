import requests
import json

# make a get request
def get_coin_tikers(url):
    req=requests.get(url)
    json_resp=json.loads(req.text)
    return json_resp

# Loop through each objects and find the tradeable pairs
def collect_tradeables(json_obj):
    coin_list = []
    for coin in json_obj:
        coin_list.append(coin["symbol"])
    return coin_list