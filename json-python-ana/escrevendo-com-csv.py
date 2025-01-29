import csv

with open ('saida.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['nome', 'idade', 'cidade'])
    escritor.writerow(['João', 30, 'São paulo'])
    print(arquivo)