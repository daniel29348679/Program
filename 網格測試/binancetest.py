#%%
import os
from binance.client import Client
from time import sleep
from binance import ThreadedWebsocketManager
import csv
#%%
api_key = "NQXofEkG889NjovjmYnFb8Gr7GSNxkNBKjqG35vlok2RUAiodaOgOZxB6p9JE71u"
api_secret = "A5czJL3pRZYkVoyFlznPnshygVtOifkon2lcvzaV46upTLqLlE3HxRlcgrkuA9RV"
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'
print(client.get_account())
# %%
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
print(btc_price['price'])
# %%
timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1m')
bars = client.get_historical_klines('BTCUSDT', '1m', timestamp, limit=1000)
with open('btc_bars.csv', 'w', newline='') as f:
    for line in bars:
        f.write(f'{line[0]}, {line[1]}\n')

# %%
