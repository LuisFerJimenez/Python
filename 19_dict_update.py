person = {
  'name': 'Luis',
  'last_name': 'Jimenez',
  'langs': ['python', 'js'],
  'age': 27
}

print(person)

person['name'] = 'Fernando'
person['age'] -= 7
person['langs'].append('Go')
print(person)

del person['last_name']
print(person)
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())