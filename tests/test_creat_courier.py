import pytest
from URLs import URLs
from data import generate_courier_data, PREVIOUSLY_CREATED_COURIER
from http_request import HTTPRequests


class TestCreateCourier:
    def test_create_new_courier(self):
        r = HTTPRequests.make_post(URLs.create_courier_rout, generate_courier_data())
        assert r.status_code == 201 and r.json() == {"ok": True}

    @pytest.mark.parametrize('param', ['login', 'password'])
    def test_create_new_courier_without_param(self, param):
        r = HTTPRequests.make_post(URLs.create_courier_rout, generate_courier_data(param))
        assert r.status_code == 400 and r.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_with_old_login(self):
        r = HTTPRequests.make_post(URLs.create_courier_rout, PREVIOUSLY_CREATED_COURIER)
        assert r.status_code == 409 and r.json()["message"] == "Этот логин уже используется. Попробуйте другой."
