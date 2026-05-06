#jogo pedra papel tesoura
import random
opcao = ['pedra', 'papel', 'tesoura']
rodada_usuario = 0
rodada_computador = 0

while rodada_usuario < 3 and rodada_computador < 3:
    usuario = input("Escolha pedra, papel ou tesoura:\n").lower().strip()
    
    if usuario not in opcao:
         print('Escolha invalida')
         continue
    
    computador = random.choice(opcao)  
   
    
    if usuario == computador:
         print('\033[33mEmpate!\033[0m')

    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "papel" and computador == "pedra") or \
        (usuario == "tesoura" and computador == "papel"):
        print('\033[32mVocê ganhou!!\033[0m')
        rodada_usuario += 1

    else:
        print('\033[31mVocê perdeu!!\033[0m')
        rodada_computador += 1
    print (f'Placar:\n{rodada_usuario} X {rodada_computador}')

if rodada_usuario == 3:
     print('\033[32mVocê ganhou a partida!!\033[0m')
else:
     print('\033[31mVocê perdeu a partida!\033[0m')