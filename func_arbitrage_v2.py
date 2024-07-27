import requests
import json


# make a get request
def get_coin_tikers(url):
    req = requests.get(url)
    json_resp = json.loads(req.text)
    return json_resp


# Loop through each objects and find the tradeable pairs
def collect_tradeables(json_obj):
    coin_list = []
    for coin in json_obj:
        coin_list.append(coin["symbol"])
    return coin_list


# Structure Arbitrage Pairs
def structure_triangular_pairs(coin_list):

    # Declare Variables
    triangular_pairs_list = []
    remove_duplicates_list = []
    pairs_list = []

    # Get Pair A
    for pair_a in coin_list:
        pair_a_split = pair_a.split("_")
        a_base = pair_a_split[0]
        a_quote = pair_a_split[1]
        print(a_base, a_quote)
