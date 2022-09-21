
# 1. Convert two lists into a dictionary

keys = ['ten' ,'twenty', 'thirty']
values = [10, 20, 30]


# Expected output

{
    'ten': 10,
    'twenty': 20,
    'thiry': 30
}


result = dict(zip(keys, values))
print(result)

# 2. Merge two dictionareis into one

dict1 = {
    'ten': 10,
    'twenty': 20,
    'thiry': 30
}

dict2 = {
    'forty': 40,
    'fifty': 50,
    'sixty': 60
}

combined = (dict1.update(dict2))
print(dict1)
