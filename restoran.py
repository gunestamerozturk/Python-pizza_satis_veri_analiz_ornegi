import pandas as pd
from main import *
from restoran_view import *

# Excel dosya yolu
EXCEL_DOSYASI = "veriler.xlsx"

def excel_oku(restoran_ad):
    df = pd.read_excel(EXCEL_DOSYASI)
    df = df[df["Restaurant Name"]==restoran_ad]
    return df
    
def rst_toplam_satis(restoran_ad):
    df = excel_oku(restoran_ad)
    toplam = df.shape[0]
    return toplam

def rst_ortalama_teslimat_suresi(restoran_ad):
    df = excel_oku(restoran_ad)
    ortalama = df["Delivery Duration (min)"].mean()
    return round(ortalama,2)

def rst_gecikme_orani(restoran_ad):
    df = excel_oku(restoran_ad)
    toplam = len(df)
    geciken = len(df[df["Is Delayed"]==True])
    oran = (geciken / toplam) * 100
    return round(oran,2)

def rst_en_cok_satan_sube(restoran_ad,lokasyon = "Location"):
    df = excel_oku(restoran_ad)
    yuksek_satis = df.groupby([lokasyon]).size().reset_index(name="satis_sayisi")
    max_satis = yuksek_satis['satis_sayisi'].max()
    en_yuksek_satis_sube = yuksek_satis[yuksek_satis['satis_sayisi']==max_satis].iloc[0]
    return {
        'Location':en_yuksek_satis_sube["Location"],
        'satis_sayisi':int(en_yuksek_satis_sube['satis_sayisi'])
    }

def rst_en_az_satan_sube(restoran_ad,lokasyon = "Location"):
    df = excel_oku(restoran_ad)
    yuksek_satis = df.groupby([lokasyon]).size().reset_index(name="satis_sayisi")
    min_satis = yuksek_satis['satis_sayisi'].min()
    en_dusuk_satis_sube = yuksek_satis[yuksek_satis['satis_sayisi']==min_satis].iloc[0]
    return {
        'Location':en_dusuk_satis_sube["Location"],
        'satis_sayisi':int(en_dusuk_satis_sube['satis_sayisi'])
    }

def rst_gecikme_orani_en_dusuk_sube(restoran_ad,gecikme="Is Delayed",lokasyon="Location"):
    df = excel_oku(restoran_ad)
    df["geciken"]=df["Is Delayed"] == True
    gecikme_orani = (df.groupby(lokasyon)[gecikme].mean().mul(100).round(2))

    en_az_geciken_restoran = gecikme_orani.idxmin()
    en_az_geciken_oran = gecikme_orani.min()

    return{
        "restoran":en_az_geciken_restoran,
        "gecikme_orani":float(en_az_geciken_oran)
    }

def rst_gecikme_orani_en_yuksek_sube(restoran_ad,gecikme="Is Delayed",lokasyon="Location"):
    df = excel_oku(restoran_ad)
    df["geciken"]=df["Is Delayed"] == True
    gecikme_orani = (df.groupby(lokasyon)[gecikme].mean().mul(100).round(2))

    en_cok_geciken_restoran = gecikme_orani.idxmax()
    en_cok_geciken_oran = gecikme_orani.max()

    return{
        "restoran":en_cok_geciken_restoran,
        "gecikme_orani":float(en_cok_geciken_oran)
    }

def rst_odeme_yontemi(restoran_ad,odeme_yontemi = "Payment Method"):
    df = excel_oku(restoran_ad)
    odeme_yontemleri = df.groupby([odeme_yontemi]).size().reset_index(name="satis_sayisi")
    max_odeme_tercihi = odeme_yontemleri['satis_sayisi'].max()
    en_cok_tercih_edilen_odeme = odeme_yontemleri[odeme_yontemleri['satis_sayisi']==max_odeme_tercihi].iloc[0]
    return {
        "odeme_method":en_cok_tercih_edilen_odeme["Payment Method"],
        "satis_sayisi":en_cok_tercih_edilen_odeme["satis_sayisi"]
    }

def rst_siparis_yontemi(restoran_ad,siparis_yontemi = "Payment Category"):
    df = excel_oku(restoran_ad)
    toplam = len(df)
    online = len(df[df[siparis_yontemi]=="Online"])
    online_oran = (online / toplam) * 100
    if online_oran > 50:
        return {
            'Oran':round(online_oran,2),
            'Method':"Online"
        }
    elif online_oran < 50:
        return {
            'Oran':round((100-online_oran),2),
            'Method':"Offline"
        }
    else:
        return{
            'Oran':round((100-online_oran),2),
            'Method':"Online/Offline"
        }
    
def rst_saatlik_satis_grafigi(restoran_ad,siparis_saati = "Order Hour"):
    df = excel_oku(restoran_ad)
    yogunluk = df[siparis_saati].value_counts().rename_axis("Saat").reset_index(name="Siparis Sayisi").sort_values("Saat")
    return{
        "Saatler":yogunluk["Saat"].tolist(),
        "Siparisler": yogunluk["Siparis Sayisi"].tolist()
    }

#Aylık Satış Grafiği
def rst_aylik_satis_grafigi(restoran_ad,month = "Order Month"):
    df = excel_oku(restoran_ad)
    ay_sirasi = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    aylik_satis = (df[month].value_counts().rename_axis("Ay").reset_index(name="Satis"))
    aylik_satis["Sira"]=aylik_satis["Ay"].map(ay_sirasi)
    aylik_satis = aylik_satis.sort_values("Sira")

    return {
        'aylar': aylik_satis["Ay"].tolist(),
        'satislar':aylik_satis["Satis"].tolist(),
        'toplam':aylik_satis.sum()
    }

#Pizza Tipi Dağılımı
def rst_pizza_tipi_grafigi(restoran_ad,pizza_type="Pizza Type"):
    df = excel_oku(restoran_ad)
    pizza_tipleri = {
        "BBQ Chicken":1,
        "Cheese Burst":2,
        "Deep Dish":3,
        "Gluten-Free":4,
        "Margarita":5,
        "Non-Veg":6,
        "Sicilian":7,
        "Stuffed Crust":8,
        "Thai Chicken":9,
        "Thin Crust":10,
        "Veg":11,
        "Vegan":12,
    }
    pizza_tipi=(df[pizza_type].value_counts().rename_axis("Pizza Tipi").reset_index(name="Satis"))
    pizza_tipi["Sira"]=pizza_tipi["Pizza Tipi"].map(pizza_tipleri)
    pizza_tipi = pizza_tipi.sort_values("Sira")

    return{
        'Pizza Tipleri':pizza_tipi["Pizza Tipi"].tolist(),
        'satislar':pizza_tipi["Satis"].tolist(),
        'toplam':pizza_tipi.sum()
    }