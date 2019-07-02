# email stuff
from sendEmail import sendEmail, sendCAMEmail
# scrape stuff
import requests
from bs4 import BeautifulSoup
# timestamp stuff
from datetime import datetime

page = requests.get("https://www.putlockers.me/search/john%20Wick:%20Chapter%203%20-%20Parabellum/")
soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find("span", {"class":"mli-quality"}).string

if result == "CAM":
    print(datetime.now())
    print("CAM")
elif result == "HD":
    print(datetime.now())
    print("HD")
    sendEmail()

