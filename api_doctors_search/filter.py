import json
import jmespath
import pandas as pd


with open('doctors.json') as f:
    data = json.load(f)


s = "items[].{addresses: addresses,email: email,firstName: firstName,lastName: lastName,gender: gender,specialty: specialty,title: title,zip: addresses[].zip,phonenumber: addresses[].phoneNumber}"
b = jmespath.search(s,data)

with open ('doctors_filterd_data.json', 'w') as j:
    json.dump(b,j,indent=4)
    
df = pd.read_json('doctors_filterd_data.json')
print(df)
