#DC04
#Měsíc narození

rc = int(input("Zadej své rodné číslo (bez lomítka): "))

def monthOfBirth(rc):
    rc_str = str(rc)
    mesic = int(rc_str[2:4])

    hlaska = "Rodné číslo bylo zadáno chybně."


    if mesic <= 12:
        return mesic
    elif mesic <= 50:
        return hlaska
    elif mesic <= 62:
        return mesic - 50
    elif mesic > 62:
        return hlaska

print(monthOfBirth(rc))

