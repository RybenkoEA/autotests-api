import httpx

from get_random_email import get_random_email

create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print(f'create_user_response {create_user_response.status_code}')
print(create_user_response_data)

login_user_payload = {
  "email": create_user_payload['email'],
  "password": "string"
}

login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_user_payload)
login_user_response_data = login_user_response.json()
print(f'login_user_response {login_user_response.status_code}')
print(login_user_response_data['token']['accessToken'])

update_user_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
update_user_headers = {
    "Authorization" : f"Bearer {login_user_response_data['token']['accessToken']}"
}

update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
                                   headers=update_user_headers,
                                   json=update_user_payload)
print(f'update_user_response {update_user_response.status_code}')

get_user_response_headers = {
    "Authorization": f"Bearer {login_user_response_data['token']['accessToken']}"
}
get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", headers=get_user_response_headers)

print(f'get_user_response {get_user_response.status_code}')