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

    @pytest.mark.django_db
    def test_my_issues(self, client):
        url = reverse("issues:my-issues")
        response = client.get(url)
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_project_list(self, client):
       url = reverse("issues:projects-list")
       response = client.get(url)
       assert response.status_code == 302

    @pytest.mark.django_db
    def test_add_project(self, client):
       url = reverse("issues:add-project")
       response = client.get(url)
       assert response.status_code == 302


class TestViewsLoggedInUsers:
    def test_homepage(self, admin_client):
        url = reverse('issues:dashboard')
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_my_issues(self, admin_client):
        url = reverse("issues:my-issues")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_project_list(self, admin_client):
        url = reverse("issues:projects-list")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_add_project(self, admin_client):
       url = reverse("issues:add-project")
       response = admin_client.get(url)
       assert response.status_code == 200
