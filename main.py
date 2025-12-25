import customtkinter as ctk
from genel_analiz_view import *
from restoran_view import *

BG_MAIN = "#1f1f1f"
BG_CARD = "#2b2b2b"
BG_PLOT = "#2b2b2b"
FG_TEXT = "#ffffff"

# Tema ayarları
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Uygulama(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Pencere ayarları
        self.title("Pizza Satış Raporları")
        self.geometry("1600x900")
        self.configure(fg_color=BG_MAIN)
        
        # 6 Sekme oluştur
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True)
        
        # Sekmeleri ekle
        for i in range(1, 7):
            #self.tabview.add(f"Sekme {i}")
            match i:
                case 1:
                    self.tabview.add("Tümü")
                    sekme1_icerik(self)
                case 2:
                    self.tabview.add("Domino's")
                    restoran_icerik(self,restoran_ad="Domino's")
                case 3:
                    self.tabview.add("Little Caesars")
                    restoran_icerik(self,restoran_ad="Little Caesars")
                case 4:
                    self.tabview.add("Marco's Pizza")
                    restoran_icerik(self,restoran_ad="Marco's Pizza")
                case 5:
                    self.tabview.add("Papa John's")
                    restoran_icerik(self,restoran_ad="Papa John's")
                case 6:
                    self.tabview.add("Pizza Hut")
                    restoran_icerik(self,restoran_ad="Pizza Hut")
        
        # 1. sekmeyi doldur
        
        
           
         
             
                  

    

    
if __name__ == "__main__":
    app = Uygulama()
    app.mainloop()