import requests
from django.forms.models import model_to_dict


endpoint = 'http://localhost:8000/api/products/1/'

get_response = requests.get(endpoint)
print(get_response)