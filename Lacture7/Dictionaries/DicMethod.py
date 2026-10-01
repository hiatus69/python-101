phonebook = {'Anirach': '777-1111', 'Mickey':'777-2222', 'Donald': '777-3333','pluto':'777-4444'}

heroesdict = {}
heroesdict['Hulk'] = '888-1111'
heroesdict['Iron Man'] = '888-2222'
print(heroesdict.get('Hulk','Not Found'))
print(heroesdict.get('Iron Man','Not Found'))

for key,value in phonebook.items():
    print(f"{key}: {value}")

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop('Mick','ELement not found'))
print(phonebook.pop('Mickey','ELement not found'))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('after clear')
print(phonebook)
