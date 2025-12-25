# 🌟 **Restoran Sipariş ve Teslimat Analiz Uygulaması**  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-success?logo=pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=plotly" />
  <img src="https://img.shields.io/badge/CustomTkinter-Modern%20UI-6a5acd" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
</p>

<p align="center">
  Restoran zincirlerine ait sipariş verilerini analiz eden, grafiklerle desteklenmiş modern bir Python uygulaması.
</p>

---

## 🧩 **Proje Hakkında**

Bu proje, birden fazla restoran zincirine ait sipariş verilerini inceleyerek yöneticilere operasyonel içgörüler sunmak için geliştirilmiş Python tabanlı bir analiz uygulamasıdır.  
Arayüz CustomTkinter ile modern bir dashboard tasarımına sahiptir ve Excel üzerinden veri okuyarak çok boyutlu analizler üretir.

---

## ✨ **Özellikler**

### 📊 Genel Analizler
- Toplam sipariş sayısı  
- Ortalama teslimat süresi  
- Gecikme oranı  
- En çok satan restoran  
- En çok satış yapan şube  
- Pizza tipi ve boyutu dağılımları  
- Ortalama malzeme sayısı  

### 🍕 Restoran Bazlı Analizler
- Restoran özelinde KPI göstergeleri  
- Saatlik sipariş yoğunluğu grafiği  
- Aylık satış trendi  
- Ödeme yöntemi tercihleri  
- Online / offline sipariş oranı  
- En çok ve en az satan şubeler  
- Gecikme oranı yüksek/düşük şubeler  

---

## 📂 **Proje Yapısı**

```
📦 Pizza Analiz Uygulaması
├── main.py                # Ana uygulama ve sekme yönetimi
├── genel_analiz.py        # Genel analiz fonksiyonları
├── genel_analiz_view.py   # Genel analiz arayüzü
├── restoran.py            # Restoran analiz fonksiyonları
├── restoran_view.py       # Restoran analiz arayüzü
├── veriler.xlsx           # Veri kaynağı (Excel)
└── README.md              # Dokümantasyon
```

---

## 🛠️ **Kullanılan Teknolojiler**

| Teknoloji | Amaç |
|----------|------|
| **Python** | Ana geliştirme dili |
| **Pandas** | Veri temizleme ve analiz |
| **Matplotlib** | Grafik çizimi |
| **CustomTkinter** | Modern karanlık tema arayüz |
| **Excel (xlsx)** | Veri kaynağı |

---

## 🚀 **Kurulum ve Çalıştırma**

### 1️⃣ Bağımlılıkları yükle  
```bash
pip install pandas matplotlib customtkinter openpyxl
```

### 2️⃣ Excel dosyasını ekle  
Projeye şu dosyayı koy:
```
veriler.xlsx
```

### 3️⃣ Uygulamayı başlat  
```bash
python main.py
```

---

## 📌 **Koddan Örnekler**

### Ortalama teslimat süresi:
```python
ortalama_teslimat_suresi()
```

### Restoran bazlı aylık satış analizi:
```python
rst_aylik_satis_grafigi("Domino's")
```

---

## 🤝 **Geliştirme Tavsiyelerim**

Veri ekleme, silme ve güncelleme fonksiyonları ile birlikte proje daha işlevsel hale getirilebilir.
Veriler kart, çerçeve gibi tasarım araçlarıyla desteklenir ve grafiklerdeki küçük taşmalar önlenirse verilerin anlaşılabilirliği artacaktır.

---

## 👤 **Geliştirici**

**Güneş Tamer Öztürk**

---

### 📄 Veri Kaynağı  
Bu projede kullanılan örnek veri seti, eğitim ve analiz amaçlı olarak Kaggle üzerinden alınmıştır.
Veri seti sahibi: **Akshay Gaikwad**  
Kaynak: https://www.kaggle.com/datasets/akshaygaikwad448/pizza-delivery-data-with-enhanced-features
