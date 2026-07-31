import os
import winsound

from funcoes import (
    adicionar_produto,
    remover_produto,
    consulta,
    alterar_produto,
    apagar_lista,
    salvar,
    estoque
)

winsound.PlaySound(
    "musicash-musica-de-espera.wav",
    winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)


from menu import menu


while True:

    os.system("cls")

    escolha = menu()


    match escolha:

        case 1:
            os.system("cls")
            adicionar_produto()

            input("\nPressione ENTER para continuar...")


        case 2:
            os.system("cls")
            remover_produto()

            input("\nPressione ENTER para continuar...")


        case 3:
            os.system("cls")
            consulta()

            input("\nPressione ENTER para continuar...")


        case 4:
            os.system("cls")
            alterar_produto()

            input("\nPressione ENTER para continuar...")


        case 5:
            os.system("cls")
            apagar_lista()

            input("\nPressione ENTER para continuar...")


        case 6:
            print("Encerrando programa...")
            break


        case _:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")