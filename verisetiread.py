import pandas as pd 
veriler = pd.read_csv(r'D:\NTPPython\dataa.csv', encoding ='utf-8-sig', sep=';')
print("Tüm Veri Seti: ")
print(veriler)
print("\nSadece Adlar")

print(veriler['Ad'])
print("\nAd, Soyad, Ortalama")
print(veriler[['Ad', 'Soyad', 'Ortalama']])

