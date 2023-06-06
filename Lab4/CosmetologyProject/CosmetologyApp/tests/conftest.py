import os

import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.conf import settings


@pytest.fixture(autouse=True)
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'ATOMIC_REQUESTS': True,
    }


@pytest.fixture
def user():
    user = User.objects.filter(username='Kess').first()
    return user


@pytest.fixture
def admin():
    user = User.objects.filter(username='dari').first()
    return user


@pytest.fixture
def client():
    client = Client()
    return client
