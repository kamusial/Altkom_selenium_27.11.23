class Auto:
    def __init__(self, barwa, stan, wiek):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = stan
        self.tryb_ekonomicnzy = False
        self.spalanie_na_100 = 14
        self.rocznik = 2023 - wiek




moje_auto = Auto('black', 3, 12)
print(moje_auto.kolor)
