# Python Containers
    # lists [] -  mutable
    #tuples (x, y) - fast + immutable
    # dictionaries {} - mutable


# person1_name = "Mary"
# person2_name = "Gary"
# person1_age = 23
# person2_age = 33

# # lists

# names = ["mary","gary"]
# ages = [23, 33]
# professions = ["software enginner", "product manager"]

# #dict

# person1 = {
#     "name": "mary",
#     "age" : 23,
#     "profession" : "software enginner"
# }
# person2 = {
#     "name": "gary",
#     "age" : 33,
#     "profession" : "product manager"
# }

# del person2["name"]
# print(person2)


# person1.pop("name") # what key value you want to remove
# #person1.popitem() # removes the most recent added K:V pair




adventurer = {
    'name': 'Timothy',
    'hitPoints' : 10,
    'belongings' : ['sword', 'magic potion', 'tums', 'waterbattle'],
    'companion': {
        'name': 'velma',
        'type': 'bat',
        'companion': {
            'name': 'Tim',
            'type': 'parasite',
            'belonings' : ['scuba tank', 'ipod', 'health insurance']
        }
    }
}
# print(adventurer)

# to acces all teh keys in this dictionary

# print(adventurer.keys())

# access all the values

# print(adventurer.values())


# .get() - access a value and allows to give a default
# meassage when the value does not exist

name = (adventurer['companion'].get(['name']))
print(name)

# belongings = adventurer['companion']['companion']['belonings']
# for item in belongings:
#     print(item)

# add to dictionaires
adventurer["love"] = "level 1"

#.update()

#Remove

# popitem()
# pop()

# # to retrieve
# .get()

# # to access things like keys, values, and items
# .items()
# .keys()
# .values()


# looping over dictionaries

things = {
    'book' : "Dune",
    'tea' : "green tea",
    'computer' : 'macbook pro'
}

for key, value in things.items():
    print(key, value)

# alternatively to get a tuple for the return

for kv in things.items():
    print(kv)
