''''Implemente a função soma_divisores, que recebe como parâmetro de entrada um número positivo 
e retorna a soma de todos os divisores desse número.
Por exemplo:
- caso o número seja 15, o retorno deve ser 24 (1 + 3 + 5 + 15).
- caso o número seja 30, o retorno deve ser 72 (1 + 2 + 3 + 5 + 6 + 10 + 15 + 30)'''


def soma_divisores(num):
    if num > 0 : 
        cont = 0 
        for n in range(1, num+1):
            if num % n == 0:
                cont += n 
                print(f"Os divisores são {n}")
        return cont

num = int(input("Insira um número inteiro e positivo: "))
soma = soma_divisores(num)
print(f"A soa dos divisores do número inserido é {soma}")