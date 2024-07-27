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
    pairs_list = coin_list[0:]

    # Get Pair A
    for pair_a in pairs_list:
        print("***********")
        print("pair_a: ", pair_a)
        pair_a_split = pair_a.split("_")
        a_base = pair_a_split[0]
        a_quote = pair_a_split[1]

        # Assign A to a Box
        a_pair_box = [a_base, a_quote]

        # Get Pair B
        for pair_b in pairs_list:
            pair_b_split = pair_b.split("_")
            b_base = pair_b_split[0]
            b_quote = pair_b_split[1]

            # Check Pair B
            if pair_b != pair_a:
                if b_base in a_pair_box or b_quote in a_pair_box:
                    # here we successfully identified pari and a pair b

                    # Get Pair C
                    print("pair_b: ", pair_b)
