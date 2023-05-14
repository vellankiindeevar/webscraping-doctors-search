import json
from requests_html import HTMLSession
import unicodedata

session = HTMLSession()

with open('links.json') as f:
    data = json.load(f)

doctors_list = []

for i in data:
    r = session.get(i)

    doctors = {}

    name_element = r.html.find('#__next > div > div.mainWrapper > div > div.MainCard__Wrapper-a34hio-0.gYCuyN > div > div > div > b',first=True)
    if name_element is not None:
        doctors["name"] = unicodedata.normalize("NFKD", name_element.text)
    else:
        doctors["name"] = None

    gender_element = r.html.find("#__next > div > div.mainWrapper > div > div.MainCard__Wrapper-a34hio-0.gYCuyN > div > div > div > span",first=True)
    if gender_element is not None:
        doctors["gender"] = gender_element.text
    else:
        doctors["gender"] = None

    speciality_element = r.html.find("#__next > div > div.mainWrapper > div > div.MainCard__Wrapper-a34hio-0.gYCuyN > div > div > div > div.meta > div.speciality > span",first=True)
    if speciality_element is not None:
        doctors["speciality"] = speciality_element.text
    else:
        doctors["speciality"] = None

    address_element = r.html.find("#__next > div > div.mainWrapper > div > div:nth-child(4) > div:nth-child(1) > div.LocationtsCard__Wrapper-sc-1a5uk22-0.gQkIkq > div > div > span",first=True)
    if address_element is not None:
        doctors["address"] = address_element.text
    else:
        doctors["address"] = None

    city_element = r.html.find("#__next > div > div.mainWrapper > div > div.MainCard__Wrapper-a34hio-0.gYCuyN > div > div > div > div.meta > div.hideMobile > span",first=True)
    if city_element is not None:
        doctors["city"] = city_element.text
    else:
        doctors["city"] = None

    phone_element = r.html.find("#__next > div > div.mainWrapper > div > div:nth-child(4) > div:nth-child(1) > div.LocationtsCard__Wrapper-sc-1a5uk22-0.gQkIkq > div > div > div.inline > div:nth-child(1) > span",first=True)
    if phone_element is not None:
        doctors["phone_no"] = phone_element.text
    else:
        doctors["phone_no"] = None

    doctors_list.append(doctors)


with open('doctors.json', 'w') as f:
    json.dump(doctors_list, f, indent=4)
