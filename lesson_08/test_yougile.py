import requests
import pytest

from lesson_08.config import API_TOKEN, BASE_URL

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}


class TestYougileAPI:

    @pytest.fixture(scope="class")
    def create_project(self):
        url = f"{BASE_URL}/projects"
        data = {
            "title": "Test Project"
        }
        response = requests.post(url, json=data, headers=HEADERS)
        assert response.status_code == 201

        yield response.json()
        project_id = response.json()['id']
        # Удаление проекта после тестов
        requests.delete(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)

    def test_create_project(self, create_project):
        assert "id" in create_project

    def test_create_project_missing_name(self):
        url = f"{BASE_URL}/projects"
        data = {
            "description": "No name project"
        }
        response = requests.post(url, json=data, headers=HEADERS)
        assert response.status_code == 400  # Проверка, что возвращается статус 400

    def test_get_projects(self):
        url = f"{BASE_URL}/projects"
        response = requests.get(url, headers=HEADERS)
        assert response.status_code == 200
        response_json = response.json()
        assert "content" in response_json  # Убедитесь, что содержимое присутствует
        assert isinstance(response_json["content"], list)  # Проверьте, что это список

    def test_get_project(self, create_project):
        project_id = create_project['id']
        url = f"{BASE_URL}/projects/{project_id}"
        response = requests.get(url, headers=HEADERS)
        assert response.status_code == 200
        assert response.json()['id'] == project_id

    def test_update_project(self, create_project):
        project_id = create_project['id']
        url = f"{BASE_URL}/projects/{project_id}"
        data = {
            "title": "Updated Project Name"
        }
        response = requests.put(url, json=data, headers=HEADERS)
        assert response.status_code == 200
        assert response.json()['id'] == project_id

    def test_update_project_missing_id(self):
        url = f"{BASE_URL}/projects/99999"  # несуществующий ID
        data = {
            "name": "Updated Project Name"
        }
        response = requests.put(url, json=data, headers=HEADERS)
        assert response.status_code == 400, f"Expected 404, got {response.status_code}. Response: {response.text}"

