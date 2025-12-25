import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from genel_analiz import *

BG_MAIN = "#1f1f1f"
BG_CARD = "#2b2b2b"
BG_PLOT = "#2b2b2b"
FG_TEXT = "#ffffff"
yesil = "#4CAF50"
kirmizi = "#FF6B6B"

def sekme1_icerik(self):
        frame = ctk.CTkFrame(self.tabview.tab("Tümü"))
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # 3 sütun x 4 satır grid yapısı
        for i in range(4):  # 4 satır
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
                    kayit_sayisi = excel_kayit_sayisi()  # Excel dosyasından oku
                    label = ctk.CTkLabel(cell, 
                                       text=f"Toplam Kayıt Sayısı:\n\n{kayit_sayisi}", 
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                # 1. Satır 2. Sütun (0,1) - Ortalama Teslimat Süresi
                if i == 0 and j ==1:
                    ortalama_teslimat = ortalama_teslimat_suresi("Delivery Duration (min)")
                    strcolor = FG_TEXT
                    if ortalama_teslimat >= 30:
                        strcolor = kirmizi
                    else:
                        strcolor = yesil
                    label = ctk.CTkLabel(cell,
                                         text=f"Ortalama Teslimat Süresi:\n\n{ortalama_teslimat} Dakika",
                                         text_color = strcolor,
                                         font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #1. Satır 3. Sütun (0,2) - Gecikme Oranı
                if i == 0 and j ==2:
                    toplam_gecikme_orani = gecikme_orani("Is Delayed")
                    label = ctk.CTkLabel(cell,
                                         text=f"Gecikme Oranı:\n\n{toplam_gecikme_orani}%",
                                         font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #2.Satır 1. Sütun (1,0) - En Çok Satış Yapan Restoran                
                if i == 1 and j ==0:
                    cok_satan_restoran = en_cok_satan_restoran("Restaurant Name")
                    label = ctk.CTkLabel(cell,
                                         text=f"En Çok Satış Yapan Restoran:\n\n{cok_satan_restoran}\n",
                                         text_color = yesil,
                                         font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #2.Satır 2. Sütun (1,1) - En Çok Satış Yapan Şube                
                if i == 1 and j ==1:
                    cok_satan_sube = en_cok_satan_sube("Restaurant Name","Location")
                    label = ctk.CTkLabel(cell,
                                         text=f"En Çok Satış Yapan Şube:\n\n{cok_satan_sube['Restaurant Name']}\n{cok_satan_sube['Location']}\n\nSatış Adeti : {cok_satan_sube['satis_sayisi']}",
                                         text_color = yesil,
                                         font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True) 

                #2.Satır 3. Sütun (1,2) - Aylık Satış Grafiği
                if i == 3 and j == 0:
                    veri = aylik_satis_grafigi("Order Month")

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
                    plt.close(fig) #Tkinter döngüde kalıyor ve program kapanmıyordu, bu şekilde çözdük

                #Gecikme Oranı En Yüksek Restoran
                # 3. satır, 1. sütun (2,0) -
                if i == 2 and j == 0:
                    gecikme_orani_en_yuksek = gecikme_orani_en_yuksek_restoran("Restaurant Name","Is Delayed")  # Excel dosyasından oku
                    label = ctk.CTkLabel(cell, 
                                       text=f"Gecikme Oranı En Yüksek Restoran\n{gecikme_orani_en_yuksek['restoran']}\n{gecikme_orani_en_yuksek['gecikme_orani']}%", 
                                       text_color = kirmizi,
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #Tercih Edilen Ortalama Malzeme Sayısı
                #3. Satır 2. Sütun
                if i == 2 and j == 1:
                    kayit_sayisi = ortalama_malzeme_sayisi()  # Excel dosyasından oku
                    label = ctk.CTkLabel(cell, 
                                       text=f"Tercih Edilen Malzeme Sayısı Ortalama:\n\n{kayit_sayisi} Adet", 
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)
                #3.Satır 3. Sütun (1,2) - Pizza Tipi Grafiği                   
                if i == 3 and j == 2: 
                    veri = pizza_tipi_grafigi("Pizza Type")

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

                #Gecikme Oranı En Düşük Restoran
                #4. Satır 1. Sütun (3,0)
                #Gecikme Oranı En Yüksek Restoran
                # 3. satır, 1. sütun (2,0) -
                if i == 1 and j == 2:
                    gecikme_orani_en_dusuk = gecikme_orani_en_dusuk_restoran("Restaurant Name","Is Delayed")  # Excel dosyasından oku
                    
                    label = ctk.CTkLabel(cell, 
                                       text=f"Gecikme Oranı En Düşük Restoran\n{gecikme_orani_en_dusuk['restoran']}\n{gecikme_orani_en_dusuk['gecikme_orani']}%",
                                       text_color = yesil, 
                                       font=ctk.CTkFont(size=14, weight="bold"))
                    label.pack(expand=True)

                #4.Satır 2.Sütun
                #Saatlik Yoğunluk
                if i == 3 and j ==1:
                    veriler=saatlik_satis_grafigi()

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

                #4.Satır 3. Sütun (3,2) - Pizza Boyut Grafiği                   
                if i == 2 and j == 2: 
                    veri = pizza_boyut_grafigi("Pizza Size")

                    pizzalar = veri["Pizza Boyutlari"]
                    satislar = veri["satislar"]

                    # Matplotlib Figure
                    fig, ax = plt.subplots(figsize=(4, 1), dpi=100)
                    fig.patch.set_facecolor("#2b2b2b")  # Dark theme uyumu
                    ax.set_facecolor("#2b2b2b")
                    fig.subplots_adjust(top=0.80,bottom=0.20,left=0.10,right=0.95)
                    
                    ax.pie(satislar,labels=pizzalar,autopct="%1.1f%%",startangle=90,pctdistance=0.6,labeldistance=1.2,textprops={"color":"white","fontsize":8})
                    ax.set_title("Pizza Boyut Dağılımı",color="white")
                    # Grafiği CustomTkinter içine gömme
                    canvas = FigureCanvasTkAgg(fig, master=cell)
                    canvas.draw()
                    canvas.get_tk_widget().pack(fill="both", expand=True,padx=10,pady=15)
                    plt.close(fig)