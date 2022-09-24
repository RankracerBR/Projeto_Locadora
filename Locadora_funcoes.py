import os
import csv
import time

passos = '🏃'

def listar_filmes(lista):
  print(f'Existem {len(lista)} filmes cadastrados\n\n')
  print('Título'.ljust(30,' '), 'Diretor'.ljust(30,' '),'Ano'.ljust(30,' '),'Disponibilidade'.ljust(30,' '))
  print('-'*120)

  for filme in lista:
    for info in filme[0:-1]:
      print(info.ljust(30,' '),end='|')
    if filme[-1] == 'True':
      print('Alugado'.ljust(30,' '))
    else:
      print('Disponível'.ljust(30,' '))
    
def criar_cabecalho():
  tamanho = os.get_terminal_size()
  largura = tamanho[0]
  print('-'*largura)
  print('PyBuster'.center(largura))
  print('-'*largura)

def menu():
  print('Menu de opções: ')
  print('1 - Listar Filmes\n2 - Cadastrar Filmes\n3 - Pesquisar\n4 - Salvar Dados\n0 - SAIR')
  op = int(input('\nInforme a sua opção: '))
  return op

def cadastrar_filmes(dados):
  resp = 'sim'
  while resp == 'sim':
    titulo = input('Informe o título do filme: ')
    diretor = input('Informe o diretor do filme: ')
    ano = input('Informe o ano do filme: ')
    filme = [titulo,diretor,ano,True]
    dados.append(filme)
    resp = input('Deseja cadastrar outro filme: ').lower()

def pesquisar_filme(dados):
  palavra = input('Informe a palavra para pesquisar: ')
  palavra = palavra.lower()
  resultados = []
  for filme in dados:
    if palavra in filme[0].lower():
      resultados.append(filme)    
  
  listar_filmes(resultados)

def salvar_dados(dados):
  print(f'Salvando os dados...{passos}')
  with open('Locadora_dados_6.csv','w') as arquivo:
    writer = csv.writer(arquivo,delimiter=',')
    for linha in dados:
      writer.writerow(linha)
    time.sleep(3)
  print('Dados salvos com sucesso!')

def ler_dados():
  with open('Locadora_dados_6.csv','r') as arquivo:
    reader = csv.reader(arquivo,delimiter=',')
    dados = list(reader)
    return dados

