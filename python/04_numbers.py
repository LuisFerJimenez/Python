lives = 3
print(type(lives))
age = 27
budget = 200

temperatura = 12.12
print(type(temperatura))

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

# Ejercicio
budget_january = int(input('Ingrese presupuesto de enero '))
budget_february = int(input('Ingrese presupuesto de febrero '))
budget_march = int(input('Ingrese presupuesto de marzo '))

budget_total = budget_january + budget_february + budget_march

avg_budget = budget_total / 3
print('El promedio es: ', avg_budget)