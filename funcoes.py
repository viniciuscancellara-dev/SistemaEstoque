import json
import os
from classes import *


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")




def produto_para_dict(produto):
    return {
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco,
        "quantidade": produto.quantidade,
    }


def dict_para_produto(dados):
    return Produto(
        dados["id"], dados["nome"], dados["preco"], dados["quantidade"]
    )

def carregar_estoque():
    try:
        with open("estoque.json", "r") as arq:
            dados = json.load(arq)

        estoque = []
        for produto in dados:
            objeto = dict_para_produto(produto)
            estoque.append(objeto)

        return estoque

    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou o JSON estiver vazio retorna lista vazia
        return []


estoque = carregar_estoque()


def salvar(estoque):
    dados = []
    for produto in estoque:
        dados.append(produto_para_dict(produto))

    with open("estoque.json", "w") as arq:
        json.dump(dados, arq, indent=4)

def adicionar_produto():
    limpar_tela()
    print("=" * 45)
    print("         CADASTRO DE PRODUTOS")
    print("=" * 45)

    while True:
        try:
            quantity = int(input("\nQuantos produtos deseja cadastrar?: "))
        except ValueError:
            print("Valor invalido")
            continue

        if quantity <= 0:
            print("Valor deve ser maior que 0")
            continue
        else:
            break

    maior_id = 0
    for produto in estoque:
        if produto.id > maior_id:
            maior_id = produto.id

    id = maior_id + 1

    print("""
    -----------------------
    Qual o tipo do produto?
    -----------------------

    1- Eletronicos
    2- Alimentos
    3- Roupas
    """)
    while True:
        try:
            escolha = int(input("Escolha uma opcao 1 - 3: "))
        except ValueError:
            print("Valor invalido!")
            continue
        if escolha not in(1,2,3):
            print("Valor indefinido!")
            continue
        break


    for i in range(quantity):
        print("\n" + "-" * 30)
        nome = input(f"Digite o nome do produto {i+1}: ").lower()

        while True:
            try:
                preco = float(input("Preco do produto: R$ "))
                quantidade = int(
                    input(f"Quantos {nome} existe no estoque?: "))
            except ValueError:
                print("Valor invalido")
                continue

            if preco < 0 or quantidade < 0:
                print("Valor deve ser maior que 0")
                continue

            match escolha:
                case 1:
                    while True:
                        try:
                            garantia = int(input("Digite a garantia: "))
                            voltagem = int(input("Digite a voltagem: "))
                        except ValueError:
                            print("Valor invalido!")
                            continue
                        if voltagem<=0:
                            print("Voltagem nao pode ser igual a 0")
                            continue
                        break
                    produto = Eletronico(id,nome,preco,quantidade,garantia,voltagem)
                    break
                case 2:
                    while True:
                        try:
                            peso = int(input("Digite o peso (KG): "))
                            validade = str(input("Digite a data de validade"))
                        except (ValueError):
                            print("Valor invalido!")
                            continue
                        if peso <0 or not validade:
                            print("Peso nao poder ser 0, e a data de validade deve ser preenchida!") 
                            continue
                        break
                    produto = Alimento(id,nome,preco,quantidade,peso,validade)
                    break
                case 3:
                    while True:
                        try:
                            tamanho = str(input("Digite o tamanho: "))
                            marca = str(input("Digite a marca: ")).lower()
                        except (ValueError):
                            print("Valor invalido!")
                            continue
                        if not tamanho  or not marca:
                            print("Tamanho nao pode ser menor ou igual a zero, e o campo marca deve ser preenchida!")
                            continue
                        break
                    produto = Roupa(id,nome,preco,quantidade,tamanho,marca)
                    break

        estoque.append(produto)
        id += 1

    #  Salva as alterações no JSON
    salvar(estoque)
    print("\n" + "=" * 45)

def remover_produto():
    limpar_tela()
    print("=" * 45)
    print("          REMOVER PRODUTO")
    print("=" * 45)

    if not estoque:
        print("\nEstoque vazio!")
        return

    print("\n--- Produtos em Estoque ---")
    for produto in estoque:
        print(produto)
    print("-" * 45)

    while True:
        try:
            #  Alterado para buscar por ID em vez de Nome para evitar confusao
            id_remocao = int(input("\nDigite o ID do produto que deseja remover do estoque: "))
        except ValueError:
            print("ID invalido")
            continue

        encontrado = False
        for produto in estoque:
            if id_remocao == produto.id:
                encontrado = True
                estoque.remove(produto)
                print("\nProduto removido com sucesso!")
                break

        if not encontrado:
            print("ID nao encontrado!")
            continue
        else:
            break

    # Salva as alterações no JSON
    salvar(estoque)
    print("=" * 45)


def consulta():
    limpar_tela()
    print("=" * 45)
    print("         CONSULTAR PRODUTO")
    print("=" * 45)

    if not estoque:
        print("\nEstoque vazio!")
        return None

    print("\n--- Produtos no Estoque ---")
    for produto in estoque:
        print(produto)
    print("-" * 45)

    while True:
        try:
            pergunta = int(input("\nQual produto deseja consultar? (ID): "))
        except ValueError:
            print("Valor invalido")
            continue

        if pergunta < 0:
            print("Valor deve ser maior que 0")
            continue

        for produto in estoque:
            if pergunta == produto.id:
                print("\n---------------------------------------------")
                print(produto)
                print("---------------------------------------------")
                return produto

        print("ID nao encontrado no estoque. Tente novamente.")


# mudei o nome para fazer mais sentido
def alterar_produto():
    produto = consulta()
    if not produto:
        return

    print("\n" + "=" * 45)
    print("          ALTERAR PRODUTO")
    print("=" * 45)

    while True:
        try:
            novo_preco = float(input("\nDigite o novo preco: "))
            nova_quantidade = int(input("Digite a nova quantidade: "))
        except ValueError as error:
            print(error)
            continue
        break

    produto.preco = novo_preco
    produto.quantidade = nova_quantidade

    print("")
    print(produto)
    print("=" * 45)

    # Salva as alterações no JSON
    salvar(estoque)

def mostrar_estoque():
    if not estoque:
        print("Estoque vazio!")
        return
    with open("estoque.json","r")as arq:
        mostrar = json.load(arq)
    print(json.dumps(mostrar, indent=4))
        


def apagar_lista():
    limpar_tela()
    print("=" * 45)
    print("         APAGAR TODO O ESTOQUE")
    print("=" * 45)

    while True:
        pergunta = input(
            "\nVoce tem certeza que deseja apagar o estoque? (s/n): "
        ).lower()

        match pergunta:
            case "s":
                # Apaga a lista e o json
                estoque.clear()
                salvar(estoque)
                print("\nOk! Apagando a lista... Lista apagada com sucesso!")
                print("=" * 45)
                break

            case "n":
                print("\nOk. A lista nao foi apagada!")
                print("=" * 45)
                return

            case _:
                print("Valor invalido, digite apenas s ou n.")