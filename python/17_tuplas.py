# TUPLAS: estructura de datos inmutables

numbers = (1, 2, 3, 5)
strings = ('nico', 'zuke', 'santi', 'nico')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# Métodos
print(strings)
print(strings.index('zuke'))
print(strings.count('nico'))

# Convertir tupla a lista para poder modificarla
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

# Transformar lista a tupla después de hacer la modificación

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))