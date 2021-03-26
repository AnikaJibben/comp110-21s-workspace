"""Examples of dictionaries."""

#Establiosh a type with dict[key type, value type]
# empty dictionary literal is{}
players: dict[str,int] = {}

# Insert a new key-value pair
# Reference keys inside subscriptopn notation, asociated values are assigned
players["Brooks"] = 15
players["Love"] = 2
players["Bacot"] = 4 # this is intentionally off by one
players["Bacot"] = players["Bacot"] + 1
print(players)


# for..in loops will give you each key one by one
# dont need key and value defined and the print key and value
for player_name in players:
    key: str = player_name
    value: int= players[key]
    print(f"{player_name} -> {players[player_name]}")
    print(f"{key} -> {value}")

#you can have keys and values of any types, notice this is the opposite mapping
# that we had above. Additionally this is an example of a dictionary literal
jerseys: dict[int, str] = {15: "Brooks", 2: "Love", 5: "Bacot"}
jerseys[23] = "Jordan"
print(jerseys)
print(jerseys[23])

# the pop method allows you to remove a key-value pair by its key. the pop
# method return the value associated with the popped key
popped_name: str = jerseys.pop(23)
print(popped_name)
print(jerseys)