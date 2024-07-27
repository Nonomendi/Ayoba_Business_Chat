import requests
import json

sk = "sk_test_b86a969911ebb347fb5f46fd043f973c29b6d4b" # Paystack API secret key


# Function to create a payment request
def request_payment(amount:int, email:str):
    body = {
        "amount":amount, # Payment amount
        "email": email   # Customer email
    }

    # Send request request to create a payment order
    result = json.loads(requests.post("https://api.paystack.co/transaction/initialize", json=body, headers={
        "Authorization": "Bearer " + sk,
        "Content-Type": "application/json"
    }).text)

    if (result["status"]):
        return result["data"]["authorization_url"]  # Return checkout address
    
    return result # Return error json

