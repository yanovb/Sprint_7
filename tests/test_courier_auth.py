from URLs import URLs
from data import PREVIOUSLY_CREATED_COURIER, MISSING_ACCOUNT, remove_value
from http_request import HTTPRequests


class TestCourierAuth:
    def test_courier_auth(self):
        r = HTTPRequests.make_post(
            URLs.courier_auth_rout,
            remove_value(PREVIOUSLY_CREATED_COURIER, ["firstName"])
        )
        assert r.status_code == 200 and "id" in r.json()

    def test_auth_without_param(self):
        r = HTTPRequests.make_post(
            URLs.courier_auth_rout,
            remove_value(PREVIOUSLY_CREATED_COURIER, ["firstName", "login"])
        )
        assert r.status_code == 400 and r.json()["message"] == "Недостаточно данных для входа"

    def test_auth_with_missing_login(self):
        r = HTTPRequests.make_post(URLs.courier_auth_rout, MISSING_ACCOUNT)
        assert r.status_code == 404 and r.json()["message"] == "Учетная запись не найдена"
