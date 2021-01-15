import json as js

def get_sex():
    with open('sexboard.json') as f:
        data = js.load(f)
        return data

def add_sex(user):
    try:
        data = get_sex()
        data[user] += 1
    except KeyError:
        data[user] = 1
    with open('sexboard.json', 'w') as f:
        js.dump(data, f)



