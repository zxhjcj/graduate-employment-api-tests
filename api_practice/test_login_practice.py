import requests

login_url = "http://localhost:8080/api/auth/login"
login_json = {
    "username": "stu001",
    "password": "123456"
}

response = requests.post(login_url, json=login_json)
assert response.status_code == 200
token = response.json()["data"]["token"]
print(response.json())
print(token)
json = response.json()["code"]
assert json == 200
print(json)