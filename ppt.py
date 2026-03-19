import random
escolha = ['pedra','papel','tesoura']
def jogo():
  pessoa = input('Pedra, Papel ou Tesoura?').lower()
  while pessoa not in escolha:
    print('jogada invalida')
    pessoa = input('Pedra, Papel ou Tesoura?').lower()
  maquina = random.choice(escolha)
  print(f'Voce escolheu {pessoa}')
  print(f'A maquina escolheu {maquina}')
  if pessoa == maquina:
    print("empate")
  elif pessoa == 'pedra' and maquina == 'tesoura':
    print('voce venceu')
  elif pessoa == 'tesoura' and maquina == 'papel':
    print('voce venceu')
  elif pessoa == 'papel' and maquina == 'pedra':
    print('voce venceu')
  else:
    print('voce perdeu')
  continuar = input('Deseja continuar? S/N').lower()
while True:
  jogo()
  continuar = input('Deseja continuar? S/ N').lower()
  while continuar != 's' and continuar != 'n':
    continuar = input('Deseja continuar? S/N').lower()
  if continuar == 'n':
    print('Fim de jogo')
    break
  else:
      print('-'*80)