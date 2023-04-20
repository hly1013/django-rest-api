import requests
from django.forms.models import model_to_dict


endpoint = 'http://localhost:8000/api/products/11231243452423462456345765476/'

get_response = requests.get(endpoint)
print(get_response)