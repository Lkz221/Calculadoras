num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
calculos = [num1+num2, num1-num2, num1*num2, f'{num1/num2:.2f}', num1**num2]
print("-="*20)
print("Escreva o operador correspodente ao numero que esta apos o ')'\n1)Somar\n2)Subtrair\n3)Multiplicar\n4)Divisão\n5)Exponenciação")
print('-='*20)
operador = int(input('Escolha um desses a cima: ')) - 1
print(f'O resultado é {calculos[operador]}')