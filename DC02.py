# Domácí cvičení 2. lekce

# 9) Ověřování věku

veky = [35, 12, 44, 11, 18, 21, 28, 18]

do_18 = [18 - v for v in veky]
nad_18 = [v >= 18 for v in veky]
presne_18 = [v == 18 for v in veky]

#11) Počty obyvatel

kraje = [
  ['Hlavní město Praha', '1 280 508'],
  ['Jihočeský kraj', '638 782'],
  ['Jihomoravský kraj', '1 178 812'],
  ['Karlovarský kraj', '296 749'],
  ['Kraj Vysočina', '508 952'],
  ['Královéhradecký kraj', '550 804'],
  ['Liberecký kraj', '440 636'],
  ['Moravskoslezský kraj', '1 209 879'],
  ['Olomoucký kraj', '633 925'],
  ['Pardubický kraj', '517 087'],
  ['Plzeňský kraj', '578 629'],
  ['Středočeský kraj', '1 338 982'],
  ['Ústecký kraj', '821 377'],
  ['Zlínský kraj', '583 698']
]

kraje_jmena = [jm[0] for jm in kraje]

# int() is build it funcion
# replace() 

kraje_cisla0 = [jm[1] for jm in kraje]
kraje_cisla1 = [jm.replace(' ','') for jm in kraje_cisla0]
kraje_cisla = [int(jm) for jm in kraje_cisla1]

print(kraje_jmena)
print(kraje_cisla)

kraje_transp = [kraje_jmena, kraje_cisla]