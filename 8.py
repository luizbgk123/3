def controlar_laco_while():
    continuar = True
    contagem = 0

    while continuar:
        print(f"Valor do booleano: {continuar}")

        contagem += 1

        if contagem >= 15:
            continuar = False  

    print("Laço encerrado.")

controlar_laco_while()