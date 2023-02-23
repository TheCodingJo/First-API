import requests
# request = requests.get("http://api.open-notify.org")
# #print(request.text)
# #print(request.status_code)
# request2 = requests.get('http://api.open-notify.org/fake-endpoint')
# #print(request2.status_code)
# people = requests.get('http://api.open-notify.org/astros.json')
# #print(people.text)
# people_json = people.json()
# #print(people_json)

# #To print the number of people in space
# print("Number of people in space:",people_json['number'])
# #To print the names of people in space using a for loop
# for p in people_json['people']:
#     print(p['name'])


iss_now = requests.get('http://api.open-notify.org/iss-now.json')
iss_now_json = iss_now.json()
message = iss_now_json["message"]
# print(message)

longitude = iss_now_json['iss_position']['longitude']
latitude =iss_now_json['iss_position']['latitude']

print(f'The International Space Station is currently at the following coordinates: {latitude}; {longitude}.')

