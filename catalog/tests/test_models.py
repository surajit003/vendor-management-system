import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestCatalogModel:
    def test_category(self):
        obj = mixer.blend("catalog.Category")
        assert obj.pk == 1, "Should create a Category instance"
        assert str(obj) == "{}".format(obj.name)

    def test_productimage(self):
        obj = mixer.blend("catalog.ProductImage")
        assert obj.pk == 1, "Should create ProductImage instance"
        assert str(obj) == "{} {}".format(obj.product.name, obj.img_category)

    def test_product(self):
        obj = mixer.blend("catalog.Product")
        assert obj.pk == 1, "Should create Product instance"
        assert str(obj) == "{}".format(obj.name)

    def test_get_absolute_url_for_category(self):
        obj = mixer.blend("catalog.Category")
        result = obj.get_absolute_url()
        assert result == "/ecommerce/catalog/category/{}".format(obj.slug)

    def test_get_absolute_url_for_product(self):
        obj = mixer.blend("catalog.Product")
        result = obj.get_absolute_url()
        assert result == "/ecommerce/catalog/product/{}".format(obj.slug)

    def test_sale_price_with_old_price_gt_price(self):
        obj = mixer.blend("catalog.Product", price=100, old_price=200)
        assert obj.sale_price() == obj.price

    def test_sale_price_with_old_price_lt_price(self):
        obj = mixer.blend("catalog.Product", price=300, old_price=200)
        assert obj.sale_price() == obj.old_price
