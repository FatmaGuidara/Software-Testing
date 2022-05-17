import pytest # compatible with unit test
from app import create_app
from utils.create_db import create_db
import os

# Scope Module = every test create a new database
# Autouse = we dont have to call it
@pytest.fixture(scope="session", autouse=True)
# tmp_path_factory = default  fixture
def create_test_database(tmp_path_factory):
    # Temporary directory
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db(database_filename)
    # Envirement variable
    os.environ["DATABASE_FILENAME"] = str(database_filename)


# Creates a client
# Fixture teb3a lifecycle
# Scope Module = automaticly works in the whole Module (test_app)
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(__name__)
    testing_client = flask_app.test_client(use_cookies=False)
    context = flask_app.app_context()
    context.push()
    # return something but we re still in the function
    yield testing_client
    context.pop()

def test_get_all_todos_initial(test_client):
    # Given
    expected_response = []
    expected_status_code = 200

    # When
    response = test_client.get("/todos")

    # Then
    assert expected_status_code == response.status_code
    assert expected_response == response.json

def test_create_todo (test_client):
    # Given
    request_payload = {
        "name": "Walk the dog"
    }

    expected_body = {
        "id": 1,
        "name": "Walk the dog",
        "status": 0
    }
    expected_status_code = 201

    expected_body_keys = ["id", "name", "status"]

    # When
    response = test_client.post('/todos', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["id"])

def test_create_todo_2 (test_client):
    # Given
    request_payload = {
        "name": "Do the dishes"
    }

    expected_body = {
        "id": 2,
        "name": "Do the dishes",
        "status": 0
    }
    expected_status_code = 201

    expected_body_keys = ["id", "name", "status"]

    # When
    response = test_client.post('/todos', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["id"])

def test_create_todo_3 (test_client):
    # Given
    request_payload = {
        "name": "Clean up"
    }

    expected_body = {
        "id": 3,
        "name": "Clean up",
        "status": 0
    }
    expected_status_code = 201

    expected_body_keys = ["id", "name", "status"]

    # When
    response = test_client.post('/todos', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["id"])

def test_get_all_todos(test_client):
    # Given
    expected_response = [
        {
            "id": 1,
            "name": "Walk the dog",
            "status": 0
        },
        {
            "id": 2,
            "name": "Do the dishes",
            "status": 0
        },
        {
            "id": 3,
            "name": "Clean up",
            "status": 0
        }
    ]
    expected_status_code = 200

    # When
    response = test_client.get("/todos")

    # Then
    assert expected_status_code == response.status_code
    assert expected_response == response.json

def test_delete_existing_todo(test_client):
    # Given
    id_to_delete = 1
    expected_body = {
        "message": "Todo deleted successfully"
    }

    # When
    response = test_client.delete(f'/todos/{id_to_delete}')

    # Then
    assert expected_body == response.json

def test_delete_already_deleted_todo(test_client):
    # Given
    id_to_delete = 1
    expected_body = {
        "message": "Todo not deleted successfully"
    }

    # When
    response = test_client.delete(f'/todos/{id_to_delete}')

    # Then
    assert expected_body == response.json

def test_delete_not_existing_todo(test_client):
    # Given
    id_to_delete = 100
    expected_body = {
        "message": "Todo not deleted successfully"
    }

    # When
    response = test_client.delete(f'/todos/{id_to_delete}')

    # Then
    assert expected_body == response.json

def test_get_todos_after_delete(test_client):
    # Given
    expected_response = [
        {
            "id": 2,
            "name": "Do the dishes",
            "status": 0
        },
        {
            "id": 3,
            "name": "Clean up",
            "status": 0
        }
    ]    
    expected_status_code = 200
    
    # When
    response = test_client.get("/todos")

    # Then
    assert expected_status_code == response.status_code
    assert expected_response == response.json