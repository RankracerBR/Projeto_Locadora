import os
import Locadora_funcoes as f

acervo = f.ler_dados()

op = 1
while op != 0:
  os.system('cls')
  
  f.criar_cabecalho()
  op = f.menu()

  if op == 1:
    os.system('cls')
    f.listar_filmes(acervo)
    input('\n\ndigite ENTER para continuar: ')
  elif op == 2:
    os.system('cls')
    f.cadastrar_filmes(acervo)
  elif op == 3:
    os.system('cls')
    f.pesquisar_filme(acervo)
    input('aperte ENTER para continuar')
  elif op == 4:
    os.system('cls')
    f.salvar_dados(acervo)
    input('aperte ENTER para continuar')
  elif op == 0:
    print('Até mais humano!')
  else:
    os.system('cls')
    print('Opção inválida')
    input('aperte ENTER para continuar')