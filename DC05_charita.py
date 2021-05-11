# Charita
# Fundraisingová charita se anží udělat si pořádek ve svých dárcích 
# a odměňovat je podle výše příspěvku pohlednicemi.

class Charita:
    def __init__(self, name, address, contribution, card):
        self.name = name
        self.address = address
        self.contribution = contribution
        self.card = False
    
    def typ_prani(self):
        if self.card == False:
            if self.contribution >= 1000:
                return f"Děkujeme za Váš štědrý příspěvěk {self.contribution} Kč, posíláme Vám pohlednice vytvořené našimi svěřenci"
            else:
                return f"Děkujeme Vám za příspěvěk pro naše svěřence."
        else:
            return f"Přání již bylo odesláno"
    
    def deliver(self):
        self.card = True


p1 = Charita("Jiri Novak", "Nadrazni 321, Brno", 450, False)
p2 = Charita("Anna Kolinska", "Znojemska 22, Brno", 1200, False)



print(p1.typ_prani())
print(p2.typ_prani())
p2.deliver()
print(p2.typ_prani())

