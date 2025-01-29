'''
Converter Dicionário em JSON: Converta o dicionário { "nome": "Maria", "idade":
25 } em JSON e salve no arquivo dados.json.

com adição do usuário podendo adicionar pessoas :D

'''




import json

#import os #q diabéisso

#descobri que da pra fazer sem ent vou fazer sem, é isso

def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def salvar_dados(dados):
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4) #O dump serve para desserialização que -> Converter strings JSON em objetos Python. Só falta eu lembrar disso sempre

lista = carregar_dados()

while True:
    nome = input('\nDigite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    novo_user = {'nome' : nome, 'idade' : idade}
    lista.append(novo_user)

    decisao = int(input('Deseja adicionar mais alguém?\n1 - Sim\n2 - Não'))

    if decisao != 1:
        break

salvar_dados(lista)

print(json.dump(lista, indent=4)) #estudar esse diax de indent