import json as js
from datetime import datetime as dt

def get_sex():
    with open('sexboard.json') as f:
        data = js.load(f)
        return data

def add_sex(user):
    try:
        data = get_sex()
        data[user]['total'] += 1
    except KeyError:
        data[user]['total'] = 1
    with open('sexboard.json', 'w') as f:
        js.dump(data, f)



