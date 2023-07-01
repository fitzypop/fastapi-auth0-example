import pytest


@pytest.fixture
def mock_fastapi_auth0(mocker):
    auth0 = mocker.patch("fastapi_auth0.auth.Auth0")
    auth0.implicit_scheme.return_value = None
    auth0.get_user.return_value = None
    return auth0
