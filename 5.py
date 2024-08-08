#5 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
#inteiro entre 1 e 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

tabuada = int(input("\nDigite a tabuada que deseja: "))

resultado = 0

print(f"\nvocê escolheu a tabuada do {tabuada}")

for num in range (1, 10 + 1, 1):
    resultado = tabuada * num
    print(f"{tabuada} X {num} = {resultado}")