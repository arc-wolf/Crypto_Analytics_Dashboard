import requests
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time

API_URL = "https://api.coingecko.com/api/v3/simple/price"
COINS = ['bitcoin', 'ethereum', 'dogecoin']
CURRENCY = 'usd'

bucket = "crypto_bucket"
org = "crypto_org"
token = "token123"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

while True:
    try:
        response = requests.get(API_URL, params={"ids": ",".join(COINS), "vs_currencies": CURRENCY})
        data = response.json()
        now = datetime.utcnow()

        for coin in COINS:
            price = data[coin][CURRENCY]
            point = Point(coin).field("price", price).time(now, WritePrecision.NS)
            write_api.write(bucket=bucket, org=org, record=point)
            print(f"[✅] Wrote {coin} with field `price`: ${price}")

        time.sleep(60)

    except Exception as e:
        print(f"[❌] Error: {e}")
        time.sleep(60)
