# shippingboapy

[![PyPI version](https://img.shields.io/pypi/v/shippingboapy.svg)](https://pypi.org/project/shippingboapy/)
[![Python versions](https://img.shields.io/pypi/pyversions/shippingboapy.svg)](https://pypi.org/project/shippingboapy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An async Python SDK for the [ShippingBo API](https://app.shippingbo.com).

`shippingboapy` is a faithful, low-level wrapper around the ShippingBo REST API. The SDK structure mirrors the actual API endpoints rather than introducing ergonomic abstractions that hide them.
> ⚠️ **Alpha:** this SDK is in early development. The public API may change before v1.0.

- 📦 [PyPI](https://pypi.org/project/shippingboapy/)
- 🐙 [GitHub](https://github.com/trynogaunt/ShippingboAPY)
- 🐛 [Issues](https://github.com/trynogaunt/ShippingboAPY/issues)

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

Or with explicit cleanup:

```python
client = Client(...)
try:
    products = await client.products.list()
finally:
    await client.close()
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
    search=[("user-ref", "eq", "123456")],
    sort=[("updated_at": "asc")],
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

## Orders

### List orders

```python
orders = await client.orders.list(limit=50)
```

### Get an order

```python
order = await client.orders.get(order_id=456)
```

### Create an order

```python
from shippingboapy import OrderCreate, OrderItemCreate

order = await client.orders.create(
    OrderCreate(
        product_source= "product_src_str",
        source="source"
        title="Order Title"
        ...
    )
)
```

---

## Token refresh

Token refresh is handled automatically on `401` responses. After any request, the current tokens are accessible on the client:

```python
client.token.access_token
client.token.refresh_token
```

### Persisting refreshed tokens

To persist tokens after an automatic refresh, register a callback at init:

```python
async def save_tokens(access_token: str, refresh_token: str):
    # Persist to your database, file, or any storage
    await db.save(access_token=access_token, refresh_token=refresh_token)

client = Client(
    access_token="your_access_token",
    refresh_token="your_refresh_token",
    ...,
    on_token_refresh=save_tokens,
)
```

Token storage is intentionally left to the caller, the SDK does not persist tokens itself.

---

## Error handling

The SDK raises typed exceptions for predictable failure modes:

```
ShippingboAPYException
├── AuthenticationError
│   ├── TokenExpiredError
│   └── TokenRefreshError
└── APIRequestError          # exposes .status_code and .message
    ├── BadRequestError      # 400
    ├── UnauthorizedError    # 401
    ├── ForbiddenError       # 403
    ├── NotFoundError        # 404
    ├── RateLimitError       # 429
    ├── ServerError          # 5xx
    └── UnexpectedError      # any other status
```

```python
from shippingboapy import TokenRefreshError, ShippingBoAPIError

try:
    await client.products.get(product_id=123)
except TokenRefreshError:
    # Re-authenticate the user
    ...
except ShippingBoAPIError as e:
    print(e.status_code, e.message)
```

---

## Available Resources

| Resource | Status |
| --- | --- |
| Products | ✅ Available |
| Orders | ✅ Available |
| Addresses | ✅ Available |
| Address Labels | ✅ Available |
| Order Tags | ✅ Available |
| Order Documents | ✅ Available |
| Stock Variations | 🚧 Planned |
| Suppliers | 🚧 Planned |

Missing a resource? Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — see [LICENSE](LICENSE).