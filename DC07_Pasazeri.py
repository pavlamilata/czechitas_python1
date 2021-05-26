#DC07_Pasazeri


with open('pasazeri.txt', encoding='utf-8') as vstup:
    jizdy = []
    for radek in vstup:
        radek = radek.strip('\n')
        radek = radek.split(' ')

    den =  [[int(jizda.split(',')[0]) for jizda in radek],[int(jizda.split(',')[1]) for jizda in radek] ]
    jizdy.append(den) 

#print(jizdy)

tam = 0
zpet = 0
for den in jizdy:
    tam += sum(den[0])
    zpet += sum(den[1])
print('První den tam:', sum(jizdy[0][0]), 'a zpet:', sum(jizdy[0][1]))
print('Celkem za týden tam:', tam, 'a zpet:', zpet)