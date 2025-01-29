'''
Converter Dicionário em JSON: Converta o dicionário { "nome": "Maria", "idade":
25 } em JSON e salve no arquivo dados.json.


Meu pai amado--
'''

import json

dados = {
    'nome' : 'Ana',
    'Idade' : 21
}

#Salvando no json AAAAAAAAAAAAAAAAAAAA

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo)


#Para ler os arquivos json é recomendado usar o indent para melhor leitura do arquivo aa

with open ('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(json.dump(dados, arquivo, indent=4))   #n sei pra que serve mas tem que estudar essa budega


#Tentar implementar sistema em que o usuário consiga decidir se quer adicionar um novo aluno

#Descobri que pra isso preciso criar funçaõ eu vou me mat-
#criei em outro arquivo 'exercicio-2-def.py'