class Produs(object):
    def __init__(self, denumire, pret, cantitate, owner, an_productie):
        self.denumire = denumire
        self.pret = pret
        self.cantitate = cantitate
        self.owner = owner
        self.an_productie = an_productie

    def aplica_reducere(self, procent):
        self.pret = self.pret - self.pret / 100 * procent
    
    def restocare(self, numar):
        if numar > 0:
            self.cantitate = self.cantitate + numar
        else:
            print(f'{numar} nu este un numar valid')


class Aliment(Produs):
    def __init__(self, denumire, pret, cantitate, owner, an_productie, an_expirare, tip, greutate, este_bio = False, este_vegan = False):
        self.an_expirare = an_expirare
        self.tip = tip
        self.greutate = greutate
        self.este_bio = este_bio
        self.este_vegan = este_vegan
        super().__init__(denumire, pret, cantitate, owner, an_productie)
    
    def este_expirat(self):
        if self.an_expirare < 2020:
            return True
        else:
            return False
    
    def este_sanatos(self):
        if self.este_bio and self.este_vegan:
            return True
        else:
            return False

potato_chips = Aliment("Lay's", 5, 200, "PepsiCo", 2020, 2021, "snack", 100, False, True)
corn_chips = Aliment("Doritos", 4, 100, "PepsiCo", 2020, 2022, "snack", 80)
cola = Aliment("Coca-Cola", 7, 500, "The Coca-Cola Company", 2019, 2022, "bautura", 2000, False, True)
fanta = Aliment("Fanta", 6, 250, "The Coca-Cola Company", 2018, 2019, "bautura", 2000, False, True)
pepsi = Aliment("Pepsi", 6, 300, "PepsiCo", 2019, 2021, "bautura", 2000, False, True)
print(fanta.este_expirat())
print(potato_chips.este_sanatos())
print(pepsi.pret)
pepsi.aplica_reducere(50)
print(pepsi.pret)
print(corn_chips.cantitate)
corn_chips.restocare(100)
print(corn_chips.cantitate)