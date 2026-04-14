def test_config_loading(mock_config):
    assert mock_config.app_id == "447"
    assert mock_config.api_version == "1"
    assert mock_config.client_id == "jZgZZTwwdJXzBTN8btkssqO6UrbZriha5DX0rxdqj14"
    assert mock_config.client_secret == "vqVUUuChI7UNZ-z0DKdYILr0XY0QbOslD1clDRlBmoAt"
    assert mock_config.auth_url == "https://stoplight.io/mocks/shippingbo/api/256683485/oauth/token"
    assert mock_config.api_url == "https://stoplight.io/mocks/shippingbo/api/757519129"
    assert mock_config.redirect_uri == "urn:ietf:wg:oauth:2.0:oob"
    assert mock_config.max_retries == 3
    assert mock_config.retry_backoff_factor == 0.5
    assert mock_config.timeout == 30
