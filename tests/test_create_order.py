import allure
import pytest
from URLs import URLs
from data import make_order_data
from http_request import HTTPRequests


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа')
    @allure.description(
        'Проверка, что при создании успешного заказа возвращается статус 201 и тело ответа содержит track'
    )
    @pytest.mark.parametrize(
        'colors',
        [
            ["BLACK", "GREY"],
            ["GREY"],
            ["BLACK"],
            []
        ]
    )
    def test_create_order(self, colors):
        r = HTTPRequests.make_post(
            URLs.create_order_rout,
            make_order_data(colors)
        )
        assert r.status_code == 201 and "track" in r.json()
