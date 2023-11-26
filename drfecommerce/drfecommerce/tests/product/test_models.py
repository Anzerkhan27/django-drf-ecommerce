import pytest


pytestmark = pytest.mark.django_db
class TestCategoryModel:
    def test_str_method(self, category_factory):
        #Arrange
        #Act
        x = category_factory()
        # Assert
        assert x.__str__() == "test_category"


class TestBrandyModel:
    def test_str_method(self, brand_factory):
        #Arrange
        #Act
        x = brand_factory()
        # Assert
        assert x.__str__() == "test_brand"

class TestBrandyModel:
    def test_str_method(self, brand_factory):
        #Arrange
        #Act
        x = brand_factory()
        # Assert
        assert x.__str__() == "test_brand"        
        


class TestProductModel:
    def test_str_method(self, product_factory):
        #Arrange
        #Act
        x = product_factory()
        # Assert
        assert x.__str__() == "test_product"             