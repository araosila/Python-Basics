import tkinter as tk

pencere = tk.Tk()
pencere.title("Ad Soyad Penceresi")
pencere.geometry("350x350")

etiket_ad = tk.Label(pencere, text="Ad:" , font=("Arial",14) )
etiket_ad.pack(pady=10)
giris_ad = tk.Entry(pencere)
giris_ad.pack(pady=10)

etiket_soyad = tk.Label(pencere, text="Soyad:" , font=("Arial",14) )
etiket_soyad.pack(pady=10)
giris_soyad = tk.Entry(pencere)
giris_soyad.pack(pady=10)


etiket_sonuc = tk.Label(pencere, text="", fg="red" , font=("Arial",14) )
etiket_sonuc.pack(pady=10)


def yazdir():
    ad = giris_ad.get()
    soyad = giris_soyad.get()
    etiket_sonuc.config(text=f"{ad} {soyad}")


buton_yazdir = tk.Button(pencere, text="Yazdır",font=("Arial",14) ,  command=yazdir)
buton_yazdir.pack(pady=10)


pencere.mainloop()

