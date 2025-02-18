from shippingboapy.client import Client


app_id = 447
api_version = 1
client_id = 'Q8TGUF0QDZVPlDZzck9kIjCs6aj7efqWoNAcnyiljKc'
client_secret = 'TalkAlPu47s331DxTo-z1btOiww_2luCQ-6w5oc4lX0'
redirect_uri = 'https://www.shippingbo.com'


if __name__ == "__main__":
    client = Client(app_id, api_version, client_id, client_secret)
    client.run("fP_lcOYEyDk5GVpR1EnOYmlCzYi3khbV1DsDcjci864")