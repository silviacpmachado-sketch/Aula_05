numero = float(input('Informe o numero:'))
match numero:
 case num if num > 0:
  print('Positivo')
 case num if num < 0:
  print('Negativo')
 case num if num == 0:
  print("Neutro")
 case _:
  print('Número inválido')