# 👁️ Heimdall Data Analysis Library

Heimdall, modern veri mühendisliği ve veri analizi süreçlerini dinamik, esnek ve kurşun geçirmez bir boru hattı (pipeline) mimarisiyle yönetmek için tasarlanmış açık kaynaklı bir Python kütüphanesidir.

Adını her şeyi gören İskandinav tanrısından alan Heimdall, verilerinizin yapısal sorunlarını, format hatalarını ve kirliliklerini daha ilk adımda yakalar ve arındırır.

---

## 🚀 Öne Çıkan Özellikler

- **Sıfır Kelime Bağımlılıklı Esnek Pipeline:** `step` gibi katı anahtar kelimelere bağlı kalmadan, doğrudan YAML/JSON üzerinden fonksiyon isimleriyle dinamik süreç yönetimi.
- **Akıllı CSV/Excel Ayrımı (Zırhlı Yükleyici):** Uzantısı `.csv` yapılmış ama içi aslında Excel olan manipüle edilmiş dosyaları dosya imzasından (`PK\x03\x04`) tanır, format hatasını yüzünüze vurur.
- **Kirli Veri İzolasyonu:** CSV okuma esnasında patlayan hatalı/bozuk satırları ana akışı bozmadan ayıklar ve `heimdall_bad_lines.txt` raporuna fırlatır.
- **Frontend Entegrasyonuna Hazır:** Tamamen veri yapısı güdümlü (Data-Driven) mimarisi sayesinde gelecekteki bir Web/Masaüstü arayüzüne (React, Vue vb.) doğrudan bağlanabilir.

---

## 🛠️ Kurulum & Çalıştırma

Projeyi yerelde çalıştırmak için terminalden bağımlılıkları yükleyin:

```bash
pip install pandas openpyxl

Pipeline'ı tetiklemek için projenin kök dizininde PYTHONPATH ayarını yaparak main.py dosyasını ateşleyin:

Windows (CMD):

DOS
set PYTHONPATH=. && python main.py
```

Örnek Senaryo Tasarımı (config.yaml)
Heimdall, karmaşık döngüler veya if-elif hamallıkları gerektirmez. Yapacağınız işlemleri sırasıyla YAML dosyasına dizmeniz yeterlidir:

YAML
project_name: "Heimdall Enerji Verisi Analizi"
pipeline:

- load:
  path: "deneme.csv"
  encoding: "utf-8"
- save:
  path: "output/sonuc.csv"

🤝 Katkıda Bulunun
Heimdall geliştirilmeye açık modüler bir yapıya sahiptir. Yeni bir veri işleme adımı eklemek için MyPipeline sınıfına çağrılabilir (callable) yeni bir metot eklemeniz yeterlidir; dinamik akış motorumuz onu otomatik olarak tanıyacaktır!

Eklemek istediğiniz özellikler için lütfen bir Issue açın veya Pull Request gönderin.
