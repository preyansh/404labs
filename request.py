import requests

response = requests.get('https://raw.githubusercontent.com/preyansh/404labs/master/request.py')
print (response.text)