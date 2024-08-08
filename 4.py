#4 - Peça para o usuário digitar outro intervalo, e agora mostre a soma entre os números
#desse intervalo, lembre-se que o usuário não pode inserir um intervalo maior que 100
#números.

n1 = int(input("\nDigite um numero inicial: "))
n2 = int(input("Digite o segundo numero: "))
resultado = 0

for i in range(n1 , n2+1, 1):
    if n2 > 100 or n1 < 0:
        print("Numero invalido para o sevidor ")
        break
    else:
        resultado +=i

print(resultado)