from datetime import datetime

import requests
import base58
import base64
from pprint import pprint
from tronapi import Tron


##BSC LIBRARY
from web3 import Web3
bsc_rpc_url = "https://bsc-dataseed.binance.org/"
w3_bsc = Web3(Web3.HTTPProvider(bsc_rpc_url))


CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"  # USDT
"main net"
API_URL_BASE = 'https://api.trongrid.io/'


METHOD_BALANCE_OF = 'balanceOf(address)'
METHOD_TRANSFER = 'transfer(address,uint256)'
DEFAULT_FEE_LIMIT =1_000_000  # 1 TRX




#Get the current data as stamp

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class GetBalanceTrc20:



    def address_to_parameter(self, addr):
        return "0" * 24 + base58.b58decode_check(addr)[1:].hex()

    def get_usdt_balance(self, address=ADDRESS):
        # print("ADDRESS : " , ADDRESS)
        url = API_URL_BASE + 'wallet/triggerconstantcontract'
        payload = {
            'owner_address': base58.b58decode_check(ADDRESS).hex(),
            'contract_address': base58.b58decode_check(CONTRACT).hex(),
            'function_selector': METHOD_BALANCE_OF,
            'parameter': self.address_to_parameter(address),
        }
        resp = requests.post(url, json=payload)
        data = resp.json()

        if data['result'].get('result', None):
            hex_balance = data['constant_result'][0]
            int_balance = int(hex_balance, 16)
            decimals = 6
            float_balance = int_balance / (10 ** decimals)

            #print('USDT balance =', float_balance)
            return float_balance
        else:
            #print('error:', bytes.fromhex(data['result']['message']).decode())
            return bytes.fromhex(data['result']['message']).decode()


    def get_trx_balance(self, address=ADDRESS):
        url = API_URL_BASE + 'wallet/getaccount'
        payload = {
            'address': base58.b58decode_check(address).hex(),
        }
        resp = requests.post(url, json=payload)
        data = resp.json()

        if data.get('balance', None):
            trx_balance = int(data['balance']) / (10 ** 6)
            #print('TRX balance =', trx_balance)
            return trx_balance
        else:
            # print('Error:', data.get('error_message', 'Unknown error'))
            return 'Unknown error'

class GetBalanceBsc:
    usdt_contract_address = "0x55d398326f99059fF775485246999027B3197955"
    usdt_bep20_abi = [
        {
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_to", "type": "address"},
                {"name": "_value", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]


    def get_bnb_balance(self,address, stamp):
        bnb_balance = w3_bsc.eth.get_balance(address)
        bnb_balance_in_bnb = bnb_balance / 10 ** 18
        # print(bnb_balance_in_bnb)
        return bnb_balance_in_bnb, stamp

    def get_usdt_balance_bep20(self, address, stamp):
        self.usdt_bep20_contract = w3_bsc.eth.contract(address=self.usdt_contract_address, abi=self.usdt_bep20_abi)

        return self.usdt_bep20_contract.functions.balanceOf(address).call() / 1e18, stamp



#Usage for BSC
bsc_balance = GetBalanceBsc()
address = '0x99F427c0544CD7E9F66b349A2E4A274066d264Ea'
print(bsc_balance.get_bnb_balance(address=address, stamp=current_date))
print(bsc_balance.get_usdt_balance_bep20(address=address, stamp=current_date))

# Usage FOR TRC
ADDRESS = 'TMDCtzCUVBHtLQQmZEis1osCQgbVsCELDF'
print(GetBalanceTrc20().get_trx_balance(ADDRESS))

print(GetBalanceTrc20().get_usdt_balance(ADDRESS))
