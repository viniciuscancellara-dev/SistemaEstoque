class Produto():
    def __init__(self,id,nome,preco,quantidade):
        self.__id = id
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def id(self):
        return self.__id
    @property
    def preco(self):
        return self.__preco
    @property
    def quantidade(self):
        return self.__quantidade
    
    def __str__(self):
        return f"ID : {self.__id} - Produto : {self.nome} - Preco : {self.__preco} - Quantidade : {self.__quantidade}."
    
    def aumentar_quantidade(self,aumento):
        self.__quantidade += aumento
        
    def diminuir_quantidade(self,subtracao):
        self.__quantidade -= subtracao
        
    def alterar_preco(self,novo_preco):
        self.__preco = novo_preco

    def alterar_quantidade(self,nova_quantidade):
        self.__quantidade = nova_quantidade
    