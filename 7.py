def imprimir_intervalo_inverso_e_correto():
    intervalo_str = input("Digite até 10 números inteiros separados por espaços: ")
    
    intervalo = list(map(int, intervalo_str.split()))
    
    if len(intervalo) > 10:
        print("O intervalo não pode ter mais de 10 números.")
        return
    
    print("Intervalo na ordem inversa:")
    for numero in reversed(intervalo):
        print(numero, end=" ")
    print()
    
    print("Intervalo na ordem correta:")
    for numero in intervalo:
        print(numero, end=" ")
    print()  

imprimir_intervalo_inverso_e_correto()