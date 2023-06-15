#diccionarios 
#{ "key": "value", "key": value }

team = {
    "name": "City",
    "country": "England",
    "champions":1,
    "players": ['halland','grealinsh']
}

print(type(team))
print(team)
print (team["name"])
print (team["players"])
team["players"].append("Kevin")
team["name"] = "manchertes city"
team["league"] = "premiere league" 
print(team)


