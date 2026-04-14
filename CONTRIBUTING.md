# Contributing to shippingbo-apy

Thank you for your interest in contributing! This document covers everything you need to know to add resources, fix bugs, or improve the SDK.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Adding a Resource](#adding-a-resource)
- [Models](#models)
- [Integration Tests](#integration-tests)
- [Code Style](#code-style)
- [Known Limitations](#known-limitations)
- [Submitting a Pull Request](#submitting-a-pull-request)

---

## Getting Started

**Requirements:** Python >= 3.10

```bash
git clone https://github.com/tryno/shippingbo-apy.git
cd shippingbo-apy
pip install -e ".[dev]"
pre-commit install
```

---

## Project Structure

```txt
shippingboapy/
├── client.py          # Core Client class, _request(), OAuth handling
├── auth.py            # Token management (get_token, TokenData)
├── config.py          # Settings via pydantic-settings
├── exceptions.py      # ShippingBoError hierarchy
├── models/            # Pydantic v2 models, one file per resource
└── resources/         # Resource classes, one file per resource
tests/
└── ...                # Integration tests against Stoplight mock server
```

---

## Adding a Resource

Each resource lives in two places: a model file and a resource file.

### 1. Create the model - `shippingboapy/models/<resource>.py`

Use Pydantic v2 with these settings on every model:

```python
from pydantic import BaseModel, ConfigDict

class MyResource(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        populate_by_name=True,
    )

    id: int
    name: str | None = None
```

Follow this naming convention:

| Model | Purpose |
| --- | --- |
| `MyResource` | Full response model (GET by id) |
| `MyResourceSummary` | List response model (GET list) |
| `MyResourceCreate` | POST payload |
| `MyResourceUpdateById` | PATCH payload (by id) |
| `MyResourceUpdateByKey` | PATCH payload (by key/value) |

Only create the models you actually need — not all resources have every variant.

### 2. Create the resource - `shippingboapy/resources/<resource>.py`

```python
from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.my_resource import MyResource, MyResourceCreate

if TYPE_CHECKING:
    from shippingboapy.client import Client


class MyResourceResource:
    def __init__(self, client: Client):
        self.client = client

    async def list(self, **kwargs) -> list[MyResource]:
        data = await self.client._request("GET", "my_resources", **kwargs)
        if data is None:
            return []
        return [MyResource(**item) for item in data.get("my_resources", [])]

    async def get(self, resource_id: int, **kwargs) -> MyResource | None:
        data = await self.client._request("GET", f"/my_resources/{resource_id}", **kwargs)
        if data is None:
            return None
        return MyResource(**data)

    async def create(self, payload: MyResourceCreate, **kwargs) -> MyResource | None:
        data = await self.client._request(
            "POST", "my_resources",
            json=payload.model_dump(exclude_none=True),
            **kwargs
        )
        if data is None:
            return None
        return MyResource(**data)
```

Key conventions:
    - Always check `if data is None` before constructing models.
    - Return types must include `| None` when the method can return nothing.
    - Forward references via `TYPE_CHECKING` to avoid circular imports.

### 3. Register on the Client — `shippingboapy/client.py`

```python
from shippingboapy.resources.my_resource import MyResourceResource

class Client:
    def __init__(self, ...):
        ...
        self.my_resources = MyResourceResource(self)
```

---

## Models

- All fields that are optional in the API must be typed `field: Type | None = None`.
- Use `model_dump(exclude_none=True)` for all request payloads to avoid sending null fields.
- Nest sub-models as proper Pydantic models, not raw dicts.
- Never use `dict` as a field type when the structure is known.

---

## Integration Tests

Tests run against the [Stoplight mock server](https://stoplight.io/mocks/shippingbo/api/757519129).

```bash
pytest
```

Place tests in `tests/` following the existing pattern in `tests/conftest.py`.

### Known mock limitations

The Stoplight mock server has known issues on some endpoints. If you encounter a 422 response with `"Request body must be object"` or similar errors that also reproduce directly on the Stoplight UI, this is a mock artifact — **not a bug in your code**.

When this happens:

- Add a comment in your test explaining the mock is broken for that endpoint.
- Do not skip the test silently, mark it with `pytest.mark.xfail` and a reason.

```python
@pytest.mark.xfail(reason="Stoplight mock returns 422 on this endpoint — mock config issue, not an SDK bug")
async def test_update_by_id():
    ...
```

---

## Code Style

This project uses `black`, `isort`, and `mypy`. Pre-commit hooks run them automatically on commit.

To run manually:

```bash
black shippingboapy tests
isort shippingboapy tests
mypy shippingboapy
```

---

## Submitting a Pull Request

1. Fork the repo and create a branch: `git checkout -b feat/order-resource`
2. Follow the conventions above.
3. Add integration tests for any new endpoint.
4. Document broken mock endpoints with `xfail` rather than skipping.
5. Open a PR with a clear description of what resource or fix you're adding.

If you're implementing a resource listed in the ShippingBo API spec but haven't covered all its endpoints yet, that's fine partial implementations are welcome as long as what's there is solid.

---

## Questions?

Open an issue or reach out at [trynogaunt@gmail.com](mailto:trynogaunt@gmail.com)
