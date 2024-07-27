import requests
import json

secret_key = "sk_test_b86a969911ebb347fb5f46fd043f973c29b6d4b9" # Paystack API secret key


# Function to create a payment request
#
# Return tuple of payment link and reference
def request_payment(amount:int, email:str):
    body = {
        "amount":amount, # Payment amount
        "email": email   # Customer email
    }

    # Send request request to create a payment order
    result = json.loads(requests.post("https://api.paystack.co/transaction/initialize", json=body, headers={
        "Authorization": "Bearer " + secret_key,
        "Content-Type": "application/json"
    }).text)

    if (result["status"]):
        return (result["data"]["authorization_url"], result["data"]["reference"])  # Return checkout address
    return result # Return error json


# Verify payments
#
# returns success, failed, abandoned
def verify_payment(payment_ref:str):
    result = json.loads(requests.get("https://api.paystack.co/transaction/verify/" + payment_ref, headers={
        "Authorization": "Bearer " + secret_key,
        "Content-Type": "application/json"
    }).text)

    data = result["data"]
    return data["status"]