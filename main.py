import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('computer_wins', computer_wins)
  print('user_wins', user_wins)
  
  user_option = (input('piedra, papel o tijera => ')).lower()

  rounds += 1
  
  if not user_option in options:
    print('Opción no válida')
    continue
    
  computer_option = random.choice(options)
  
  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('pidra gana a tijera')
      print('user ganó!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('Computer ganó!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gana')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gana!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gana!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gana!')
      computer_wins += 1

  if computer_wins == 2:
    print('El rotundo ganador es la computadora')
    break

  if user_wins == 2:
    print('El rotundo ganador es el usuario')
    break
  