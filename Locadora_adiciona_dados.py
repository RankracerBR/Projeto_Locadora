import csv 

filme_1 = ['The Batman', 'Matt Reeves', '2022', True]
filme_2 = ['Doutor Estranho 2', 'Sam Raimi','2022',True]
filme_3 = ['Seven, os sete pecados', 'David Fincher', '1997', False] 

acervo = [filme_1, filme_2, filme_3] 


#Anota os dados no arquivo Locadora_dados.csv
with open('locadora_dados_6.csv','w') as arquivo:
   csv_writer = csv.writer(arquivo,delimiter=',')
   for linha in acervo:
         csv_writer.writerow(linha)
        
#Lê  os arquivos na Locadora_csv
with open('dados.csv','r') as arquivo:
  reader = csv.reader(arquivo,delimiter=',')
  dados = list(reader)

print(dados)