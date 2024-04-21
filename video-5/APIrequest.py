import requests

base_url = 'https://www.boredapi.com/api/activity/'
payload = {'participants ': 1} #https://www.boredapi.com/api?participants=1
r = requests.get('https://www.boredapi.com/api', params = payload)
data = r.json()
print('Response : ',data)
print("Message : ", data['message'])