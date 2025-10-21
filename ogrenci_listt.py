class sinif:
    def __init__(self,no,ad,soyad,adres):
        self.no = no 
        self.ad = ad
        self.soyad = soyad
        self.adres = adres
        
    def bilgi_goster(self):
        print(f"No:{self.no},Ad:{self.ad},Soyad:{self.soyad},Adres:{self.adres}")
        
ogrenci1 = sinif("1", "Sıla","Kart","Trabzon")
ogrenci2 = sinif("2","Nisanur", "Çimen","Gümüşhane")

ogrenci1.bilgi_goster()
ogrenci2.bilgi_goster()
