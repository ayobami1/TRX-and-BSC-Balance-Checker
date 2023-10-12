# Import the necessary classes
from datetime import datetime
from pycryptchecker import GetBalanceTrc20, GetBalanceBsc

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
