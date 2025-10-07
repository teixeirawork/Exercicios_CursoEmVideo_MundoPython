# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do SANTOS.

print('-=|*|=-' * 3,'MOD 03 EXC TABELA BRASILEIRAO','-=|*|=-' * 3)

times =('Flamengo','Cruzeiro','Palmeiras','Bahia','Botafogo','Mirassol','São Paulo',
'Bragantino','Fluminense','Internacional','Ceará SC','Corinthians','Grêmio',
'Atlético-MG','Vasco da Gama','Santos','EC Vitória','Juventude','Fortaleza',
'Sport Recife')

print('Os Primeiros colocados são: \n',times[:5],'\n')

print('Os últimos colocados são: \n',times[-4:],'\n')

print('Os times em ordem alfabética: \n',sorted(times))

print('A posição do Santos é: ',times.index('Santos')+1,'ºColocado')

print('-=|*|=-' * 3,'MOD 03 EXC TABELA BRASILEIRAO','-=|*|=-' * 3)
