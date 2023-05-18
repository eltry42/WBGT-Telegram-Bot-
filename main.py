import requests
import pandas as pd
import time
from keepalive import keep_alive 
from datetime import datetime

now = datetime.now()

def run():

  keep_alive()

  try:
    
    def send_message ():
        location = "Old Choa Chu Kang Road"
        tables = pd.read_html("https://www.wbgt.sg/allstations")
        tables[0].to_csv("my_file.csv")
        data = pd.read_csv("my_file.csv")
        
        row_of_location = data[data.Location == location]

        wbgt_code = row_of_location["WBGT Code"].item()
        wbgt_reading = row_of_location["WBGT Reading"].item()

        if wbgt_reading >= 35:
          base_url = 'https://api.telegram.org/bot6087536906:AAHQFuawb2xk_KlnrDdoAuAE4HE2wbqXbhU/sendMessage?chat_id=-1001626786883&text={}'.format(f"WBGT Reading is {wbgt_reading}, \033[1mno strenous training\033[0m")

        else:
          base_url = 'https://api.telegram.org/bot6087536906:AAHQFuawb2xk_KlnrDdoAuAE4HE2wbqXbhU/sendMessage?chat_id=-1001626786883&text={}'.format(f"WBGT Reading is {wbgt_reading} and WBGT Code is {wbgt_code}")
      
        requests.get(base_url)
        time.sleep(3600)
    
    while True:
        send_message()
 
  except ValueError:
    print("URL is not working. Please Standby or type manually :)")
    time.sleep(60)
    pass

while 7 <= now.hour <= 19:
    run()


