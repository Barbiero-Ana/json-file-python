'''
Criar e Ler um CSV: Crie um arquivo CSV chamado alunos.csv com os dados de 3 alunos
(Nome, Idade, Nota). Em seguida, leia e exiba o conteúdo no console

Senhor jesus
'''



import csv

with open('alunos.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['nome', 'idade', 'nota'])
    escritor.writerow(['João', 20, 9.5])
    escritor.writerow(['Maria', 22, 8.7])
    escritor.writerow(['Carlos', 19, 7.8])


with open('alunos.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

#Deixando o usuário decidir os dados a serem adiiconados no arquivo

while True:
    print('Adicionar mais um aluno?\n1 - Sim\n2 - Não\n3 - Ver lista de alunos')
    decisao = int(input('- '))

    if decisao == 1:
        nome = input('Digite o nome do aluno: ')
        idade = int(input('Digite a idade do aluno: '))
        nota = float(input('Digite a nota do aluno: '))
        with open('alunos.csv', 'a', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([nome, idade, nota])
        print('Aluno registrado.')

    elif decisao == 2:
        print('Ok, até uma próxima')
        break

    elif decisao == 3:
        with open('alunos.csv', 'r') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)

    else:
        print('Opção inválida, tente novamente')
        continue