import requests


url = "https://app.shippingbo.com/orders"

querystring = {"limit":"100","sort[created_at]=":"asc"}

headers = {
    "Accept": "application/json",
    "X-API-VERSION": "1",
    "X-API-APP-ID": "447",
    "Authorization": "Bearer 2T4JEx9c-ORVYf5BkjWrmVmqTzE3FUTVQ3CaB_uCBfM"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())