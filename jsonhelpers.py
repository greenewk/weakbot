import json as js
from datetime import date

def get_sex():
    with open('sexboard.json') as f:
        data = js.load(f)
        return data

def add_sex(user):
    today = str(date.today())
    week = (str(date.today().isocalendar()[1]) + '-' + 
            str(date.today().isocalendar()[0]))
    month = (str(date.today().month) + '-' +
            str(date.today().year))
    year = (str(date.today().year))

    data = get_sex()
    data.setdefault(user, {})

    data[user].setdefault('total', 0)
    data[user]['total'] += 1

    data[user].setdefault('days', {})
    data[user]['days'].setdefault(today, 0)
    data[user]['days'][today] += 1

    data[user].setdefault('weeks', {})
    data[user]['weeks'].setdefault(week, 0)
    data[user]['weeks'][week] += 1

    data[user].setdefault('months', {})
    data[user]['months'].setdefault(month, 0)
    data[user]['months'][month] += 1

    data[user].setdefault('years', {})
    data[user]['years'].setdefault(year, 0)
    data[user]['years'][year] += 1

    with open('sexboard.json', 'w') as f:
        js.dump(data, f)



