import requests
import json
URL="http://127.0.0.1:8000/studentinfo/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()

get_data()

def post(request):
    data={
        'name':'shakil',
        'roll':101,
        'city':'dhaka',
    }
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.post(url=URL,data=json_data)
        data=r.json()

post()

def Update(request):
    data={
        'id':3,
        'name':'shakil',
        'city':'dhaka',
    }
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.put(url=URL,data=json_data)
        data=r.json()

Update()


def deleted_Data(request):
    data={
        'id':3}
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.delete(url=URL,data=json_data)
        data=r.json()

deleted_Data()



