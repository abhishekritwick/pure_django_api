import os
import json
import requests

ENDPOPINT = "http://127.0.0.1:8000/api/status/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

image_path = os.path.join(os.getcwd(), "images", "DRF_logo.png")

headers = {
	"Content-Type": "application/json"
}

data = {
	'username':'ritwick',
	'password':'testpassword'
}



# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()['token']
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InJpdHdpY2siLCJleHAiOjE1ODU3NDQxNjUsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE1ODU3NDM4NjV9.4VTLE7Y0RU-Z2HyfyRsfLBz8wFZ5iusXPMElzjufWNM"
print(token)

refresh_data = {
	'token':token
}

new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
new_token = new_response.json()['token']
print(new_token)


headers = {
	# "Content-Type": "application/json",
	"Authorization": "JWT " + token,
}

post_data = {} #json.dumps({"content":"some random content vvv random"})

with open(image_path, 'rb') as image:
	file_data = {
		'image' : image
	}
	posted_response = requests.post(ENDPOPINT, data = post_data, headers=headers, files = file_data)
	print(posted_response.text)



# def do_img(method='get', data={}, is_json=True, img_path = None):
#     headers = {}
#     if is_json:
#     	headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#     	with open(img_path, 'rb') as image:
#     		file_data = {
#     			'image' : image
#     		}
#     		r = requests.request(method, ENDPOPINT, data=data, headers = headers, files = file_data)	
#     else:
#     	r = requests.request(method, ENDPOPINT, data=data)
#     print(r.text)
#     print(r.status_code)
#     return r

# def do(method='get', data={}, is_json=True):
#     if is_json:
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOPINT, data=data)
#     print(r.text)
#     return r

# get_endpoint = ENDPOPINT + str(8)


# do_img(method='patch', data={'id':10,'user':1, 'content':""}, is_json=False ,img_path=image_path)
#data={'id':7}
