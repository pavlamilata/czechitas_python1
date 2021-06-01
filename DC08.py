#DC08 Recept

recept = {
  'nazev': 'Batáty se šalvějí a pancettou',
  'narocnost': 'stredni',
  'doba': 30,
  'ingredience': [
    ['batát', '1', '15 kč'],
    ['olivový olej', '2 lžíce', '2 kč'],
    ['pancetta', '4-6 plátků', '21 kč'],
    ['přepuštěné máslo', '2 lžíce', '5 kč'],
    ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
    ['sůl', '1/2 lžičky', '0.1 kč'],
    ['muškátový oříšek', 'špetka', '1 kč'],
    ['česnek', '2 stroužky', '1 kč'],
    ['šalvějové lístky', '20-25', '12 kč']
  ]
}

print( round( sum( [ float(x[-1].split()[0]) for x in recept['ingredience'] ] ) ) )


## Jednotlivé kroky
# 1) Vytvoření seznamu s informací o ceně
ceny = [ingredience[-1] for ingredience in recept['ingredience']]
# 2) Převedení ceny na číslo
# Nejdříve jdem rozkouskovala pomocí bílých znaků a pomocí indexace jsem vybrala první hodnotu
# Následně jsem převedla na číslo
cena_cislo = [cena.split()[0] for cena in ceny]
celkova_cena = [float(cena )for cena in cena_cislo]

# 3) Sečíst a zaokrouhlit
print(f"Celé jídlo bude stát: { round( sum(celkova_cena))} Kč")
