import requests
import pandas as pd
import time
from keepalive import keep_alive
from datetime import datetime
from pytz import timezone

def run():

  try:

    def send_message():
      tz = timezone("Asia/Singapore")
      now = datetime.now(tz)

      #Firstly,   
  
     
      tables = pd.read_html("https://www.wbgt.sg/allstations") #The WBGT Bot will open up the wbgt website (https://www.wbgt.sg) and scrape                                                              the data under the section “all stations” which shows the results of the WBGT                                                               for all areas in Singapore in a table format.
      tables[0].to_csv("my_file.csv")
      data = pd.read_csv("my_file.csv") #It converts the table which is in HTML format to CSV format for easier reading of the data.

      # In the following 4 lines of code, the WBGT Bot identifies the correct location (Old Chua Chu Kang Road) in the table and retrieves the WBGT Code and Reading that coresponds to the given location. 
      location = "Old Choa Chu Kang Road"
      row_of_location = data[data.Location == location] 

      wbgt_code = row_of_location["WBGT Code"].item()
      wbgt_reading = row_of_location["WBGT Reading"].item()
      
      if wbgt_reading >= 35:
        base_url = 'https://api.telegram.org/bot6087536906:AAHQFuawb2xk_KlnrDdoAuAE4HE2wbqXbhU/sendMessage?chat_id=-1001626786883&text={}'.format(
          f"WBGT Reading is {wbgt_reading}, no strenous training") #One initial roadblock I faced was that the WBGT Code was still being reflected as “Black” in the WBGT Website even when the WBGT Reading is above 34. I had to adapt and be innovative, adapting the code such instead of sending out the text message as WBGT Code “Black”, it sends out a message indicating that there should be no strenous training when the WBGT Code is 35 and above.

      else:
        base_url = 'https://api.telegram.org/bot6087536906:AAHQFuawb2xk_KlnrDdoAuAE4HE2wbqXbhU/sendMessage?chat_id=-1001626786883&text={}'.format(
        f"WBGT Reading is {wbgt_reading} and WBGT Code is {wbgt_code}") #Using the inputs (WBGT Code and WBGT Reading) obtained, the WBGT Bot will craft a text message: “WBGT Reading is {wbgt_reading} and WBGT Code is {wbgt_code}” that would be sent to the TAB Met Channel in telegram.                                                     

      if now.hour < 20 and now.hour > 6: #Automatically pageout the message only between the time given (0700H to 1900H)
        requests.get(base_url) #The Python code carries out the sending of message by opening a URL backend which contains an API link with                                 information such as the WBGT Bot Token as well as the TAB MET Channel ID to ensure that the correct bot is                                  being used to send the message to the correct channel.
        print("message sent!")
        time.sleep(3600) #Time delay of 3600s (60 mins) between each message sent 
        
      else:
        print("Non working hours") #Between 1900H to 0700H (the next day), informs users every 300s (5mins) that the WBGT Bot will not send any messages to the TAB MET Channel as it is not between the specified working hours (0700H to 1900H)
        time.sleep(300)
        
      keep_alive()

    while True:
      send_message()

  except ValueError:
    print("URL is not working. Please Standby or type manually :)") #Informs users in the unlikely scenario that the WBGT Website URL is down
    time.sleep(60)
    pass

while True:
  run()

