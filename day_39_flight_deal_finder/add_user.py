import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety"

print("WELCOME TO FLIGHT CLUB.")
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")

verified_ok = True
while verified_ok:
    email = input("enter your email adress:")
    email_2 = input("enter your email adress again: ")
    if email == email_2:
        print("Your account is created!!")
        verified_ok = False
    else:
        verified_ok = True

    config = {
        "user":{
          "FirstName": first_name,
          "LastName": last_name,
          "Email": email
        }
      }

    response = requests.post(url=SHEETY_USERS_ENDPOINT, json=config)
    data = response.json()
    print(data)
