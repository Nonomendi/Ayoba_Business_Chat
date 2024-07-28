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
# If messageId already in table, update column
def get_messages(access_token):
    return json.loads(requests.get("https://api.ayoba.me/v1/business/message", headers={'Authorization': "Bearer " + access_token}).text)


# Send message to numbers/msisdns
def send_message(access_token:str, message:str, *msisdns):
    body = {
        "msisdns": list(msisdns),
        "message": {
            "text": message,
            "type": "text"
        }
    }

    results = json.loads(requests.post("https://api.ayoba.me/v1/business/message", json=body, headers={'Authorization': "Bearer " + access_token}).text)

    for msg in results:
        print("Update DB with 'msisdn':" + msg["msisdn"] + " 'message_id': " + msg["messageId"] + " 'message': " + message)

    return results


# Delete message
def delete_message(access_token:str, message_id:str, *msisdns):
    body = {
        "msisdns": list(msisdns),
        "message": {
            "correlationId":message_id,
            "type": "delete"
        }
    }

    return json.loads(requests.post("https://api.ayoba.me/v1/business/message", json=body, headers={'Authorization': "Bearer " + access_token}).text)


# Needs assess to DB
def message_reaction(messageID:str, reaction:str):
    reactions = {
        "love": "❤️",
        "thumbs-up": "👍",
        "thumbs-down": "👎",
        "laugh": "😂",
        "shock": "🫨",
        "sad": "😥"
    }

