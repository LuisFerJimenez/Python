# Las listas pueden ser modificadas, cada elemenro está separado por comas y puede contener todo tipo de datos

numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'Hola']
print(types)

print(numbers[0])
print(tasks[0])
text = 'hola'
#text[0] = 'W'

tasks[0] = 'watch platzi course'
print(tasks)

tasks[0] = 'do the disehes'
print(tasks)

print(numbers[:3])
print(True in types)
print('hola' in types)