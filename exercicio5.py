'''Implemente a função calcular_salario, que recebe o salário atual de um funcionário e retorna o 
salário com um reajuste de aumento, sendo que:
- Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
- Caso contrário, o funcionário receberá 15% de aumento'''


def calcular_salario(atual):
    if atual > 2000:
        salario = atual + ( atual * (7/100))
    else: 
        salario = atual + (atual * (15/100))
    return salario

atual = float(input("Salário atual: "))
print(f"O salario com reajusta é igual a {calcular_salario(atual)}")



