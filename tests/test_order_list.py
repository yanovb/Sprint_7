from URLs import URLs
from http_request import HTTPRequests


class TestOrderList:
    def test_get_order_list(self):
        r = HTTPRequests.make_get(URLs.create_order_rout)
        assert r.status_code == 200 and "orders" in r.json()
