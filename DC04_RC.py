#DC04
#Měsíc narození

rc = int(input("Zadej své rodné číslo (bez lomítka): "))


def monthOfBirth(rc):
    rc_str = str(rc)
    hlaska = (f"Rodné číslo bylo zadáno chybně.")

    if int(rc_str[2:4]) <= 12:
        return int(rc_str[2:4])
    elif int(rc_str[2:4]) <= 50:
        return(hlaska)
    elif int(rc_str[2:4]) <= 62:
        return int(rc_str[2:4]) - 50
    elif int(rc_str[2:4]) > 62:
        return(hlaska)

print(monthOfBirth(rc))

