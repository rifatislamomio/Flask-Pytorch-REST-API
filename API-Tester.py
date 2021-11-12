import requests
import json

api_url = "http://127.0.0.1:5000"
payload =  {'image': open("IMAGE_FILE_PATH", 'rb')}

req = requests.post(url=api_url, files=payload)
res = json.loads(req.text)

print(res)