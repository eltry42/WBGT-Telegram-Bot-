import requests
import pandas as pd
import time
from keepalive import keep_alive 

location = "Old Choa Chu Kang Road"
tables = pd.read_html("https://www.wbgt.sg/allstations")
tables[0].to_csv("my_file.csv")
data = pd.read_csv("my_file.csv")

row_of_location = data[data.Location == location]
wbgt_code = row_of_location["WBGT Code"].item()
wbgt_reading = row_of_location["WBGT Reading"].item()

keep_alive()

base_url = 'https://api.telegram.org/bot6098228864:AAEdx6waT3Hl0kAPWhbJSJAGCFWJeLnGfrk/sendMessage?chat_id=-1001800784547&text={}'.format(f"WBGT Reading is {wbgt_reading} and WBGT Code is {wbgt_code}")
while True:
    requests.get(base_url)
    time.sleep(3600)

#https://api.telegram.org/bot6098228864:AAEdx6waT3Hl0kAPWhbJSJAGCFWJeLnGfrk/getUpdates
#-1001800784547