def swap_nomes():
    primeiro_nome = "will"
    segundo_nome = "lucas"

    num_interacoes = 6  

    for i in range(num_interacoes):
        print(f"Interação {i + 1}:")
        print(f"primeiro nome: {primeiro_nome}")
        print(f"segundo nome: {segundo_nome}")

        primeiro_nome, segundo_nome = segundo_nome, primeiro_nome

        print()


swap_nomes()
