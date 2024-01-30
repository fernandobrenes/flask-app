import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    print("Testing / route...")
    assert response.status_code == 200
    assert b'A glorious Bootstrap' in response.data  # Adjust this based on your actual content
    print("Test passed!")

def test_menu1_route(client):
    print("Testing /menu1 route...")
    response = client.get('/menu1')
    assert response.status_code == 200
    assert b'This is the content of Menu1!' in response.data  # Adjust this based on your actual content
    print("Test passed!")

def test_menu2_route(client):
    print("Testing /menu2 route...")
    response = client.get('/menu2')
    assert response.status_code == 200
    assert b'This is the content of Menu2!' in response.data  # Adjust this based on your actual content
    print("Test passed!")
