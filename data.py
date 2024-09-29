import random
import string

def generate_courier_data(without_parameter=None):
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    if without_parameter is not None:
        payload.pop(without_parameter)

    return payload

PREVIOUSLY_CREATED_COURIER = {
    "login": "hobbit1",
    "password": "1234",
    "firstName": "frodo"
}

def remove_value(dictionary, arr):
    result = {}
    for key in dictionary.keys():
        if key not in arr:
            result[key] = dictionary[key]
    return result

MISSING_ACCOUNT = {
    "login": "hobbit123",
    "password": "1234"
}

def make_order_data(colors):
    result = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
    if len(colors) < 1:
        result["color"] = colors
    return result
