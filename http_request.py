import requests


class HTTPRequests:
    @staticmethod
    def make_get(route):
        return requests.get(route)

    @staticmethod
    def make_post(route, body):
        return requests.post(route, body)
