def corrida_carros():
    velocidade_carro1 = 10  # km/h
    velocidade_carro2 = 20  # km/h

    incremento_carro1 = 3   # km/h por volta
    incremento_carro2 = 1.5 # km/h por volta

    voltas = 0

    while velocidade_carro1 <= velocidade_carro2:
        voltas += 1

        print(f"Volta {voltas}:")
        print(f"Velocidade do Carro 1: {velocidade_carro1} km/h")
        print(f"Velocidade do Carro 2: {velocidade_carro2} km/h")
        print()

        velocidade_carro1 += incremento_carro1
        velocidade_carro2 += incremento_carro2

    print(f"O carro 1 ultrapassou o carro 2 após {voltas} voltas.")

corrida_carros()