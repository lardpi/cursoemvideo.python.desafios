tabela = ('Fortaleza','Juventude','Vasco','Cruzeiro','Grêmio',
'Bragantino','Ceará','Corinthians','Flamengo','Internacional',
'Bahia','São Paulo','Sport','Botafogo','Palmeiras',
'Atlético-MG','Santos','Mirassol','Fluminense','Vitória')
print('Tabela do Brasileirão em 31/03/2025')
print('A) Os 5 primeiros colocados são:')
print(tabela[0:5])
print('B) Os últimos 4 colocados são:')
print(tabela[-4:])
print('C) Os clubes ordenados são:')
print(sorted(tabela))
print(f'D) Em que posição está o Corinthians: {tabela.index("Corinthians")}.')
