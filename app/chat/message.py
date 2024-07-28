import requests
import json

username = "b54ba9dca84def801bf0fe59602c82ef75d7f4ee"
password = "zIAq9U4UQ04Md5bT7hSiyjWbrcIq6hO"

def login():
    body = {
        "username": "b54ba9dca84def801bf0fe59602c82ef75d7f4ee",
        "password": "zIAq9U4UQ04Md5bT7hSiyjWbrcIq6hO"
    }

    return json.loads(requests.post("https://api.ayoba.me/v2/login", json=body).text)["access_token"]


# To-Do, save the mesages to the database
def get_messages(access_token):
    return json.loads(requests.get("https://api.ayoba.me/v1/business/message", headers={'Authorization': "Bearer " + access_token}).text)


def send_message(access_token:str, message:str, *msisdns):
    body = {
        "msisdns": list(msisdns),
        "message": {
            "text": message,
            "type": "text"
        }
    }

    return json.loads(requests.post("https://api.ayoba.me/v1/business/message", json=body, headers={'Authorization': "Bearer " + access_token}).text)



access_token = login()
print(send_message(access_token, "Mock message", "+27838430298"))