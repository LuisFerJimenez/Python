'''for element in range(1, 21):
  print(element)'''

my_list = [23, 24, 25, 26, 27]
for element in my_list:
  print(element)

my_tuple = ('luis', 'fernando')
for elemnet in my_tuple:
  print(elemnet)

product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}
for element in product:
  print(elemnet, '=>', product[element])

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'luis',
    'age': 27
  },
  {
    'name': 'fernando',
    'age': 26
  },
  {
    'name': 'key',
    'age': 26
  }
]

for person in people:
  print(person['name'])