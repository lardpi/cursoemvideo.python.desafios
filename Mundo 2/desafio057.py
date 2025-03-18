#Curso em Vídeo
#Python 3 - Mundo 02
#Desafio 057
sexo = ''
while sexo == '' or sexo not in ('FfMm'):
    sexo = str(input('Informe o sexo da pessoa a ser cadastrada (M - masculino; F - feminino): '))
    if sexo not in ('FfMm'):
        print('Opção inválida!')
print('Obrigado. Informação salva com sucesso!')    
