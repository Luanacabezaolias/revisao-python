'''Implemente a função media, que recebe três valores numéricos e retorna a média aritmética dos 
valores.'''

def media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media 

num1 = float(input("Infome o primerio número: "))
num2 = float(input("Infome o segundo número: "))
num3 = float(input("Infome o terceiro número: "))
print(f"A média dos números é de {media(num1, num2, num3)}")