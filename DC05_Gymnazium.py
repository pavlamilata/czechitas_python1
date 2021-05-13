#DC05 Gymnazium

#Požádejte uživatele o zadání známky z matematiky a průměru všech známek na posledním vysvědčení. 
# Pokud má zájemce průměr známek nižší než 1.8 a z matematiky nejhůře dvojku, vypište text: 
# "Přijmeme vás bez přijímací zkoušky.". V opačném případě vypište 
#"Musíte splnit přijímací zkoušku.".


zz = int(input("Prosím, zadejte Vaši závěrečnou známku z matematiky: "))
prumer = float(input("Prosím, zadejte průměr všech známek na posledním vysvědčení: "))

prumer = prumer < 1.8

if zz <= 2 and prumer:
    print("Přijmeme vás bez přijímací zkoušky.")
else:
    print("Musíte splnit přijímací zkoušku.")