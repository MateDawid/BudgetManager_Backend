from typing import Any

import pytest
from app_users.tests.factories import UserFactory
from django.contrib.auth import get_user_model
from periods.tests.factories import BudgetingPeriodFactory
from pytest_django.lazy_django import skip_if_no_django
from pytest_factoryboy import register
from rest_framework.test import APIClient, APIRequestFactory

register(UserFactory)
register(BudgetingPeriodFactory)


@pytest.fixture(scope='session')
def api_rf() -> APIRequestFactory:
    skip_if_no_django()
    return APIRequestFactory()


@pytest.fixture
def api_client() -> APIClient:
    """API Client for creating request."""
    skip_if_no_django()
    return APIClient()


@pytest.fixture
def base_user() -> Any:
    """User with base permissions."""
    return get_user_model().objects.create_user('user@example.com', 'user123!@#')


@pytest.fixture
def superuser() -> Any:
    """User with admin permissions."""
    return get_user_model().objects.create_superuser('admin@example.com', 'admin123!@#')
