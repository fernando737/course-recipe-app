"""
Test for the health check API.
"""
from contextlib import AbstractContextManager
from typing import Any
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckAPITest(TestCase):
    """Test the health check API."""

    def test_health_check(self):
        """Test the health check API."""
        url = reverse('health-check')
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'status': 'ok'})