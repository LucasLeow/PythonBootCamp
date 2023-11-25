import requests
from datetime import datetime
from creds import user_create_params, headers

pixela_endpoint = 'https://pixe.la/v1/users'
graph_creation_endpoint = f"{pixela_endpoint}/{user_create_params['username']}/graphs"
graph_post_endpoint = f"{pixela_endpoint}/{user_create_params['username']}/graphs/graph1"

# == 1 create new user account ==

# res = requests.post(url=pixela_endpoint, json=user_create_params)
# print(res.text)

# == 2 Create graph definition ==
'''
graph req body: id | name | unit | type | color
id - unique id for graph
name - name of graph
unit - unit of measure for activity
type -  measure type ("float" or "int")
color - shibafu(g), momiji(r), sora(blue), ichou(y), ajisai(p), kuro(blk)
graph access: https://pixe.la/v1/users/lucasl96/graphs/graph1.html
'''

# graph_config = {
#     "id": "graph1",
#     "name": "coding",
#     "unit": "km",
#     "type": "float",
#     "color": "sora"
# }

# res = requests.post(
#     url=graph_creation_endpoint,
#     json=graph_config,
#     headers=headers
# )

# print(res.text)

# == 3 Posting value to graph ==
# today = datetime.today().strftime('%Y%m%d')

# graph_post_config = {
#     "date": today,
#     "quantity": "5"
# }

# res = requests.post(
#     url=graph_post_endpoint,
#     json=graph_post_config,
#     headers=headers
# )
