import requests
import pandas as pd
import time
from keepalive import keep_alive
from datetime import datetime
from pytz import timezone

tz = timezone("Asia/Singapore")
now = datetime.now(tz)

def run():

  keep_alive()

  try:

    def send_message():
      location = "Old Choa Chu Kang Road"
      tables = pd.read_html("https://www.wbgt.sg/allstations")
      tables[0].to_csv("my_file.csv")
      data = pd.read_csv("my_file.csv")

      row_of_location = data[data.Location == location]

      wbgt_code = row_of_location["WBGT Code"].item()
      wbgt_reading = row_of_location["WBGT Reading"].item()

      if wbgt_reading >= 35:
        base_url = 'https://api.telegram.org/bot6087536906:AAHQFuawb2xk_KlnrDdoAuAE4HE2wbqXbhU/sendMessage?chat_id=-1001480559009&text={}'.format(
          f"WBGT Reading is {wbgt_reading}, no strenous training")

      else:
        base_url = 'https://api.telegram.org/bot6087536906:AAHQFuawb2xk_KlnrDdoAuAE4HE2wbqXbhU/sendMessage?chat_id=-1001480559009&text={}'.format(
          f"WBGT Reading is {wbgt_reading} and WBGT Code is {wbgt_code}")

      requests.get(base_url)
      time.sleep(3600)

    while True:
      send_message()

  except ValueError:
    print("URL is not working. Please Standby or type manually :)")
    time.sleep(60)
    pass

while now.hour < 20 and now.hour > 6:
  run()
else:
  print("Non working hours")
  time.sleep(300)
