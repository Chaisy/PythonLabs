import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_shedule_crud_view(admin, client):
    client.force_login(admin)

    form_data = {'room': 1}
    response = client.post(reverse('add_shedule'), data=form_data)
    assert response.status_code == 200

    form_data = {'room': 2}
    response = client.post(reverse('edit_shedule', kwargs={'pk': 3}), data=form_data)
    assert response.status_code == 200

    response = client.post(reverse('delete_shedule', kwargs={'pk': 3}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_service_crud_view(admin, client):
    client.force_login(admin)

    form_data = {'price': 50.00}
    response = client.post(reverse('add_service'), data=form_data)
    assert response.status_code == 200

    response = client.post(reverse('delete_service', kwargs={'pk': 1}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_client_crud_view(admin, client):
    client.force_login(admin)

    form_data = {'name': 'Ilina'}
    response = client.post(reverse('add_client'), data=form_data)
    assert response.status_code == 200

    form_data = {'name': 'Lina'}
    response = client.post(reverse('edit_client', kwargs={'pk': 2}), data=form_data)
    assert response.status_code == 200

    response = client.post(reverse('delete_client', kwargs={'pk': 2}))
    assert response.status_code == 302
