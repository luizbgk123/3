def calcular_fatorial():
    try:
        numero = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
        
        if numero < 0:
            print("Número inválido! O número deve ser não negativo.")
            return
        
        fatorial = 1
        
        for i in range(1, numero + 1):
            fatorial *= i
        
        print(f"O fatorial de {numero} é {fatorial}.")
        
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")

calcular_fatorial()