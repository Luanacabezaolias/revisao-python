'''Implemente a função quadrado que recebe um número e retorna o resultado desse número ao 
quadrado.'''

def quadrado(num):
    quadrado = num ** 2
    print(quadrado)
    return quadrado 

num = float(input("informe um número: "))
quadrado(num)
