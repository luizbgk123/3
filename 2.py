#2 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 100.

n1 = int(input("Digite o maximo de numeros q deseja: "))

for i in range(1,n1,1):
    if i % 2 != 0:
        print(f"{i} inpar")