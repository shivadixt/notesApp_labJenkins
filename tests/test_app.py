import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_add_note(client):
    response = client.post('/add', data={'title': 'Test', 'content': 'Testing content'})
    assert response.status_code == 302  # redirect after add
    response = client.get('/')
    assert b'Test' in response.data


def test_delete_note(client):
    client.post('/add', data={'title': 'ToDelete', 'content': 'Delete me'})
    response = client.get('/')
    assert b'ToDelete' in response.data
