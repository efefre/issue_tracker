import pytest

from django.urls import reverse


class TestViewsWithoutLogin:
    @pytest.mark.django_db
    def test_view_account_login(self, client):
        url = reverse("account_login")

        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_homepage(self, client):
        url = reverse("issues:dashboard")
        response = client.get(url)
        assert response.status_code == 302


class TestViewsLoggedInUsers:
   def test_homepage(self, admin_client):
      url = reverse('issues:dashboard')
      response = admin_client.get(url)
      assert response.status_code == 200