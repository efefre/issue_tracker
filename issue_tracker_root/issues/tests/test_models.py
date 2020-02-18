import pytest
from ..models import Project


@pytest.mark.django_db
def test_create_project():
    new_project = Project.objects.create(name='First project', status='success')
    new_project.save()
    assert Project.objects.count() == 1
    assert new_project.status == 'success'