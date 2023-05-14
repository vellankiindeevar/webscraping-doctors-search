import mysql.connector
import json

db = mysql.connector.connect(
        host = 'localhost',
        user = 'indeevar',
        passwd = 'indeevar',
        database = 'hehe',
    )

cursor = db.cursor()

with open('doctors.json', 'r') as f:
    data = json.load(f)

for i in data:
    query = "INSERT INTO doctors (name, gender, speciality, address, city, phone_no) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (i['name'],i['gender'],i['speciality'],i['address'],i['city'],i['phone_no'])
    cursor.execute(query, values)

db.commit()

cursor.close()
db.close()
