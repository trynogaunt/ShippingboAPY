from shippingboapy.client import Client
import os

client = Client(app_id=447, api_version=1, client_id="Q8TGUF0QDZVPlDZzck9kIjCs6aj7efqWoNAcnyiljKc", client_secret="TalkAlPu47s331DxTo-z1btOiww_2luCQ-6w5oc4lX0", redirect_uri="urn:ietf:wg:oauth:2.0:oob")

if os.path.exists("token.txt"):
    with open("token.txt", "r") as f:
        access_token = f.read()
else:
    access_token = None
if os.path.exists("refresh_token.txt"):
    with open("refresh_token.txt", "r") as f:
        refresh_token = f.read()
else:
    refresh_token = None    

client.run(token="3HPylDVw_rszzswmHY8pthBnVgG-fG7qVD5-xwEP2j8", refresh_token=refresh_token, access_token=access_token)

with open("token.txt", "w") as f:
    f.write(client.get_access_token())

with open("refresh_token.txt", "w") as f:
    f.write(client.get_refresh_token())

print(client.order.get_order_by_id(114903442))