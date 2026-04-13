# Shippingboapy

An async Python SDK for the [ShippingBo API](https://app.shippingbo.com).

## Installation

```bash
pip install shippingboapy
```

## Requirements

- Python 3.10+

## Usage

### Initialization

If you already have an access token and refresh token:

```python
from shippingboapy import Client

client = Client(
    access_token="your_access_token",
    refresh_token="your_refresh_token",
    app_id="your_app_id",
    api_version="your_api_version",
    client_id="your_client_id",
    client_secret="your_client_secret",
)
```

### OAuth — first-time authentication

If you don't have tokens yet, use the OAuth flow with an authorization code:

```python
from shippingboapy import Client

client = await Client.from_auth_code(
    auth_code="your_auth_code",
    app_id="your_app_id",
    api_version="your_api_version",
    client_id="your_client_id",
    client_secret="your_client_secret",
    redirect_uri="your_redirect_uri",
)
```

### Context manager

```python
async with Client(...) as client:
    products = await client.products.list()
```

### Configuration

```python
client.set_config(
    timeout=30,
    max_retries=3,
    retry_backoff_factor=0.5,
    api_url="https://app.shippingbo.com",
)
```

---

## Products

### List products

```python
products = await client.products.list()
```

With filters:

```python
products = await client.products.list(
    limit=50,
    offset=0,
    is_pack=False,
    search={"search[user_ref__eq]": "MY-REF"},
    sort={"updated_at": "asc"},
)
```

### Get a product

```python
product = await client.products.get(product_id=123)
```

### Create a product

```python
from shippingboapy import ProductCreate

product = await client.products.create(
    ProductCreate(
        user_ref="MY-REF-001",
        title="My Product",
        weight=500,
        width=200,
        length=300,
        height=100,
    )
)
```

---

## Token refresh

Token refresh is handled automatically on `401` responses. If you need to persist the new tokens, you can access them after any request:

```python
client.token.access_token
client.token.refresh_token
```

---

## License

MIT
