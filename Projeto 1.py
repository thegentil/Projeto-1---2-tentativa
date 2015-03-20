# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:24:27 2015

@author: nicogentil
"""

inicio = 6

while inicio == 6:
    
    from random import choice
    
    placar_j = 0
    placar_pc = 0
    
    print('Bem vindo ao jogo: Pedra Papel Tesoura Lagarto Spock! Para ganhar vc deve vencer o pc 3 vezes seguidas! Boa sorte...\n')
    
    while placar_j < 3 and placar_pc <3:
        
        print('O pc está pronto\n')
        
        opc = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
        
        escolha = choice(opc)
        
        pc = opc.index(escolha) + 1  # faz com que a escolha do pc se transforme em um número   
        
        pedra = 1
        papel = 2
        tesoura = 3
        lagarto = 4
        spock = 5
        
        pjogador = input('Faca a sua escolha:\n')
        
        jogador = opc.index(pjogador) + 1  # faz com que a escolha do jogador se transforme em um número
        
        if jogador == 1 and pc == 1:
            print('Empate! Ambos escolheram pedra!\n')
            
        if jogador == 1 and pc == 2:
            print('Vc perdeu! O pc embrulhou a sua pedra com papel!\n')
            placar_pc += 1
            placar_j = 0
            
        if jogador == 1 and pc == 3:
            print('Vc ganhou! Sua pedra destruiu a tesoura do pc!\n')
            placar_j += 1
            placar_pc = 0
            
        if jogador == 1 and pc == 4:
            print('Vc ganhou! Sua pedra esmagou o lagarto do pc!\n')    
            placar_j += 1
            placar_pc = 0
            
        if jogador == 1 and pc == 5:
            print('Vc perdeu! O spock vaporizou a sua pedra!\n')
            placar_pc += 1
            placar_j = 0
            
        if jogador == 2 and pc == 1:
            print('Vc ganhou! Seu papel embrulhou a pedra do pc!\n')
            placar_j += 1
            placar_pc = 0
            
        if jogador == 2 and pc == 2:
            print('Empate! Ambos escolheram papel\n')
            
        if jogador == 2 and pc == 3:
            print('Vc perdeu! A tesoura do pc cortou o seu papel!\n')
            placar_pc += 1
            placar_j = 0
        
        if jogador == 2 and pc == 4:
            print('Vc perdeu! O lagarto do pc comeu o seu papel!\n')
            placar_pc += 1
            placar_j = 0
            
        if jogador == 2 and pc == 5:
            print('Vc ganhou! Seu papel refutou o spock!\n')
            placar_j += 1
            placar_pc = 0
            
        if jogador == 3 and pc == 1:
            print('Vc perdeu! A pedra do pc esmagou sua tesoura!\n')
            placar_pc += 1
            placar_j = 0
            
        if jogador == 3 and pc == 2:    
            print('Vc ganhou! Sua tesoura cortou o papel do pc!\n')
            placar_j += 1
            placar_pc = 0
            
        if jogador == 3 and pc == 3:    
            print('Empate! Ambos escolheram tesoura\n')
        
        if jogador == 3 and pc == 4:
            print('Vc ganhou! Sua tesoura decaptou o lagarto do pc!\n')
            placar_j += 1
            placar_pc = 0
            
        if jogador == 3 and pc == 5:
            print('Vc perdeu! O spock esmagou a sua tesoura!\n') 
            placar_pc += 1
            placar_j = 0
            
        if jogador == 4 and pc == 1:
            print('Vc perdeu! A pedra do pc esmagou o seu lagarto!\n')    
            placar_pc += 1
            placar_j = 0
            
        if jogador == 4 and pc == 2:
            print('Vc ganhou! Seu lagarto comeu o papel do pc!\n') 
            placar_j += 1
            placar_pc = 0
            
        if jogador == 4 and pc == 3:
            print('Vc perdeu! A tesoura do pc decaptou o seu lagarto!\n')
            placar_pc += 1
            placar_j = 0
            
        if jogador == 4 and pc == 4:
            print('Empate! Ambos escolheram lagarto\n')
        
        if jogador == 4 and pc == 5:
            print('Vc ganhou! Seu lagarto envenenou o spock!\n')
            placar_j += 1
            placar_pc = 0
            
        if jogador == 5 and pc == 1:
            print('Vc ganhou! O spock vaporizou a pedra do pc!\n')
            placar_j += 1
            placar_pc = 0
            
        if jogador == 5 and pc == 2:
            print('Vc perdeu! O papel do pc refutou o spock!\n') 
            placar_pc += 1
            placar_j = 0
            
        if jogador == 5 and pc == 3:
            print('Vc ganhou! O spock esmagou a tesoura do pc!\n')
            placar_j += 1
            placar_pc = 0
            
        if jogador == 5 and pc == 4:
            print('Vc perdeu! O lagarto do pc envenenou o spock!\n')
            placar_pc += 1
            placar_j = 0
            
        if jogador == 5 and pc == 5:
            print('Empate! Ambos escolheram spock\n')
            
            
        if (placar_j == 3 and placar_pc == 3) or placar_j == 3 or placar_pc == 3:
            inicio = 7
            restart = int(input('Fim do jogo! Se quiser jogar novamente, pressione 1\n'))
            
            if restart == 1:
               inicio = 6 
            