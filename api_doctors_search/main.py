import json
import requests

'''
i used post method to the api 'https://intake.steerhealth.io/api/doctor-search'
with the below header and payload. there are 420 elements in total. so i used 420 as size in payload.
then i sent that json to 'doctors.json' and then filterd it to 'doctors_filter_data.json' with filter.py.
'''

headers = {
    'origin': 'https://intake.steerhealth.io',
    'accept': 'application/json',
    'content-type': 'application/json',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
}

url = 'https://intake.steerhealth.io/api/doctor-search'
s = requests.Session()
s.headers.update(headers)
payload = '{"name":"","specialty":"","distance":"","location":"","errors":{},"organizationId":"aa1f8845b2eb62a957004eb491bb8ba70a","size":420,"page":0}'
r = s.post(url, data = payload)
df = r.json()
print(type(df))

with open ('doctors.json', 'w') as j:
    json.dump(df,j,indent=4)

