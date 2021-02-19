from django.test import RequestFactory
from mixer.backend.django import mixer
import pytest
from .. import views
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestProductView:
    def test_detailview(self):
        obj = mixer.blend("catalog.Product")
        path = reverse("catalog:product_detail", kwargs={"slug": obj.slug})
        request = RequestFactory().get(path)
        response = views.ProductDetail.as_view()(request, slug=obj.slug)
        assert response.status_code == 200, "Should return 200"


class TestCategoryView:
    def test_detailview(self):
        obj = mixer.blend("catalog.Category")
        path = reverse("catalog:category_detail", kwargs={"slug": obj.slug})
        request = RequestFactory().get(path)
        response = views.CategoryDetail.as_view()(request, slug=obj.slug)
        assert response.status_code == 200, "Should return 200"


class TestProductList:
    def test_product_list(self):
        path = reverse("catalog:product_list")
        request = RequestFactory().get(path)
        response = views.ProductList.as_view()(request)
        assert response.status_code == 200, "Should return 200"
