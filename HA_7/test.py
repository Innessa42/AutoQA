import requests


class TestEmployeeApi:
    base_url = "http://5.101.50.27:8000"
    client_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXJyeXBvdHRlciIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0NjQ1ODkxM30.Elw9ExSKMizCP4TJM-DWqzJeSQ7jymkBZuhG_DI7OQs"

    def test_user_create(self):
        data_json = {
            "first_name": "Inna",
            "last_name": "Graur",
            "middle_name": "Dmitrii",
            "company_id": 615,
            "email": "inna@net.net",
            "phone": "+4934215728899",
            "birthdate": "1980-02-18",
            "is_active": True
        }

        response = requests.post(f"{self.base_url}/employee/create", json=data_json)
        assert response.status_code == 200

    def test_user_info(self):
        user_id = 11

        response = requests.get(f"{self.base_url}/employee/info/{user_id}")
        assert response.status_code == 200

    def test_user_update(self):
        data_json = {
            "company_id": 613,
            "email": "inna@net.net",
            "phone": "+4934215728899",
        }

        response = requests.patch(f"{self.base_url}/employee/change/1/?client_token={self.client_token}", json=data_json)
        assert response.status_code == 200

