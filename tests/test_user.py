import pytest
from shippingboapy.models.user import User

@pytest.mark.asyncio
async def test_get_user(mock_client):
    user_id = "user_123"
    user = await mock_client.users.get(user_id, headers={"Prefer": "code=200, dynamic=true"})
    
    assert user is not None
    assert isinstance(user, User)
    assert isinstance(user.email, str)
    assert isinstance(user.roles, list)

@pytest.mark.asyncio
async def test_list_users(mock_client):
    users = await mock_client.users.list(headers={"Prefer": "code=200, dynamic=true"})
    
    assert users is not None
    assert isinstance(users, list)
    assert all(isinstance(user, User) for user in users)