# import json
# from pprint import pprint
#
# with open('data.json', 'r', encoding='utf-8') as data_json:
#     data_json = data_json.read()
#     data = json.loads(data_json)[1]
#     json_data = json.dumps(data)
#     print(json_data)
#     print(type(json_data))
#     pprint(data)
#     print(type(data))


data = {
    'user1': [
        {'username': 'user1', 'password': '1283657'},
        {'msg': {
            'date': "17:30",
            'msg1': 'hello',

        }}
    ]
}
data['user1'][1]['msg']['msg1'] = 'Welcome'
data['user1'][1]['msg'].update({'msg2': 'Halo'})
print(data)
