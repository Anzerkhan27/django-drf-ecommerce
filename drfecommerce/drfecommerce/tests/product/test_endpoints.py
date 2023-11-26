import pytest

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:
    
    endpoint = "/api/category/"

    def test_category_get(self, category_factory, api_client):
        category_factory()

        response = api_client().get(self.endpoint)
        assert response.status_code == 200

class TestBrandEndpoints:
    pass

class TestProductEndpoints:
    pass
