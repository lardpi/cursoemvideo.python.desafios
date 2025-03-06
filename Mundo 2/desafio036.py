print('### EMPRESTAÍ 1.0 ###')
valorImovel = float(input('Informe o valor total do imóvel a ser comprado: R$ '))
salarioBruto = float(input('Informe o seu salário bruto mensal: R$ '))
percTeto = 0.3
tetoPrestacao = salarioBruto*percTeto
prazoEmAnos = int(input('Informe o prazo para pagamento (quantidade de anos): '))
prazoEmMeses = prazoEmAnos*12
prestacaoMensal = valorImovel/prazoEmMeses
if prestacaoMensal > tetoPrestacao:
    print('Infelizmente seu empréstimo será negado, pois a parcela mensal (R$ {:.2f}) é superior ao teto da prestação (R$ {:.2f}) para este caso.'.format(prestacaoMensal,tetoPrestacao))
else: print('Empréstimo aprovado! Traga o restante da documentação para prosseguirmos com o processo.')
