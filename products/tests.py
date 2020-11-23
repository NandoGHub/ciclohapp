from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APIClient

from http import HTTPStatus
from products.models import Product


class OrderTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = None
        self.token = self._get_token()

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token))

        self.product1 = Product.objects.create(
            name="Iphone 12",
            price=185000,
            stock=10
        )

    def _get_token(self):
        data = {
            'username': 'admin',
            'password': 'admin'
        }

        self.user = User.objects.create_user(**data)
        response = self.client.post('/api-auth/token/', data)
        if response.status_code == 200:
            response = response.json()
            return response.get("access")
        return response

    def test_get_token_user(self):
        data = {
            'username': 'admin',
            'password': 'admin'
        }
        response = self.client.post('/api-auth/token/', data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_product_ok(self):

        data = {
            "name": "Iphone 12",
            "price": 25698,
            "stock": 20
        }

        response = self.client.post(
            '/api/products/v1/products/', data, format='json')
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_get_all_products(self):
        response = self.client.get('/api/products/v1/products/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_one_product(self):
        response = self.client.get(
            f'/api/products/v1/products/{self.product1.uuid}/'
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_update_stock_product(self):
        response = self.client.get(
            f'/api/products/v1/products/{self.product1.uuid}/'
        )
        product = response.json()
        self.assertEqual(product.get("stock"), 10)

        data = {"stock": 100}

        response = self.client.patch(
            f'/api/products/v1/products/{self.product1.uuid}/',
            data, format='json'
        )

        product = response.json()
        self.assertEqual(product.get("stock"), 100)

    def test_delet_product(self):
        response = self.client.delete(
            f'/api/products/v1/products/{self.product1.uuid}/'
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)  # 204

        response = self.client.get(
            f'/api/products/v1/products/{self.product1.uuid}/'
        )
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
