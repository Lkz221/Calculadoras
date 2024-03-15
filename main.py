import os

import calculos as cacl
while True:
    print('Para parar aperte ctrl+c!')
    print(cacl.linha('-='))
    try:
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
    except ValueError as err:
        print('Digite um numero valido')
        print(cacl.linha('-='))
        continue
    except KeyboardInterrupt as err:
        print('\nExecução parada pelo usuario!')
        break
    operador = input('Escreva um operador (+,-,/,*,**): ')
    if len(operador) > 2:
        print('Escreva um operador valido!')
        print(cacl.linha('-='))
        continue
    else:
        if operador in '+-**/':
            cacl.linha('-=')
            os.system('cls')
            if operador == '**':
                print(cacl.resul('exponenciação', num1, num2, cacl.ex(num1, num2)))
                print(cacl.linha('-='))
            elif operador == '+':
                print(cacl.resul('soma', num1, num2, cacl.soma(num1, num2)))
                print(cacl.linha('-='))
            elif operador == '-':
                print(cacl.resul('subtração', num1, num2, cacl.sub(num1, num2)))
                print(cacl.linha('-='))
            elif operador == '/':
                print(cacl.resul('devisão', num1, num2, cacl.div(num1, num2)))
                print(cacl.linha('-='))
            elif operador == '*':
                print(cacl.resul('multiplicação', num1, num2, cacl.mult(num1, num2)))
                print(cacl.linha('-='))
            else:
                print('Como vc chegou aqui?')


