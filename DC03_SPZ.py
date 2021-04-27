#Poznávací značky

#Napiš kód, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji,
#tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}



značky = list(plates.keys()) #převedu dic na list, aby bylo možné použít index
print(značky)


for značky, jmeno in plates.items():
    if značky[1] == 'P':
        print(jmeno)