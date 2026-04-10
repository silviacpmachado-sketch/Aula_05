# # Match Case
# print("""
# [1] - Marketing
# [2] - Financeiro
# [3 a 5] - ADM
# [6 a 9] - TI
# [10] - Serviços Gerais      
# """)

# codigo = int(input('Informe o código de acesso: '))

# match codigo: 
#     case 1:
#         print('Marketing')
#     case 2:
#         print('Financeiro')
#     case 3 | 4 | 5:
#         print('ADM')
#     case 6 | 7 | 8 | 9:
#         print('TI')
#     case 10:
#         print('Serviços Gerais')
#     case _: 
#         print('Acesso Negado')

# Verifica Faixa Etária
# idade = int(input('Informe a idade:'))
# match idade:
#  case idade if 0 <= idade < 12:
#   print('Criança')
#  case idade if 12 <= idade < 18:
#   print('Adolescente')
#  case idade if idade >= 18:
#   print('Adulto')
#  case _:
#   print('Idade Inválida')
  
# Escolha a forma de pagamento
valor = float(input('Informe o valor: '))
print("""
Escolha a forma de pagamento
[1] - Pix (12% de desconto)
[2] - Débito (8% de desconto)
[3] - Crédito (5% de desconto)
[4] - Dinheiro (15% de desconto)
    """)
opcao = int(input('Escolha uma das opções: '))
desconto = 0

match opcao:
    case 1:
        desconto = valor * 0.12
        print('\n---Pagamento no Pix---')
        
    case 2:
        desconto = valor * 0.08
        print('\n---Pagamento no Débito---')

    case 3:
        desconto = valor * 0.05
        print('\n---Pagamento no Crédito---')

    case 4:
        desconto = valor * 0.15
        print('\n---Pagamento no Dinheiro---')

    case _:
        print('Opção Inválida')

if desconto != 0:
    valor_final = valor - desconto
    print(f'Valor: {valor}')
    print(f'Valor do Desconto: {desconto}')
    print(f'Valor com o Desconto: {valor_final}')
else:
    print('Por favor, informe uma das opções acima')