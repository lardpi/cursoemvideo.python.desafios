print('XECAUTE Versão 25.2.21 \n\n')
condicoes = {1:'Dinheiro/Cheque',2:'Cartão Débito',3:'Cartão Crédito até 2x',4:'Cartão Crédito 3x em diante'}
precoNormal = float(input('Digite o valor total dos produtos da compra: R$ '))
print('-'*15)
print(condicoes,'\n')
condicao = int(input('Digite o código da condição de pagamento desejada: '))
if condicao == 1:
    precoAjustado = precoNormal-precoNormal*0.1
elif condicao == 2:
    precoAjustado = precoNormal-precoNormal*0.05
elif condicao == 3:
    precoAjustado = precoNormal
elif condicao == 4:
    precoAjustado = precoNormal+precoNormal*0.2
else:
    precoAjustado = 0
    print('Opção inválida!')
print('\nO valor da compra ajustado de acordo com a condição de pagamento desejada é R$ {:.2f}.'.format(precoAjustado))

