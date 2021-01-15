def format_fucks(data):
    results = ''
    for user in data:
        results += f' **{user}** \n     {data[user]["total"]} fucks\n'
    return results
