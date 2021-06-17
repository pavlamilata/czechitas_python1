#DC10

import pandas as pd

jmena = pd.read_csv('jmena100.csv', encoding='utf-8')

# Vypište všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
print(jmena[jmena['věk'] > 60])

# Vypište pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
print(jmena[(jmena['četnost'] >= 80000) & (jmena['četnost'] <= 100000)]['jméno'])

# Vypište jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je?
slovansky = jmena[jmena['původ'].isin(['slovanský'])][['jméno', 'četnost']]
print(slovansky)
print(f'\nPočet: {slovansky.shape[0]}')

hebrejsky = jmena[jmena['původ'].isin(['hebrejský'])][['jméno', 'četnost']]
print(hebrejsky)
print(f'\nPočet: {hebrejsky.shape[0]}')
