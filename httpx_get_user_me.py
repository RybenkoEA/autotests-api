import httpx

payload = {
    "email": "user@example.com",
    "password": "string"
}

token_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
print(token_response.json())
print(token_response.status_code)

token_response_json = token_response.json()
access_token = token_response_json['token']['accessToken']
# print(f'accessToken {access_token}')

headers = {
    "Authorization":  "Bearer " + access_token
}

response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(response.json())
print(response.status_code)