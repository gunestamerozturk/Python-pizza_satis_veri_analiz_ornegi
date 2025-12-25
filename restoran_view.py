import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from restoran import *

BG_MAIN = "#1f1f1f"
BG_CARD = "#2b2b2b"
BG_PLOT = "#2b2b2b"
FG_TEXT = "#ffffff"
yesil = "#4CAF50"
kirmizi = "#FF6B6B"

def restoran_icerik(self,restoran_ad):
        #restoran_ad = "Pizza Hut"
        frame = ctk.CTkFrame(self.tabview.tab(restoran_ad))
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        for i in range(4): 
            for j in range(3):  # 3 sütun
                # Her hücre için frame
                cell = ctk.CTkFrame(frame, corner_radius=12, border_width=0, fg_color=BG_CARD)
                cell.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
                
                # Grid boyutlandırma
                for c in range(3):
                    frame.grid_columnconfigure(c, weight=1, uniform="x")

                #for r in range(4):
                    #frame.grid_rowconfigure(r, weight=1, uniform="y")
                frame.grid_rowconfigure(0, weight=1)   # KPI satırı (ince)
                frame.grid_rowconfigure(1, weight=3)
                frame.grid_rowconfigure(2, weight=3)
                frame.grid_rowconfigure(3, weight=4)  


                frame.pack(fill="both",expand=True)
                
                # 1. satır, 1. sütun (0,0) - Toplam kayıt sayısı
                if i == 0 and j == 0:
                    restoran_satis_toplami = rst_toplam_satis(restoran_ad)  # Excel dosyasından oku
                    label = ctk.CTkLabel(cell, 
                                       text=f"Toplam Kayıt Sayısı:\n\n{restoran_satis_toplami}", 
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #1. Satır, 2. Sütun
                if i == 0 and j == 1:
                    restoran_teslimat_suresi = rst_ortalama_teslimat_suresi(restoran_ad)  # Excel dosyasından oku
                    strcolor = FG_TEXT
                    if restoran_teslimat_suresi >= 30:
                        strcolor = kirmizi
                    else:
                        strcolor = yesil
                    label = ctk.CTkLabel(cell, 
                                       text=f"Ortalama Teslimat Süresi:\n\n{restoran_teslimat_suresi}\nDakika", 
                                       text_color=strcolor,
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #1.Satır 3. Sütun
                if i == 0 and j == 2:
                    restoran_gecikme = rst_gecikme_orani(restoran_ad)  # pyright: ignore[reportUndefinedVariable] # Excel dosyasından oku
                    strcolor = FG_TEXT
                    if restoran_gecikme >= 25:
                        strcolor = kirmizi
                    else:
                        strcolor = yesil
                    label = ctk.CTkLabel(cell, 
                                       text=f"Geciken Sipariş Ortalaması:\n\n{restoran_gecikme}%",
                                       text_color=strcolor, 
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)
                #2.Satır 1. Sütun
                if i == 1 and j == 0:
                    cok_satan_sube = rst_en_cok_satan_sube(restoran_ad)  # Excel dosyasından oku
                    label = ctk.CTkLabel(cell, 
                                       text=f"En Çok Satan Şube:\n\n{cok_satan_sube['Location']}\n{cok_satan_sube['satis_sayisi']} Adet", 
                                       text_color=yesil,
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)
                    #2.Satır 1. Sütun
                if i == 2 and j == 0:
                    az_satan_sube = rst_en_az_satan_sube(restoran_ad)  # Excel dosyasından oku
                    label = ctk.CTkLabel(cell, 
                                       text=f"En Az Satan Şube:\n\n{az_satan_sube['Location']}\n{az_satan_sube['satis_sayisi']} Adet", 
                                       text_color=kirmizi,
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)
                #2.Satır 2. Sütun
                #2.Satır 1. Sütun
                if i == 1 and j == 1:
                    en_dusuk_gecikme_orani_sube = rst_gecikme_orani_en_dusuk_sube(restoran_ad)  # Excel dosyasından oku
                    strcolor = FG_TEXT
                    if en_dusuk_gecikme_orani_sube["gecikme_orani"] >= 25:
                        strcolor = kirmizi
                    else:
                        strcolor = yesil
                    label = ctk.CTkLabel(cell, 
                                       text=f"Gecikme Oranı En Düşük Şube:\n\n{en_dusuk_gecikme_orani_sube['restoran']}\n{en_dusuk_gecikme_orani_sube['gecikme_orani']}%", 
                                       text_color=strcolor,
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)
                #2.Satır 1. Sütun
                if i == 1 and j == 2:
                    en_yuksek_gecikme_orani_sube = rst_gecikme_orani_en_yuksek_sube(restoran_ad)  # Excel dosyasından oku
                    strcolor = FG_TEXT
                    if en_yuksek_gecikme_orani_sube["gecikme_orani"] >= 25:
                        strcolor = kirmizi
                    else:
                        strcolor = yesil
                    label = ctk.CTkLabel(cell, 
                                       text=f"Gecikme Oranı En Yüksek Şube:\n\n{en_yuksek_gecikme_orani_sube['restoran']}\n{en_yuksek_gecikme_orani_sube['gecikme_orani']}%", 
                                       text_color=kirmizi,
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #3.Satır 2. Sütun
                if i == 2 and j == 1:
                    en_cok_tercih_odeme_methodu = rst_odeme_yontemi(restoran_ad)  # Excel dosyasından oku
                    label = ctk.CTkLabel(cell, 
                                       text=f"En Çok Tercih Edilen Ödeme Yöntemi:\n\n{en_cok_tercih_odeme_methodu['odeme_method']}\n{en_cok_tercih_odeme_methodu['satis_sayisi']} Adet", 
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #3.Satır 3. Sütun
                if i == 2 and j == 2:
                    en_cok_tercih_siparis_methodu = rst_siparis_yontemi(restoran_ad)  # Excel dosyasından oku
                    label = ctk.CTkLabel(cell, 
                                       text=f"En Çok Tercih Edilen Sipariş Yöntemi:\n\n{en_cok_tercih_siparis_methodu['Method']}\n{en_cok_tercih_siparis_methodu['Oran']}%", 
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #4. Satır 1. Sütun Saatlik satış
                if i == 3 and j ==0:
                    veriler=rst_saatlik_satis_grafigi(restoran_ad)

                    fig,ax = plt.subplots(figsize=(4,2), dpi=100)
                    fig.patch.set_facecolor("#2b2b2b")
                    ax.set_facecolor("#2b2b2b")
                    fig.subplots_adjust(top=0.80,bottom=0.20,left=0.10,right=0.95)

                    ax.bar(veriler["Saatler"],veriler["Siparisler"])
                    ax.set_xlabel("Saat",color="white")
                    ax.set_ylabel("Toplam Sipariş",color="white")
                    ax.set_title("Saatlik Yoğunluk",color="white")

                    ax.tick_params(axis="x", colors="white")
                    ax.tick_params(axis="y", colors="white")

                    canvas = FigureCanvasTkAgg(fig, master=cell)
                    canvas.draw()
                    canvas.get_tk_widget().pack(fill="both", expand=True,padx=10,pady=10)

                    plt.close(fig)
                
                #4.Satır 2.Sütun Aylık Satış
                if i == 3 and j == 1:
                    veri = rst_aylik_satis_grafigi(restoran_ad,"Order Month")

                    aylar = veri["aylar"]
                    satislar = veri["satislar"]

                    # Matplotlib Figure
                    fig, ax = plt.subplots(figsize=(4, 2), dpi=100)
                    fig.patch.set_facecolor(BG_PLOT)  # Dark theme uyumu
                    ax.set_facecolor(BG_PLOT)
                    fig.subplots_adjust(top=0.80,bottom=0.20,left=0.10,right=0.95) #Yazıların taşmasını engellemek için boşluk bıraktık

                    ax.plot(aylar, satislar, marker="o") #Çizgi Grafiği
                    ax.set_title("Aylık Satış Grafiği", color="white")
                    #ax.set_xlabel("Ay", color="white")
                    ax.set_ylabel("Satış Adedi", color="white")

                    ax.tick_params(axis='x', colors='white', rotation=45)
                    ax.tick_params(axis='y', colors='white')

                    # Grafiği CustomTkinter içine gömme
                    canvas = FigureCanvasTkAgg(fig, master=cell)
                    canvas.draw()
                    canvas.get_tk_widget().pack(fill="both", expand=True)
                    plt.close(fig)

                #4.Satır 3. Sütun (1,2) - Pizza Tipi Grafiği                   
                if i == 3 and j == 2: 
                    veri = rst_pizza_tipi_grafigi(restoran_ad,"Pizza Type")

                    pizzalar = veri["Pizza Tipleri"]
                    satislar = veri["satislar"]

                    # Matplotlib Figure
                    fig, ax = plt.subplots(figsize=(4, 2), dpi=100)
                    fig.patch.set_facecolor("#2b2b2b")  # Dark theme uyumu
                    ax.set_facecolor("#2b2b2b")
                    fig.subplots_adjust(top=0.80,bottom=0.20,left=0.10,right=0.95)

                    ax.bar(pizzalar, satislar) #Sütun Grafiği 
                    ax.set_title("Pizza Tipi Grafiği", color="white")
                    #ax.set_xlabel("Pizza Tipi", color="white")
                    ax.set_ylabel("Satış Adedi", color="white")

                    ax.tick_params(axis='x', colors='white', rotation=45)
                    ax.tick_params(axis='y', colors='white')

                    # Grafiği CustomTkinter içine gömme
                    canvas = FigureCanvasTkAgg(fig, master=cell)
                    canvas.draw()
                    canvas.get_tk_widget().pack(fill="both", expand=True,padx=10,pady=15)
                    plt.close(fig)