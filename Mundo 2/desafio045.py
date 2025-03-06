import random,time
print('JKP Lite\n\n')
opcoes = {1:'Pedra',2:'Papel',3:'Tesoura'}
print('Você vai jogar uma partida de Jan-Ken-Pô comigo! Vamos lá!\n')
opcaoPC = random.randint(1,3)
opcao = int(input('{}\nJá escolhi minha opção. Escolha a sua: '.format(opcoes)))
print('J-A-N')
time.sleep(1)
print('K-E-N')
time.sleep(1)
print('P-Ô\n')
if opcao not in (opcoes):
    print('Opção inválida!')
else:
    print('Você escolheu {} e eu escolhi {}.\n'.format(opcoes[opcao],opcoes[opcaoPC]))
    resultado = opcaoPC+opcao
    ganhou = 0
    if opcao != opcaoPC:
        if resultado == 3:
            ganhou = 2
        elif resultado == 4:
            ganhou = 1
        else:
            ganhou = 3
    else:
        print('Ah! Nós dois escolhemos {}. Deu empate...'.format(opcoes[opcao]))
    if ganhou > 0:
        if opcao == ganhou:
            print('Parabéns! {} ganha de {}. Você ganhou!'.format(opcoes[opcao],opcoes[opcaoPC]))
        else:
            print('A-ha! {} ganha de {}. Eu ganhei!'.format(opcoes[opcaoPC],opcoes[opcao]))

        
