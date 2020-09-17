import requests

res = requests.get('http://naver.com')


code = res.status_code

print(code)