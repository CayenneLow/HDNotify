# email stuff
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
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
message = Mail(
        from_email='john@wick.com',
        to_emails='lowkhyeean@gmail.com',
        subject='John Wick 3 is HD!',
        html_content='<a href="https://www.putlockers.me/stream-4k/john-wick-chapter-3-parabellum-25636/"> Watch Now! </a>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
except Exception as e:
    print(e.message)
