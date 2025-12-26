import pandas as pd
from main import *
from restoran_view import *

# Excel dosya yolu
EXCEL_DOSYASI = "veriler.xlsx"

#Excel dosyasını okur, df adında veri çerçevesine tabloyu tanımlar ve df değerini döndürür.
def excel_oku(restoran_ad):
    df = pd.read_excel(EXCEL_DOSYASI) #pandas kütüphanesi kullanılarak excel dosyası df değişkenine tanımlandı.
    df = df[df["Restaurant Name"]==restoran_ad] #excel dosyasından gelen veri, eşitlik kontrolü yapılarak filtrelendi.
    return df

#Veri çerçevesindeki toplam kayıt sayısını bulur.    
def rst_toplam_satis(restoran_ad):
    df = excel_oku(restoran_ad)
    toplam = df.shape[0] #shape[0] satır sayısını verir.
    return toplam

#Veri çerçevesindeki "Delivery Duration (min)" sütunundaki değerlerin ortalamasını alır. 
def rst_ortalama_teslimat_suresi(restoran_ad):
    df = excel_oku(restoran_ad)
    ortalama = df["Delivery Duration (min)"].mean() #mean() fonksiyonu sayısal değerlerin ortalamasını alır.
    return round(ortalama,2)

#Veri çerçevesinde "Is Delayed" sütunundaki True değerlerinin toplam değer sayısına oranını bulur.
def rst_gecikme_orani(restoran_ad):
    df = excel_oku(restoran_ad)
    toplam = len(df)
    geciken = len(df[df["Is Delayed"]==True])
    oran = (geciken / toplam) * 100
    return round(oran,2)

#Veri çerçevesindeki "Location" sütununda gruplama ve sayım yaparak en yüksek değeri bulur
def rst_en_cok_satan_sube(restoran_ad,lokasyon = "Location"):
    df = excel_oku(restoran_ad)
    yuksek_satis = df.groupby([lokasyon]).size().reset_index(name="satis_sayisi") #Lokasyon sütunundaki değerleri gruplar, size() ile veri sayısını alır, reset_index() ile sonucu veri çerçevesine dönüştürür.
    max_satis = yuksek_satis['satis_sayisi'].max() #max() en yüksek değeri bulur.
    en_yuksek_satis_sube = yuksek_satis[yuksek_satis['satis_sayisi']==max_satis].iloc[0] #En yüksek değere sahip "Location" değerini filtreler.
    return {
        'Location':en_yuksek_satis_sube["Location"],
        'satis_sayisi':int(en_yuksek_satis_sube['satis_sayisi'])
    }

#Veri çerçevesindeki "Location" sütununda gruplama ve sayım yaparak en düşük değeri bulur.
def rst_en_az_satan_sube(restoran_ad,lokasyon = "Location"):
    df = excel_oku(restoran_ad)
    yuksek_satis = df.groupby([lokasyon]).size().reset_index(name="satis_sayisi")
    min_satis = yuksek_satis['satis_sayisi'].min() #min() endüşük değeri bulur.
    en_dusuk_satis_sube = yuksek_satis[yuksek_satis['satis_sayisi']==min_satis].iloc[0]
    return {
        'Location':en_dusuk_satis_sube["Location"],
        'satis_sayisi':int(en_dusuk_satis_sube['satis_sayisi'])
    }

#Veri çerçevesindeki "Location" ve "Is Delayed" sütunlarında gruplama ve filtreleme işlemleri yaparak en düşük değeri bulur.
def rst_gecikme_orani_en_dusuk_sube(restoran_ad,gecikme="Is Delayed",lokasyon="Location"):
    df = excel_oku(restoran_ad)
    df["geciken"]=df["Is Delayed"] == True
    gecikme_orani = (df.groupby(lokasyon)[gecikme].mean().mul(100).round(2)) #mul() çarpma işlemi yapar.

    en_az_geciken_restoran = gecikme_orani.idxmin() #idxmin() minimum değerin konumunu bulur.
    en_az_geciken_oran = gecikme_orani.min()

    return{
        "restoran":en_az_geciken_restoran,
        "gecikme_orani":float(en_az_geciken_oran)
    }

