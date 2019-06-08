# email stuff
from sendEmail import sendEmail
# scrape stuff
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.putlockers.me/search/john%20Wick:%20Chapter%203%20-%20Parabellum/")
soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find("span", {"class":"mli-quality"}).string

if result == "CAM":
    print("CAM")
elif result == "HD":
    print("HD")
    sendEmail()

