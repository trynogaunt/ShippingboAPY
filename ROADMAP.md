# Roadmap — shippingboapy

Async Python SDK for the ShippingBo API. This document lists in-progress features, planned work, and ideas to explore.

---

## v0.1 — Foundations (in progress)

### Architecture & client

- [x] `Client` with `@classmethod from_auth_code()`
- [x] Async context manager support + explicit `close()`
- [x] Centralized requests through `_request()`
- [x] Centralized auth header and config handling
- [x] Robust URL construction (strip/join to avoid double slashes)
- [x] Resource pattern: instantiated in `Client.__init__`, accessed via `client.<resource>`
- [x] `ShippingBoConfig` kept internal, not exposed to callers

### Authentication

- [x] OAuth authorization code flow
- [x] Automatic token refresh on 401
- [x] Expiration tracking deferred to first 401
- [x] `on_token_refresh` callback for caller-side persistence
- [x] Token persistence out of scope (caller's responsibility)

### Error handling & retries

- [x] Status code → custom exception mapping (`BadRequestError`, `AuthenticationError`, `ForbiddenError`, `NotFoundError`, `ServerError`, etc.)
- [x] Manual retry with exponential backoff (no external dependency)
- [x] Transport error handling (429, 5xx)
- [x] Centralized `_process_response()` using `match/case`

### Resources

- [x] Order: `OrderBase`, `OrderSummary`, `Order`, `OrderCreate`, `OrderItemCreate`
- [x] Filter model with `to_param()` serialization
- [x] `orders.list()` with named parameters (`search`, `tags`, `sort`)
- [ ] Products resource (in progress)
- [ ] Resolve the `ValidationError` caused by an empty string key in the API response

### Models

- [x] Separate response models from request payload models (`Order` vs `OrderCreate`)
- [x] Inheritance based on real field differences (`OrderBase` shared between `Order` and `OrderSummary`)
- [x] Pydantic v2 config: `extra="forbid"`, `validate_assignment=True`, `populate_by_name=True`

### Tests

- [x] Integration tests against the Stoplight mock server
- [x] `pytest` + `pytest-asyncio` in `auto` mode
- [x] `mock_config` fixtures in `conftest.py`
- [x] Workaround for the Stoplight artifact on `GET /products/{id}` (body required)

---

## v0.2 — Ergonomics & API coverage

### File downloads

- [ ] `_download()` method for binary endpoints (shipping labels, exports)
- [ ] Shared `_raw_request()` factored out of `_request()` and `_download()`
- [ ] Support `Accept` header override via kwargs
- [ ] AddressLabels resource with `download()` → bytes

### Automatic pagination

- [ ] `iter_all()` (or `all()`) method on listable resources
- [ ] Async iterator handling offset/max_results under the hood
- [ ] Clean stopping: empty page or partial page
- [ ] Coexistence with `list()` (fine-grained control over a specific page)

### Retry improvements

- [ ] Separate counters for auth retries vs server retries (currently shared)
- [ ] Dedicated `ValidationError` for 422 (distinct from `BadRequestError` for 400)
- [ ] Narrow the `except Exception` around token refresh to typed exceptions
- [ ] Handle `response.text` properly on binary endpoints (content-type check or truncation)

### New resources

- [ ] Products (finalization)
- [ ] Shipments
- [ ] Carriers
- [ ] Stocks / Warehouses

---

## v0.3+ — Advanced features

### HTTP streaming

- [ ] `_stream()` method for large exports (AsyncIterator of bytes)
- [ ] Simplified error handling in streaming mode
- [ ] Document limitations (no graceful auth retry during streaming)

### Rate limiting

- [ ] Read and honor `X-RateLimit-*` headers returned by the API
- [ ] Client-side throttling to avoid 429s
- [ ] Configuration: strict mode vs best-effort

### Webhooks

- [ ] Signature verification helpers
- [ ] Typed parsing of webhook payloads
- [ ] Pydantic models for each event type

### Observability

- [ ] Structured logging hooks (request/response)
- [ ] Optional tracing support (OpenTelemetry?)
- [ ] Basic metrics (request count, retries, token refreshes)

---

## Ideas / To discuss

- **Sync support alongside async** — via a `SyncClient` wrapper around async calls, or a dual API? Value vs. maintenance cost to assess.
- **CLI companion** — a command-line tool to explore the API quickly (debugging, one-shot scripts).
- **Local cache** — optional caching of idempotent GETs (products, carriers…) with invalidation.
- **Batch / bulk operations** — if ShippingBo exposes batch endpoints, surface them with a clear ergonomics.
- **Typed filters** — beyond the generic `Filter`, per-resource typed classes (`OrderFilter`, `ProductFilter`) for autocompletion.
- **Strict vs permissive Pydantic response validation** — dev mode that raises on extra fields vs. prod mode that logs.

---

## Technical notes kept on record

- `httpx` for the async HTTP client
- Pydantic v2 for models
- `pydantic-settings` for config
- `json=payload` required (not `data=payload`) for Stoplight
- Tests run under WSL / Windows Terminal
- No additional dependency for retries (no `tenacity` or equivalent)
