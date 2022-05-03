import json
import time
import msvcrt #Consola solo para windows I/O
#qfrom traceback import format_exception_only
import colorama
from colorama import Fore
from datetime import datetime
from wsgiref import headers
import requests

    
print(Fore.LIGHTBLUE_EX + '-----------------------------------------------')
print('Cotización BITCOIN-COINBASE')
print('-----------------------------------------------')

while True:
    if msvcrt.kbhit():
        print(Fore.WHITE +'Finalizó la tarea')
        break 
    time.sleep(1)
    bitcoin= requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
    print(Fore.GREEN +'USD ',bitcoin.json()['data']['rates']['EUR'], datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
