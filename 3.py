import requests

# GET запрос для получения информации о заказе по ID
order_id = 12345
url = f"https://petstore.swagger.io/v2/store/order/{order_id}"
response = requests.get(url)
print(response.json())


# POST запрос для создания нового заказа
order_data = {
    "id": 12345,
    "petId": 54321,
    "quantity": 1,
    "shipDate": "2023-06-09T12:00:00Z",
    "status": "placed",
    "complete": True
}
url = "https://petstore.swagger.io/v2/store/order"
response = requests.post(url, json=order_data)
print(response.json())


# DELETE запрос для удаления заказа по ID
order_id = 12345
url = f"https://petstore.swagger.io/v2/store/order/{order_id}"
response = requests.delete(url)
print(response.status_code)


# PUT запрос для обновления информации о пользователе
user_id = 12345
updated_user_data = {
    "id": user_id,
    "username": "new_username",
    "firstName": "John",
    "lastName": "Doe",
    "email": "johndoe@example.com",
    "password": "new_password",
    "phone": "1234567890",
    "userStatus": 1
}
url = f"https://petstore.swagger.io/v2/user/{user_id}"
response = requests.put(url, json=updated_user_data)
print(response.json())
