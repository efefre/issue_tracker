import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_view_account_login(client):
   url = reverse('account_login')
   response = client.get(url)
   assert response.status_code == 200