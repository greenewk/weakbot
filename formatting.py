from datetime import date as dt

def format_alltime_fucks(data):
    results = '**ALL      TIME      FUCKS**\n'
    results += '-----------------------------\n'
    for user in data:
        results += f' **{user}** \n     {data[user]["total"]} fucks\n'
    return results

def format_today_fucks(data):
    today = str(dt.today())

    results = f'**TODAY\'S           FUCKS**\n'
    results += '-----------------------------\n'
    for user in data:
        results += f' **{user}** \n     {data[user]["days"][today]} fucks\n'
        results += '-----------------------------\n'
    return results

def format_week_fucks(data):
    week = str(dt.today().isocalendar()[1])
    year = str(dt.today().year)
    wkyear = week + '-' + year

    results = f'**WEEK      FUCKS      {wkyear}**\n'
    results += '-----------------------------\n'
    for user in data:
        results += f' **{user}** \n     {data[user]["weeks"][wkyear]} fucks\n'
        results += '-----------------------------\n'
    return results


def format_month_fucks(data):
    month = str(dt.today().month)
    year = str(dt.today().year)
    monyear = month + '-' + year

    results = f'**MONTH      FUCKS      {monyear}**\n'
    results += '-----------------------------\n'
    for user in data:
        results += f' **{user}** \n     {data[user]["months"][monyear]} fucks\n'
        results += '-----------------------------\n'
    return results


def format_year_fucks(data):
    year = str(dt.today().year)

    results = f'**YEAR      FUCKS      {year}**\n'
    results += '-----------------------------\n'
    for user in data:
        results += f' **{user}** \n     {data[user]["years"][year]} fucks\n'
        results += '-----------------------------\n'
    return results

