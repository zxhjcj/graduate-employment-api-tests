import requests
def login():
    login_url = "http://localhost:8080/api/auth/login"
    login_data = {
      "username": "stu001",
      "password": "123456"
    }
    response = requests.post(login_url, json=login_data,timeout=10)
    login_body = response.json()
    assert response.status_code == 200
    assert login_body["code"] == 200
    token = login_body["data"]["token"]
    print(token)
    assert token
    return token
def test_profile():
    token = login()
    profile_url = "http://localhost:8080/api/graduate/profile"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(profile_url, headers=headers,timeout=10)
    print(response.json())
    assert response.status_code == 200
    profile_body = response.json()
    assert profile_body["data"]["realName"]
    assert profile_body["code"] == 200

if __name__ == "__main__":
    test_profile()



