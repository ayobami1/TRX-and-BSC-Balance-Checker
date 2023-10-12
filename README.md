# Crypto Balance Checker

A Python program to check the balance of cryptocurrency addresses on the TRON and Binance Smart Chain networks.

## Overview

This Python program provides two main functions:

1. `GetBalanceTrc20`: A class to check the balance of TRC20 tokens on the TRON network.
2. `GetBalanceBsc`: A class to check the balance of BNB and USDT (BEP20) on the Binance Smart Chain.

## Prerequisites

Before using this program, ensure you have the necessary libraries installed:

- requests
- base58
- base64
- tronapi
- web3

You can install these libraries using `pip`. For example:

`pip install requests base58 base64 tronapi web3`
`pip install -r requirements.txt`



## Usage

You can use this program to check cryptocurrency balances on the TRON and Binance Smart Chain networks. Here's how to use it:

```python
# Import the necessary classes
from datetime import datetime
from your_module import GetBalanceTrc20, GetBalanceBsc

# Set the cryptocurrency address you want to check
ADDRESS = 'Your_Crypto_Address_Here'

# Get the current date as a timestamp
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Check TRX balance
GetBalanceTrc20().get_trx_balance(ADDRESS)

# Check USDT balance on TRON network
GetBalanceTrc20().get_usdt_balance(ADDRESS)

# Check BNB balance on Binance Smart Chain
bnb_balance, stamp = GetBalanceBsc().get_bnb_balance(address=ADDRESS, stamp=current_date)
print(f'BNB balance: {bnb_balance} BNB')

# Check USDT (BEP20) balance on Binance Smart Chain
usdt_balance, stamp = GetBalanceBsc().get_usdt_balance_bep20(address=ADDRESS, stamp=current_date)
print(f'USDT balance: {usdt_balance} USDT')
```
Make sure to replace 'Your_Crypto_Address_Here' with the actual cryptocurrency address you want to check.

you can check example and see how is being used



# Disclaimer
This program is for educational and informational purposes only. Use it responsibly and at your own risk. It does not require API keys but relies on public APIs, and its accuracy may vary.


License
This project is open-source and available under the MIT License.

