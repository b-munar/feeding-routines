import pytest
import json
from unittest.mock import patch
from functools import wraps

def mock_authorization(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            kwargs["user"] = {"id" : "9027aff6-545e-4a1c-bbf7-9c09f6ae595c",
                               "role": 2}
            return func(*args, **kwargs)
    return decorated

patch('src.utils.authorization.authorization', mock_authorization).start()

from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_request_ping(client):
    response = client.get("/feeding-routines/ping")
    assert response.status_code == 200
    assert b"pong" in response.data
    
def test_request_post(client):
    url = "/feeding-routines"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "meals_per_day": 3,
    "alergies": "Ninguna",
    "health_issues": "Arritmia",
    "time_to_cook": 10
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201


def test_request_get(client):
    url = "/feeding-routines"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "meals_per_day": 3,
    "alergies": "Ninguna",
    "health_issues": "Arritmia",
    "time_to_cook": 10
    }
    client.post(url, data=json.dumps(data), headers=headers)
    response = client.get("/feeding-routines")
    assert response.status_code == 200
    assert b"profiles" in response.data

def test_request_post_plan(client):
    url = "/feeding-routines/foodplan"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "user": "29a3ad78-6d3c-46e3-9c42-857ca3ec5220",
    "days": [
        {
            "day": "Wednesday",
            "meals": {
                "breakfast": "pollo con papas",
                "lunch": "arrozcon huevo",
                "dinner": "arepacon queso"
            }
        }
    ]
}
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201
    
def test_request_get(client):
    url = "/feeding-routines/foodplan"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "user": "29a3ad78-6d3c-46e3-9c42-857ca3ec5220",
    "days": [
        {
            "day": "Wednesday",
            "meals": {
                "breakfast": "pollo con papas",
                "lunch": "arrozcon huevo",
                "dinner": "arepacon queso"
            }
        }
    ]
}
    client.post(url, data=json.dumps(data), headers=headers)
    response = client.get("/feeding-routines/foodplan")
    assert response.status_code == 200
    assert b"plans" in response.data


def test_request_post_400(client):
    url = "/feeding-routines/foodplan"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "user": "29a3ad78-6d3c-46e3-9c42-857ca3ec5220",
    "feed_plan": [
        {
            "day": "Wednesday",
            "meals": {
                "breakfast": "pollo con papas",
                "lunch": "arrozcon huevo",
                "dinner": "arepacon queso"
            }
        }
    ]
}
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400

