from ..loaders import LoadCsv, SaveCsv
from ...utils.config_manager import ConfigManager


class MyPipeline:
    def __init__(self, config_path="config.yaml"):
        self.data = None
        # Yeni esnek YAML yapısını okuyoruz
        self.config = ConfigManager.read_config(config_path)
        print(
            f"--- Heimdall: '{self.config.get('project_name', 'Adsız Proje')}' başlatıldı."
        )

    def run(self):
        # YAML'daki adımları sırayla liste olarak alıyoruz
        steps = self.config.get("pipeline", [])

        for step_config in steps:
            # Boş adımları pas geç
            if not step_config:
                continue

            # İlk key fonksiyon adı, altındaki value'lar blok parametrelerdir.
            step_name, params = list(step_config.items())[0]

            # 1. KONTROL: Sınıfın içinde bu isimde bir nitelik var mı?
            method = getattr(self, step_name, None)

            # 2. KONTROL: Bulunan şey gerçekten çağrılabilir bir fonksiyon mu?
            if method is not None and callable(method):
                # Parametre bloğu boş bırakıldıysa (None ise) hata vermemesi için boş sözlük ({}) güvencesi
                kwargs = params if params is not None else {}

                print(f"--- [Esnek Akış] Tetiklenen Adım: {step_name}")
                # Metodu, içindeki dinamik parametrelerle patlatarak çalıştırıyoruz
                method(**kwargs)
            else:
                raise AttributeError(
                    f"!!! MİMARİ HATA !!!\n"
                    f"Heimdall kütüphanesinde '{step_name}' adında çağrılabilir bir metot bulunamadı.\n"
                    f"Lütfen pipeline adımlarını veya fonksiyon isimlerini kontrol edin."
                )

        print("--- Heimdall: Tüm süreç başarıyla tamamlandı.")

    def load(self, path, encoding="utf-8"):
        # Artık YAML'dan encoding gelse de gelmese de default olarak 'utf-8' korumalı
        self.data = LoadCsv.load(path, encoding=encoding)
        return self

    def save(self, path):
        if self.data is not None:
            SaveCsv.save(self.data, path)
        else:
            print("--- Uyarı: Hafızada kaydedilecek veri bulunamadı (self.data boş).")
        return self
