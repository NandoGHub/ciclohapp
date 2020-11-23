
from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APIClient

from http import HTTPStatus
from .models import Order, OrderDetail
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

        self.product2 = Product.objects.create(
            name="Notebook HP",
            price=72000,
            stock=5
        )

        self.order = Order.objects.create()
        self.order_detail_1 = OrderDetail.objects.create(
            order=self.order,
            cuantity=1,
            product=self.product1
        )
        self.order_detail_2 = OrderDetail.objects.create(
            order=self.order,
            cuantity=2,
            product=self.product2
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

    def test_get_all_orders(self):
        response = self.client.get('/api/orders/v1/orders/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_order_ok(self):

        data = {
            "order_details": [
                {
                    "cuantity": 1,
                    "product": f"{self.product1.uuid}"
                },
                {
                    "cuantity": 1,
                    "product": f"{self.product2.uuid}"
                }
            ]
        }

        response = self.client.post(
            '/api/orders/v1/orders/', data, format='json')
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_create_order_cuantity_zero(self):

        data = {
            "order_details": [
                {
                    "cuantity": 0,
                    "product": f"{self.product1.uuid}"
                },
                {
                    "cuantity": 1,
                    "product": f"{self.product2.uuid}"
                }
            ]
        }

        response = self.client.post(
            '/api/orders/v1/orders/', data, format='json')
        response = response.json()
        self.assertEqual(
            response.get("error"), "La cantidad debe ser mayor que cero.")

    def test_create_order_repeat_products(self):

        data = {
            "order_details": [
                {
                    "cuantity": 1,
                    "product": f"{self.product1.uuid}"
                },
                {
                    "cuantity": 1,
                    "product": f"{self.product1.uuid}"
                }
            ]
        }

        response = self.client.post(
            '/api/orders/v1/orders/', data, format='json')
        response = response.json()
        self.assertEqual(
            response.get("error"), "No puede haber productos repetidos.")

    def test_delet_order(self):
        response = self.client.delete(
            f'/api/orders/v1/orders/{self.order.uuid}/'
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)  # 204

        response = self.client.get(
            f'/api/orders/v1/orders/{self.order.uuid}/'
        )
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
