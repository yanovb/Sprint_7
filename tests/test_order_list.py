import allure
from URLs import URLs
from http_request import HTTPRequests


class TestOrderList:
    @allure.title('Проверка запроса списка заказов')
    @allure.description(
        'Проверка, что при запросе списка заказов возвращается статус 200 и "orders"'
    )
    def test_get_order_list(self):
        r = HTTPRequests.make_get(URLs.create_order_rout)
        assert r.status_code == 200 and "orders" in r.json()
