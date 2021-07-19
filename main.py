from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = "sanjanavarghese12345@gmail.com"
MY_PASSWORD = "9447978843"
AMAZON_HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "91.0.4472.114 Safari/537.36"
}
AMAZON_URL = "https://www.amazon.com/Headphones-Earphones-Microphone-Cancellation-Compatible/dp/B093Z37JHR/ref=sr_1_1_sspa?dchild=1&keywords=earphones&qid=1624705551&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE1UEswRDU1MlNSNEkmZW5jcnlwdGVkSWQ9QTAwMjMyODZKOURWMkg4RTBGSUUmZW5jcnlwdGVkQWRJZD1BMDY5NDUxNzIxTE9TVExVOEVBNjkmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
response = requests.get(AMAZON_URL, headers=AMAZON_HEADERS)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "html.parser")
price = soup.find(name="span", class_="_p13n-desktop-sims-fbt_price_p13n-sc-price__bCZQt").getText()
actual_price = float(price.split("$")[1])
print(actual_price)

if actual_price < 10.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="sanjanavarghese47120@gmail.com",
            msg=f"Subject:Amazon Price Alert!\nEarbuds Headphones Wired Stereo Sound Earphones for "
                f"iPhone with Microphone and Volume Control Active Noise Cancellation Compatible with "
                f"iPhone 8 7 Plus 12 XR,is\n now ${actual_price},\n {AMAZON_URL}"
        )
