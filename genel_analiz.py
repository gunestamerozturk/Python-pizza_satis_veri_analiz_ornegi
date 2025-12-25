import pandas as pd
import os

# Excel dosya yolu
EXCEL_DOSYASI = "veriler.xlsx"

def excel_oku():
    """Excel dosyasını oku, DataFrame döndür"""
    try:
        if os.path.exists(EXCEL_DOSYASI):
            return pd.read_excel(EXCEL_DOSYASI)
        return pd.DataFrame()  # Boş DataFrame
    except Exception as e:
        print(f"Hata: {e}")
        return pd.DataFrame()

#Toplam Kayıt
def excel_kayit_sayisi():
    """Excel'deki toplam kayıt sayısını döndür"""
    df = excel_oku()  # Excel'i oku
    return len(df)    # Kayıt sayısını al

#Ortalama Teslimat Süresi
def ortalama_teslimat_suresi(teslimat_suresi = "Delivery Duration (min)"):
    df = excel_oku()
    ortalama_teslimat = df[teslimat_suresi].mean()
    return round(ortalama_teslimat,2)

#Gecikme Oranı (30 Dakika teslimat süresini aşanlar)
def gecikme_orani(gecikenler = "Is Delayed",deger=True):
    df = excel_oku()
    toplam = len(df)
    geciken_toplam = len(df[df[gecikenler]==deger])
    geciken_yuzde = (geciken_toplam/toplam) * 100
    return round(geciken_yuzde,2)

#En Çok Satış Yapan Restoran
def en_cok_satan_restoran(restoran="Restaurant Name"):
    df = excel_oku()
    en_cok_satan = df[restoran].mode()[0]
    return en_cok_satan

#En Çok Satış Yapan Şube
def en_cok_satan_sube(restoran="Restaurant Name",lokasyon = "Location"):
    df = excel_oku()
    yuksek_satis = df.groupby([restoran,lokasyon]).size().reset_index(name="satis_sayisi")
    max_satis = yuksek_satis['satis_sayisi'].max()
    en_yuksek_satis_sube = yuksek_satis[yuksek_satis['satis_sayisi']==max_satis].iloc[0]

    sonuc = en_yuksek_satis_sube.iloc[0]
    return {
        'Restaurant Name':en_yuksek_satis_sube["Restaurant Name"],
        'Location':en_yuksek_satis_sube["Location"],
        'satis_sayisi':int(en_yuksek_satis_sube['satis_sayisi'])
    }

#Aylık Satış Grafiği
def aylik_satis_grafigi(month = "Order Month"):
    df = excel_oku()
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

#Tercih Edilen Malzeme Sayısı (Ortalama)
def ortalama_malzeme_sayisi(malzeme_sayisi = "Toppings Count"):
    df = excel_oku()
    ortalama_malzeme_sayisi = df[malzeme_sayisi].mean()
    if ortalama_malzeme_sayisi < 1.5:
        ortalama_malzeme_sayisi=1
    elif ortalama_malzeme_sayisi >= 1.5 and ortalama_malzeme_sayisi <=2.5:
        ortalama_malzeme_sayisi = 2
    elif ortalama_malzeme_sayisi > 2.5 and ortalama_malzeme_sayisi <=3.5:
        ortalama_malzeme_sayisi = 3
    elif ortalama_malzeme_sayisi > 3.5 and ortalama_malzeme_sayisi <=4.5:
        ortalama_malzeme_sayisi = 4
    else:
        ortalama_malzeme_sayisi = 5
    return round(ortalama_malzeme_sayisi)

#Gecikme Oranı En Fazla Restoran
def gecikme_orani_en_yuksek_restoran(restoran="Restaurant Name",gecikme="Is Delayed"):
    df = excel_oku()

    gecikme_orani = (df.groupby(restoran)[gecikme].mean().mul(100).round(2))

    en_cok_geciken_restoran = gecikme_orani.idxmax()
    en_cok_geciken_oran = gecikme_orani.max()

    return{
        "restoran":en_cok_geciken_restoran,
        "gecikme_orani":float(en_cok_geciken_oran)
    }

#Gecikme Oranı En Az Restoran
def gecikme_orani_en_dusuk_restoran(restoran="Restaurant Name",gecikme="Is Delayed"):
    df = excel_oku()

    gecikme_orani = (df.groupby(restoran)[gecikme].mean().mul(100).round(2))

    en_az_geciken_restoran = gecikme_orani.idxmin()
    en_az_geciken_oran = gecikme_orani.min()

    return{
        "restoran":en_az_geciken_restoran,
        "gecikme_orani":float(en_az_geciken_oran)
    }

#Pizza Tipi Dağılımı
def pizza_tipi_grafigi(pizza_type="Pizza Type"):
    df = excel_oku()
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


#Gün İçinde En Yoğun Saatler
def saatlik_satis_grafigi(siparis_saati = "Order Hour"):
    df = excel_oku()
    yogunluk = df[siparis_saati].value_counts().rename_axis("Saat").reset_index(name="Siparis Sayisi").sort_values("Saat")
    return{
        "Saatler":yogunluk["Saat"].tolist(),
        "Siparisler": yogunluk["Siparis Sayisi"].tolist()
    }

#Pizza Boyutlarının Pasta Dağılım Grafiği
def pizza_boyut_grafigi(pizza_size="Pizza Size"):
    df = excel_oku()
    pizza_sizes = {
        "Small":1,
        "Medium":2,
        "Large":3,
        "XL":4
    }
    pizza_boyut=(df[pizza_size].value_counts().rename_axis("Pizza Boyutu").reset_index(name="Satis"))
    pizza_boyut["Sira"]=pizza_boyut["Pizza Boyutu"].map(pizza_sizes)
    pizza_boyut=pizza_boyut.sort_values("Sira")

    return{
        'Pizza Boyutlari':pizza_boyut["Pizza Boyutu"].tolist(),
        'satislar':pizza_boyut["Satis"].tolist(),
        'toplam':pizza_boyut.sum()
    }