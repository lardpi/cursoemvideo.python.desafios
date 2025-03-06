#Curso em Vídeo Python
#Mundo 2
#DESAFIO 051
print('PALINDROMANIA 27.2.25')
print('Passe-me uma palavra ou frase para eu verificar se ela é um palíndromo. Não use acentuação e nem pontuação.')
frase = str.upper(input('Digite uma palavra ou frase: '))
frSemEspaco = str.replace(frase,' ','')
invertida = frSemEspaco[::-1]
if invertida == frSemEspaco:
    print('O texto digitado é um palíndromo!')
else:
    print('O texto digitado NÃO é um palíndromo.')
