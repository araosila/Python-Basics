sayi1 = int(input("1.sayı : "))
sayi2 = int(input("2.sayı : "))
islem = input("İşlem seç (+ - * /) : ")

if islem == "+":
    print("Sonuç : " , sayi1+sayi2)
elif islem == "-":
    print("Sonuç : " , sayi1-sayi2)
elif islem == "*":
    print("Sonuç : " , sayi1*sayi2)
elif islem == "/":
    print("Sonuç : ", sayi1/sayi2)
else:
    print("Geçersiz işlem!")
    