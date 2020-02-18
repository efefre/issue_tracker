import pytest
from ..models import CustomUser


@pytest.mark.django_db
def test_user_create():
    CustomUser.objects.create_user(
        username="johnt", first_name="John", last_name="Test", email="test@test.com"
    )
    assert CustomUser.objects.count() == 1
