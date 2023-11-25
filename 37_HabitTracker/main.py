import requests
from creds import user_params

pixela_endpoint = 'https://pixe.la/v1/users'
graph_creation_endpoint = f'{pixela_endpoint}/{user_create_params["username"]/graphs}'

# 1 create new user account
# res = requests.post(url=pixela_endpoint, json=user_create_params)
# print(res.text)

# 2 Create graph definition
