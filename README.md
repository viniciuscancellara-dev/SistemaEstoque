#  Sistema de Estoque em Python

Sistema de gerenciamento de estoque desenvolvido em Python utilizando Programação Orientada a Objetos, com herança, encapsulamento, polimorfismo e persistência de dados em JSON.

O projeto começou como uma aplicação simples e foi evoluindo para um sistema estruturado utilizando classes, objetos e persistência de dados em arquivos JSON.

---

##  Funcionalidades

 Cadastro de produtos
 Geração automática de IDs
 Consulta de produtos por ID
 Alteração de informações do produto
 Remoção de produtos do estoque
 Armazenamento permanente dos dados em JSON
 Recuperação dos dados ao iniciar o programa
 Conversão entre objetos Python e dicionários para manipulação do JSON
 Limpeza completa do estoque

---

##  Conceitos praticados

Durante o desenvolvimento foram aplicados conceitos como:

### Programação Orientada a Objetos

* Criação de classes
* Instanciação de objetos
* Métodos de classe
* Encapsulamento de atributos
* Uso de propriedades (`@property`)
* Herancas
* Polimorfismo

### Manipulação de dados

* Listas de objetos
* Dicionários
* Conversão objeto → dicionário
* Conversão dicionário → objeto
* Leitura e escrita de arquivos JSON

### Organização de código

O projeto foi dividido em diferentes responsabilidades:

```
Sistema-Estoque/
│
├── main.py          # Controle principal da aplicação
├── menu.py          # Interface do menu
├── classes.py       # Classes e objetos
├── funcoes.py       # Regras e operações do estoque
└── estoque.json     # Banco de dados local
```

---

##  Persistência de dados

O sistema utiliza um arquivo JSON como armazenamento.

Como objetos Python não podem ser armazenados diretamente em JSON, foi criada uma conversão:

```
Objeto Produto
       ↓
Dicionário
       ↓
Arquivo JSON
```

E ao iniciar o programa:

```
Arquivo JSON
       ↓
Dicionário
       ↓
Objeto Produto
```

Isso permite que os produtos continuem salvos mesmo após fechar o programa.

---

##  Tecnologias utilizadas

* Python 3
* JSON
* Programação Orientada a Objetos
* Git e GitHub

---

##  Exemplo de funcionamento

Cadastro de produto:

```
ID: 1
Nome: teclado
Preço: 150
Quantidade: 10
```

Após salvar:

```json
{
    "id": 1,
    "nome": "teclado",
    "preco": 150,
    "quantidade": 10
}
```

---

##  Evolução do projeto

Este projeto foi desenvolvido como prática de aprendizado em Python, evoluindo conforme novos conceitos foram aprendidos.

Inicialmente era um sistema simples baseado em funções, mas foi refatorado para utilizar:

* Classes
* Objetos
* Encapsulamento
* Separação de responsabilidades
* Persistência de dados

O objetivo é continuar evoluindo o projeto adicionando novas funcionalidades e aplicando conceitos mais avançados de desenvolvimento.

---

##  Desenvolvido por

**Vinicius Cancellara**

Projeto criado para estudos de Python e desenvolvimento de software.
