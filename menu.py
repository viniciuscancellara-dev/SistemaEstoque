def menu():
    print("""
==============================
       SISTEMA DE ESTOQUE
==============================

1 - Adicionar produto
2 - Remover produto
3 - Consultar produto
4 - Alterar produto
5 - Apagar estoque
6 - Mostrar estoque
7 - Sair

==============================
""")

    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            return escolha
        except ValueError:
            print("Digite apenas números!")