import requests

endpoint = 'http://localhost:8000/api/'

# get_response = requests.post(endpoint, params={'abc': 123}, json={'query': 'hello world'}) # http request
get_response = requests.post(endpoint, json={'title': 'NEW', 'content': None, 'my_discount': None}) # http request
# print(get_response.headers)
# print(get_response.text) # print raw text response
# print(get_response.status_code)
# print(get_response.json())
