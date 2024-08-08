#1 – Para treinar o laço de repetição FOR, crie um formulário e peça para o usuário digitar
#um número inicial e um número final, mostre o intervalo entre esses números, mas
#lembre-se que ele poderá digitar um intervalo muito grande que irá consumir muita
#memória do servidor, pensando nisso valide para que ele digite apenas intervalos de no
#máximo 100 números.

n1 = int(input("Digite um numero inicial: "))
n2 = int(input("Digite o segundo numero: "))

if n2 < 101:
    for i in range(n1-1 , n2, 1):
        print("Numero", i)
else:
    print("Numero Muito grande para o servidor")