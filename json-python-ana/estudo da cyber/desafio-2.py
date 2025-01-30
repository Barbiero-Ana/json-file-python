'''
Desafio 2 - Agenda de contatos:
Escreva um programa que permita adicionar, editar ou remover contatos de uma agenda de contatos. Seu programa deve utilizar um arquivo JSON para persistir os dados.

SENHOOOOOOOOOOOOOOOOOOOOOOOOOOR

'''

import json

#ao inves de usar um 'import os' pode se usar o try

def load_contatos():
    try:
        with open('lista-contatos.json', 'r') as arquivo:
            return json.load(arquivo)
        
    except FileNotFoundError:
        return []
    #retornar uma lista vazia caso o documento nao exista (mas existe né vamo la)

def salvar_contatos(contatos):
    with open('lista-contatos.json', 'w') as arquivo:
        json.dump(contatos, arquivo, indent= 4) #estudar essa budega do indent=
    
def adicionar(contatos):
    nome = input('Digite o nome do contato a ser adicionado: ')
    telefone = input('Digite o telefone do contato a ser adicionado - ex: (99)99999-9999\n- ')
    email = input('Digite o E-mail do contato a ser adicionado: ')
    contatos.append({'nome' : nome, 'telefone' : telefone, 'email' : email})
    print(f'\n{nome} adicionado(a) lista de contatos.\n' )

def editar(contatos):
    nome = input('Digite o nome do contato que deseja alterar: ')
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            contato['telefone'] = input('Digite o novo telefone: ')
            contato['email'] = input('Digite o novo E-mail: ')
            print('Contato atualizado.')
            return
    print(f'\nContato de nome: {nome} não encontrado.')

def remover(contatos):
    nome = input('Digite o nome do contato que deseja remover da lista: ')
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            contatos.remove(contato)
            print(f'\n{nome} removido(a) da lista de contatos.')
            return
    print(f'\n{nome} não encontrado na lista') #SACO


def listar(contatos):
    if not contatos:
        print('Nenhum contato cadastro na lista ainda...........')
    
    else:
        print(f'\nLista de contatos adicionados\n')
        for i, contato in enumerate(contatos, 1):
            print(f'{i}. nome: {contato['nome']}\nTelefone: {contato['telefone']}\nE-mail: {contato['email']} \n')

def menu():

    contatos = load_contatos()
    while True:
        print('1 - Adicionar contato\n2 - Editar contato\n3 - Remover contato\n4 - Listar contatos\n5 - sair')
        decisao = int(input('Digite qual opção deseja realizar\n- '))

        if decisao == 1:
            adicionar(contatos)
        
        elif decisao == 2:
            editar(contatos)

        elif decisao == 3:
            remover(contatos)
        elif decisao == 4:
            listar(contatos)

        elif decisao == 5:
            salvar_contatos(contatos)
            print('\nSaindo do sistema.')
            break

        else:
            print('\nOpção inválida! Tente novamente!')

menu()