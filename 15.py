def calcular_anos_para_extincao(numero_especies, taxa_extincao_menor, taxa_extincao_maior):

    especies_restantes = numero_especies - 2  
    anos_menor = especies_restantes / taxa_extincao_maior[1]  
    anos_maior = especies_restantes / taxa_extincao_menor[0]  
    return anos_menor, anos_maior

def main():
    
    estimativa_baixa = 2_000_000  
    estimativa_alta = 100_000_000  

    taxa_extincao_menor_baixa = (200, 2_000)  
    taxa_extincao_maior_baixa = (200, 2_000)  
    
    taxa_extincao_menor_alta = (10_000, 100_000)  
    taxa_extincao_maior_alta = (10_000, 100_000)  
    
   
    anos_baixa_menor, anos_baixa_maior = calcular_anos_para_extincao(estimativa_baixa, taxa_extincao_menor_baixa, taxa_extincao_maior_baixa)
    anos_alta_menor, anos_alta_maior = calcular_anos_para_extincao(estimativa_alta, taxa_extincao_menor_alta, taxa_extincao_maior_alta)
    
    
    print(f"Para a estimativa baixa de 2 milhões de espécies:")
    print(f"- Com a taxa de extinção menor (200 a 2.000 por ano):")
    print(f"  - Anos até extinção total (mínimo): {anos_baixa_menor:.0f} anos")
    print(f"  - Anos até extinção total (máximo): {anos_baixa_maior:.0f} anos")
    
    print(f"\nPara a estimativa alta de 100 milhões de espécies:")
    print(f"- Com a taxa de extinção menor (10.000 a 100.000 por ano):")
    print(f"  - Anos até extinção total (mínimo): {anos_alta_menor:.0f} anos")
    print(f"  - Anos até extinção total (máximo): {anos_alta_maior:.0f} anos")


main()