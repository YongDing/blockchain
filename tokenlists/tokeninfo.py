import os
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
from web3.middleware import geth_poa_middleware
import json
import time
import binascii

mainnet_address = "https://bsc-dataseed1.binance.org:443"
testnet_address = "https://data-seed-prebsc-1-s1.binance.org:8545"

w3 = Web3(HTTPProvider(mainnet_address))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

common_token_abi = json.loads(open("static/common_token.json").read())


def generate_common_contract(address):
    return w3.eth.contract(address, abi=common_token_abi)


def token_info(address):
    token_contract = generate_common_contract(address)
    token_name = token_contract.functions.name().call()
    token_symbol = token_contract.functions.symbol().call()
    token_decimals = token_contract.functions.decimals().call()
    token_dict = {
        "name": token_name,
        "symbol": token_symbol,
        "address": address,
        "chainId": 56,
        "decimals": token_decimals,
    }
    print(json.dumps(token_dict, indent=4, sort_keys=True))


if __name__ == '__main__':
    address = w3.toChecksumAddress("0x8c851d1a123ff703bd1f9dabe631b69902df5f97")
    token_info(address)
