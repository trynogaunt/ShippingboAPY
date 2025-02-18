# Shippingboapy

Shippingboapy is a Python wrapper for the Shippingbo API. It allows you to easily interact with the Shippingbo API to manage orders, products, and more.

## Installation

Install the package via pip:

```bash
pip install shippingboapy
```

## Usage

### Authentification

Create an instance of the `Client` class and authenticate using an authorization code.

```python
from shippingboapy.client import Client

# Remplacez les valeurs par vos informations réelles
app_id = 123
api_version = 1
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'your_redirect_uri'
authorization_code = 'your_authorization_code'

client = Client(app_id, api_version, client_id, client_secret, redirect_uri)
client.run(authorization_code)

if client.is_authenticated():
    print("Authentification réussie")
else:
    print("Échec de l'authentification")
```

## Orders

```python
client = Client(app_id, api_version, client_id, client_secret, redirect_uri)
client.run(authorization_code)

print(client.order.get_order_by_id(123456))
```

## Products

```python
client = Client(app_id, api_version, client_id, client_secret, redirect_uri)
response = client.run(authorization_code)

print(client.product.get_product_by_id(123456))
```

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](vscode-file://vscode-app/c:/Users/Quentin/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) file for details.
