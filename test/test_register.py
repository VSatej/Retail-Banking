import unittest
from app import app
import pytest

def test_register():
    response = app.test_client.get('/register')
    assert response.status_code == 200

