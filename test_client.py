from shippingboapy.client import Client


app_id = 447
api_version = 1
client_id = 'Q8TGUF0QDZVPlDZzck9kIjCs6aj7efqWoNAcnyiljKc'
client_secret = 'TalkAlPu47s331DxTo-z1btOiww_2luCQ-6w5oc4lX0'
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'


if __name__ == "__main__":
    client = Client(app_id, api_version, client_id, client_secret, redirect_uri)
    client.run("tSeQNbKlMn0HfyEdHVALr3L-sOMhCNjwJ-H4sDtADUc")
