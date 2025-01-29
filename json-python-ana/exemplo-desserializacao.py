import json

#serialização com json


dados = {'nome' : 'joão','idade' : 30, 'cidade' : 'Cuiabá'}
with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo)


#desserialização

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados['nome'])