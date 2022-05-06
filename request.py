import requests

r = requests.post('http://127.0.0.1:8000/', data={"question_num": 1})

print(r.text)

