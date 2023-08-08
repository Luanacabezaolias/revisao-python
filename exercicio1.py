'''Implemente a função somar que recebe dois números e retorna o resultado da soma desses dois 
números.
Lembre-se que para retornar um resultado a função deve utilizar a instrução return.'''


def soma(num1,num2):
    soma = num1 + num2
    return soma


num1 = float(input("informe um número: "))
num2 = float(input("informe outro número: "))
resultado = soma(num1,num2)
print(resultado)

