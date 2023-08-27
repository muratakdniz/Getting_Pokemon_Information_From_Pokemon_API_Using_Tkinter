import requests
from tkinter import *
from PIL import Image, ImageTk

ekran = Tk()
ekran.title("Getting Pokemon Information from Pokemon Api")
ekran.geometry("700x680")

baslik = Label(text="Pokemon")
baslik.pack()
baslik.config(padx=10,pady=10,font=("Pokemon Solid",15,"normal"),fg="dark blue")

resim = ImageTk.PhotoImage(Image.open("pokemon.jpg"))

pokemon_resim = Label(image=resim,width=400, height=209)
pokemon_resim.pack()

yazi= Label(text="Pokemon İsmini Giriniz:")
yazi.pack()
yazi.config(padx=20,pady=20,font=("Arial",12,"normal"))

yazi_entry = Entry(width=50)
yazi_entry.pack(padx=15,pady=15)

def pokemon_bilgisi_alma():
    pokemon_isim = yazi_entry.get()
    pokemon_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_isim

    response = requests.get(pokemon_url)

    if response.status_code == 200:
        data = response.json()
        isim = data['name']
        yukseklik = data['height']
        agirlik = data["weight"]
        turler = [t['type']['name'] for t in data['types']]

        sonuc_yazisi.config(text=f"İsmi: {isim}\n Yüksekliği: {yukseklik}\n Ağırlığı: {agirlik}\n Türleri: {turler}")
    else:
         sonuc_yazisi.config(text="Pokemon bulunamadı! Lütfen geçerli bir isim girin.")
def cikis():
    ekran.quit()

button = Button(text="Pokemon Bilgisini Getir",bg="white", fg="#393E46",command=pokemon_bilgisi_alma)
button.pack()
button.config(padx=10,pady=10)

cikis_button = Button(text="Çıkış",bg="white",fg="#393E46",command=cikis)
cikis_button.pack()
cikis_button.config(padx=10,pady=10)

sonuc_yazisi = Label(text="")
sonuc_yazisi.pack()
sonuc_yazisi.config(padx=10,pady=10,font=("Arial",14,"normal"),fg="#00ADB5")

ekran.mainloop()
