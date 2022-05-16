import requests
import datetime as dt
import smtplib
import time

my_lat = 25.387270
my_lng = 82.568031
my_email = "gauravpandeypython@gmail.com"
password = 9664932625


def is_iss_overhead():
    con = requests.get(url="http://api.open-notify.org/iss-now.json")
    con.raise_for_status()
    place = con.json()
    iss_latitude = float(place["iss_position"]["latitude"])
    iss_longitude = float(place["iss_position"]["longitude"])

    if my_lat-5 <= iss_latitude < my_lat+5 and my_lng-5 <= iss_longitude <= my_lng+5:
        return True


def is_night():
    parameters = {
        "my_lattitude": my_lat,
        "my_longitude": my_lng,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="vishalpandey9664@gmail.com",
            msg="Subject:Look Up\n\nThe iss is above you in the sky."
        )






