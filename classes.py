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
    @preco.setter
    def preco(self,novo_preco):
        if novo_preco <0:
            raise ValueError("O preco deve ser maior que 0!")
        self.__preco = novo_preco

    @property
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self,nova_quantidade):
        if nova_quantidade <0:
            raise ValueError("A quantidade deve ser maior que 0!")
        self.__quantidade = nova_quantidade
    
    def __str__(self):
        return f"ID : {self.__id} - Produto : {self.nome} - Preco :R$ {self.__preco} - Quantidade : {self.__quantidade}."

class Eletronico(Produto):
    def __init__(self, id, nome, preco, quantidade, garantia, voltagem):
        super().__init__(id, nome, preco, quantidade)
        self.__garantia = garantia
        self.voltagem = voltagem

    @property
    def garantia(self):
        return self.__garantia
    @garantia.setter
    def garantia(self,nova_garantia):
        if nova_garantia <0:
            raise ValueError("A garantia deve ser de no minimo 0 anos!")
        self.__garantia = nova_garantia

    def __str__(self):
        return f"ID : {self.id} - Produto : {self.nome} - Preco :R$ {self.preco} - Quantidade : {self.quantidade} - Garantia : {self.__garantia} - Voltagem : {self.voltagem}."

class Alimento(Produto):
    def __init__(self, id, nome, preco, quantidade, peso, validade):
        super().__init__(id, nome, preco, quantidade)
        self.peso = peso
        self.__validade = validade

    @property
    def validade(self):
        return self.__validade
    @validade.setter
    def validade(self, nova_validade):
        if not nova_validade:
            raise ValueError("O campo deve ser preenchido!")
        self.__validade = nova_validade 

    def __str__(self):
        return f"ID : {self.id} - Produto : {self.nome} - Preco :R$ {self.preco} - Quantidade : {self.quantidade} - Peso : {self.peso} - Validade : {self.__validade}."

class Roupa(Produto):
    def __init__(self,id,nome,preco,quantidade,tamanho,marca):
        super().__init__(id, nome, preco, quantidade)
        self.__tamanho = tamanho
        self.__marca = marca

    @property
    def tamanho(self):
        return self.__tamanho
    @tamanho.setter
    def tamanho(self,novo_tamanho):
        if not novo_tamanho:
            raise ValueError("O campo deve ser preenchido!")
        self.__tamanho = novo_tamanho

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,nova_marca):
        if not nova_marca:
            raise ValueError("O campo deve ser preenchido!")
        self.__marca = nova_marca

    def __str__(self):
        return f"ID : {self.id} - Produto : {self.nome} - Preco :R$ {self.preco} - Quantidade : {self.quantidade} - Tamanho : {self.__tamanho} - Marca : {self.__marca}."
    

    