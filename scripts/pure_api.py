import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    print(type(data))
    print(type(json.dumps(data)))

    for obj in data :
        print(obj['id'])
        if(obj['id'] == 1):
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print("this - ", dir(r2))
            print(r2.json())

def create_update():
    new_data = {
        'user' : 1,
        'content' : "Another new cool update"
    }
    r = requests.post(BASE_URL + ENDPOINT, data = new_data)

    print(r.status_code)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        return r.json()

    return r.text


print(create_update())
