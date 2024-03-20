import pytest
import os
import json
from src.class_record import JsonStorage  # replace with the actual module name

class TestJsonStorage:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup: create a test json file
        self.test_file = 'data/test.json'
        self.test_data = [
            {
                "name": "Test Vacancy",
                "city": "Test City",
                "salary_from": 1000,
                "salary_to": 2000,
                "currency": "USD",
                "requirement": "Test requirement",
                "url": "http://test.url"
            }
        ]
        os.makedirs('data', exist_ok=True)  # This line creates the 'data' directory if it doesn't exist
        with open(self.test_file, 'w', encoding='utf-8') as f:
            json.dump(self.test_data, f, ensure_ascii=False, indent=4)
        yield
        # Teardown: remove the test json file
        os.remove(self.test_file)

    def test_load_json(self):
        data = JsonStorage.load_json(self.test_file)
        assert data == self.test_data, "Loaded data is not as expected."

    def test_delete_vacancy(self):
        JsonStorage.delete_vacancy("Test Vacancy", self.test_file)
        with open(self.test_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        assert len(data) == 0, "Vacancy was not deleted."

    def test_delete_vacancy_not_found(self):
        with pytest.raises(ValueError):
            JsonStorage.delete_vacancy("Non-existent Vacancy", self.test_file)
