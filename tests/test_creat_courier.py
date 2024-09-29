import allure
import pytest
from URLs import URLs
from data import generate_courier_data, PREVIOUSLY_CREATED_COURIER
from http_request import HTTPRequests


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверка, что при успешной регистрации курьера возвращается статус 201 и {"ok": True}')
    def test_create_new_courier(self):
        r = HTTPRequests.make_post(URLs.create_courier_rout, generate_courier_data())
        assert r.status_code == 201 and r.json() == {"ok": True}

    @allure.title('Проверка создания курьера без параметров')
    @allure.description(
        'Проверка, что без необходимого параметра возвращается статус 400 и сообщение "Недостаточно данных для создания учетной записи"'
    )
    @pytest.mark.parametrize('param', ['login', 'password'])
    def test_create_new_courier_without_param(self, param):
        r = HTTPRequests.make_post(URLs.create_courier_rout, generate_courier_data(param))
        assert r.status_code == 400 and r.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка создания курьера с логином, который уже есть')
    @allure.description(
        'Проверка, что при создании курьера, который уже есть, возвращается статус 409 и сообщение "Этот логин уже используется. Попробуйте другой."'
    )
    def test_create_courier_with_old_login(self):
        r = HTTPRequests.make_post(URLs.create_courier_rout, PREVIOUSLY_CREATED_COURIER)
        assert r.status_code == 409 and r.json()["message"] == "Этот логин уже используется. Попробуйте другой."
