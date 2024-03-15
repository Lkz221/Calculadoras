def mult(x, y):
    return x * y

def soma(x, y):
    return x + y

def div(x, y):
    return x / y

def sub(x, y):
    return x - y

def ex(x, y):
    return x ** y

def resul(msg,x,y,resul,cor:bool=True):
    from colorama import Fore, Style
    r = Style.RESET_ALL
    if cor:
        return f'{Fore.LIGHTBLUE_EX}A {msg} entre {x} e {y} é igual a {r}{Fore.LIGHTRED_EX}{resul}{r}'
    else:
        return f'A {msg} entre {x} e {y} é igual a {resul}'
def linha(msg):
    return msg*20