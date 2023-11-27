class Auto:
    def __init__(self, barwa, stan, wiek):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = stan
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2023 - wiek

    def __str__(self):
        napis = (f'Auto ma kolor {self.kolor} i jest rocznik {self.rocznik + 3}')
        return napis

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 10
        elif tryb == 'normal':
            self.tryb_ekonomiczny = False
            self.spalanie_na_100 = 14
        else:
            print('bez zmian')



moje_auto = Auto('black', 3, 12)
print(moje_auto.kolor)
print(moje_auto.spalanie_na_100)
print(moje_auto.zasieg())
print(moje_auto)