#Veri çerçevesindeki "Location" ve "Is Delayed" sütunlarında gruplama ve filtreleme işlemleri yaparak en yüksek değeri bulur.
def rst_gecikme_orani_en_yuksek_sube(restoran_ad,gecikme="Is Delayed",lokasyon="Location"):
    df = excel_oku(restoran_ad)
    df["geciken"]=df["Is Delayed"] == True
    gecikme_orani = (df.groupby(lokasyon)[gecikme].mean().mul(100).round(2))

    en_cok_geciken_restoran = gecikme_orani.idxmax() #idxmax() maksimum değerin konumunu bulur.
    en_cok_geciken_oran = gecikme_orani.max()

    return{
        "restoran":en_cok_geciken_restoran,
        "gecikme_orani":float(en_cok_geciken_oran)
    }

#Veri çerçevesindeki "Payment Method" sütununda gruplama ve filtreleme işlemleri yaparak en yüksek değeri bulur.
def rst_odeme_yontemi(restoran_ad,odeme_yontemi = "Payment Method"):
    df = excel_oku(restoran_ad)
    odeme_yontemleri = df.groupby([odeme_yontemi]).size().reset_index(name="satis_sayisi")
    max_odeme_tercihi = odeme_yontemleri['satis_sayisi'].max()
    en_cok_tercih_edilen_odeme = odeme_yontemleri[odeme_yontemleri['satis_sayisi']==max_odeme_tercihi].iloc[0]
    return {
        "odeme_method":en_cok_tercih_edilen_odeme["Payment Method"],
        "satis_sayisi":en_cok_tercih_edilen_odeme["satis_sayisi"]
    }

#Veri çerçevesindeki "Payment Category" sütununda gruplama ve filtreleme işlemleri yaparak en yüksek değeri bulur.
def rst_siparis_yontemi(restoran_ad,siparis_yontemi = "Payment Category"):
    df = excel_oku(restoran_ad)
    toplam = len(df)
    online = len(df[df[siparis_yontemi]=="Online"])
    online_oran = (online / toplam) * 100
    if online_oran > 50:   #Koşul blokları kullanılarak farklı sonuçlar döndürülmesi sağlandı.
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

#Veri çerçevesindeki "Order Hour" sütununda gruplama ve filtreleme işlemleri yapar ve değerleri listeler   
def rst_saatlik_satis_grafigi(restoran_ad,siparis_saati = "Order Hour"):
    df = excel_oku(restoran_ad)
    yogunluk = df[siparis_saati].value_counts().rename_axis("Saat").reset_index(name="Siparis Sayisi").sort_values("Saat")
    #value_counts() verinin tekrar sayısını bulur. rename_axis() eksen ismini değiştirir. sort_values() değerlere göre sıralama yapar.
    return{
        "Saatler":yogunluk["Saat"].tolist(),
        "Siparisler": yogunluk["Siparis Sayisi"].tolist()
    }

#Veri çerçevesindeki "Order Month" sütununda gruplama, sıralama ve filtreleme işlemleri yapar ve değerleri listeler 
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
    aylik_satis["Sira"]=aylik_satis["Ay"].map(ay_sirasi) #map() sıralama işlemi yapar.
    aylik_satis = aylik_satis.sort_values("Sira")

    return {
        'aylar': aylik_satis["Ay"].tolist(),
        'satislar':aylik_satis["Satis"].tolist(),
        'toplam':aylik_satis.sum() #sum() toplama işlemi yapar.
    }

#Veri çerçevesindeki "Pizza Type" sütununda gruplama, sıralama ve filtreleme işlemleri yapar ve değerleri listeler
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
