import allure
from URLs import URLs
from data import PREVIOUSLY_CREATED_COURIER, MISSING_ACCOUNT, remove_value
from http_request import HTTPRequests


class TestCourierAuth:
    @allure.title('Проверка успешной авторизации')
    @allure.description('Проверка, что при успешной авторизации возвращается статус 200 и id')
    def test_courier_auth(self):
        r = HTTPRequests.make_post(
            URLs.courier_auth_rout,
            remove_value(PREVIOUSLY_CREATED_COURIER, ["firstName"])
        )
        assert r.status_code == 200 and "id" in r.json()

    @allure.title('Проверка авторизации без логина')
    @allure.description(
        'Проверка, что при авторизации без логина возвращается статус 400 и сообщение "Недостаточно данных для входа"'
    )
    def test_auth_without_param(self):
        r = HTTPRequests.make_post(
            URLs.courier_auth_rout,
            remove_value(PREVIOUSLY_CREATED_COURIER, ["firstName", "login"])
        )
        assert r.status_code == 400 and r.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации незарегистрированным пользователем')
    @allure.description(
        'Проверка, что при попытке авторизации несуществующим пользователем возвращается код 400 и сообщение "Учетная запись не найдена"'
    )
    def test_auth_with_missing_login(self):
        r = HTTPRequests.make_post(URLs.courier_auth_rout, MISSING_ACCOUNT)
        assert r.status_code == 404 and r.json()["message"] == "Учетная запись не найдена"
