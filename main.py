# Calculadora que realiza operações simples

print('[CALCULADORA]')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione "s" para sair')

# laço de repetição infinita:
while True:

    op = input('Digite uma operação: ')

    if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x, y, res))
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
    elif (op == '/'):
        res = x // y
        print('Resultado: {} / {} = {}'.format(x, y, res))

    # se a tecla 's' for pressionada:
    elif (op == 's'):

        break

    # se o dado inserido for diferente das exigidas acima:
    else:
        print('Opção inválida. Digite uma operação válida ou pressione "s" para sair.')

# se o laço de repetição for quebrado:
print('Encerrando programa...')