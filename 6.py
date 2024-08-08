#6 – Utilizando o Laço While imprima os 100 valores posteriores ao que o usuário digitou,
#a cada 10 impressões crie uma forma elegante de separar os dados visualmente.

def imprimir_valores():
    numero_inicial = int(input("Digite um número inteiro: "))

    contagem = 0
    valor_atual = numero_inicial + 1

    while contagem < 100:
        print(f"{valor_atual:4}", end=" ")  
        
        valor_atual += 1
        contagem += 1
        
        if contagem % 10 == 0:
            print()  

    if contagem % 10 != 0:
        print()

imprimir_valores()
