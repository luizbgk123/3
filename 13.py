def mostrar_numeros():
    try:
        numero_maximo = int(input("Digite até que número você deseja ver (máximo 100): "))
        
        if numero_maximo < 0:
            print("Número inválido! O número deve ser maior ou igual a 0.")
            return
        if numero_maximo > 100:
            print("Número inválido! O número deve ser no máximo 100.")
            return
        
        for numero in range(0, numero_maximo + 1):
            print(numero, end=" ")
        print()  
        
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")

mostrar_numeros()