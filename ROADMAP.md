# Roadmap — shippingboapy

SDK Python async pour l'API ShippingBo. Ce document liste les fonctionnalités en cours, prévues, et les idées à explorer.

---

## ✅ v0.1 — Fondations (en cours)

### Architecture & client
- [x] `Client` avec `@classmethod from_auth_code()`
- [x] Support async context manager + `close()` explicite
- [x] Centralisation des requêtes dans `_request()`
- [x] Gestion des headers auth et config centralisée
- [x] Construction d'URL robuste (strip/join pour éviter les doubles slashes)
- [x] Pattern resource : instanciées dans `Client.__init__`, accessibles via `client.<resource>`
- [x] `ShippingBoConfig` interne, non exposé aux appelants

### Authentification
- [x] OAuth authorization code flow
- [x] Refresh token automatique sur 401
- [x] Tracking d'expiration différé au premier 401
- [x] Callback `on_token_refresh` pour persistance côté appelant
- [x] Persistance des tokens out-of-scope (responsabilité de l'appelant)

### Gestion d'erreurs & retry
- [x] Mapping status codes → exceptions custom (`BadRequestError`, `AuthenticationError`, `ForbiddenError`, `NotFoundError`, `ServerError`, etc.)
- [x] Retry manuel avec exponential backoff (pas de dépendance externe)
- [x] Gestion des erreurs transport (429, 5xx)
- [x] `_process_response()` centralisé avec `match/case`

### Resources
- [x] Order : `OrderBase`, `OrderSummary`, `Order`, `OrderCreate`, `OrderItemCreate`
- [x] Filter model avec `to_param()` serialization
- [x] `orders.list()` avec paramètres nommés (`search`, `tags`, `sort`)
- [ ] Resource Products (en cours)
- [ ] Résoudre le `ValidationError` lié à une clé vide dans la réponse API

### Modèles
- [x] Séparation response models / request payload models (`Order` vs `OrderCreate`)
- [x] Héritage basé sur différences réelles (`OrderBase` partagé entre `Order` et `OrderSummary`)
- [x] Config Pydantic v2 : `extra="forbid"`, `validate_assignment=True`, `populate_by_name=True`

### Tests
- [x] Tests d'intégration contre Stoplight mock server
- [x] `pytest` + `pytest-asyncio` en mode `auto`
- [x] Fixtures `mock_config` dans `conftest.py`
- [x] Contournement de l'artefact Stoplight sur `GET /products/{id}` (body requis)

---

## 🚧 v0.2 — Ergonomie & couverture API

### Téléchargement de fichiers
- [ ] Méthode `_download()` pour les endpoints binaires (étiquettes, exports)
- [ ] Factorisation `_raw_request()` partagée entre `_request()` et `_download()`
- [ ] Support header `Accept` override par kwargs
- [ ] Resource AddressLabels avec `download()` → bytes

### Pagination automatique
- [ ] Méthode `iter_all()` (ou `all()`) sur les resources listables
- [ ] Async iterator qui gère offset/max_results sous le capot
- [ ] Arrêt propre : page vide ou page partielle
- [ ] Cohabitation avec `list()` (contrôle fin d'une page précise)

### Amélioration du retry
- [ ] Séparer les compteurs de retry auth et retry serveur (actuellement partagés)
- [ ] `ValidationError` distincte pour 422 (vs `BadRequestError` pour 400)
- [ ] Restreindre le `except Exception` autour du refresh token à des exceptions typées
- [ ] Gérer proprement `response.text` sur les endpoints binaires (content-type check ou troncature)

### Nouvelles resources
- [ ] Products (finalisation)
- [ ] Shipments
- [ ] Carriers
- [ ] Stocks / Warehouses

---

## 🔮 v0.3+ — Fonctionnalités avancées

### Streaming HTTP
- [ ] Méthode `_stream()` pour les gros exports (AsyncIterator de bytes)
- [ ] Gestion simplifiée des erreurs en mode stream
- [ ] Documentation des limitations (pas de retry auth gracieux pendant le stream)

### Rate limiting
- [ ] Lecture et respect des headers `X-RateLimit-*` renvoyés par l'API
- [ ] Throttling côté client pour éviter les 429
- [ ] Configuration : mode strict vs best-effort

### Webhooks
- [ ] Helpers de vérification de signature
- [ ] Parsing typé des payloads webhook
- [ ] Modèles Pydantic pour chaque type d'événement

### Observabilité
- [ ] Hooks de logging structurés (request/response)
- [ ] Support tracing (OpenTelemetry ?) optionnel
- [ ] Métriques de base (nombre de requêtes, retries, refresh tokens)

---

## 💡 Ideas / À discuter

- **Support sync en plus de l'async** — via un wrapper `SyncClient` qui enveloppe les appels async, ou double API ? Valeur vs coût de maintenance à évaluer.
- **CLI companion** — outil en ligne de commande pour explorer l'API rapidement (debug, scripts one-shot).
- **Cache local** — mise en cache optionnelle des GET idempotents (produits, carriers...) avec invalidation.
- **Batch / bulk operations** — si ShippingBo expose des endpoints batch, les exposer avec une ergonomie claire.
- **Typed filters** — au-delà du `Filter` générique, des classes typées par resource (`OrderFilter`, `ProductFilter`) pour l'auto-complétion.
- **Validation de la réponse Pydantic stricte vs permissive** — mode dev qui lève sur extra fields vs mode prod qui log.

---

## 📌 Notes techniques retenues

- `httpx` pour le client HTTP async
- Pydantic v2 pour les modèles
- `pydantic-settings` pour la config
- `json=payload` requis (pas `data=payload`) pour Stoplight
- Tests en WSL / Windows Terminal
- Pas de dépendance additionnelle pour le retry (pas de `tenacity` ou autre)