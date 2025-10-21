yas = int(input("Yaşınızı giriniz :"))
kilo = int(input("Kilonuzu giriniz : "))

if yas <= 30 :
    print("Genç")
elif yas >= 60 :
    print("Yaşlı")
else:
    print("Yetişkin")
    
if kilo <= 50 :
    print("Zayıf")
elif kilo >= 80 :
    print("Kilolu")
else:
    print("Normal")
    