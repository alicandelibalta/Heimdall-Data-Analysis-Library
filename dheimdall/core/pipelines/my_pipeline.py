import os
from ...utils.config_manager import ConfigManager
from ...utils.logger import logger  # 🎯 Log mekanizmamızı içeri alıyoruz
from .. import loaders, cleaners


class MyPipeline:
    def __init__(self, config_path: str):
        """
        Deli-Heimdall Pipeline Motoru.
        Kullanıcının kendi proje klasöründe belirttiği YAML dosyasını okur ve adımları yürütür.
        """
        if not os.path.exists(config_path):
            error_msg = (
                f"Belirtilen '{config_path}' konfigürasyon dosyası bulunamadı! "
                f"Lütfen terminali çalıştırdığın dizinde bu dosyanın var olduğundan emin ol knka."
            )
            logger.error(error_msg)
            raise FileNotFoundError(f"\n🚨 [Deli-Heimdall Hatası]: {error_msg}")

        # Kullanıcının dizinindeki YAML dosyasını okuyoruz
        self.config = ConfigManager.read_config(config_path)
        self.data = None

        logger.info(
            f"👁️ Deli-Heimdall Saf Motor: '{self.config.get('project_name', 'Adsız Proje')}' başlatıldı."
        )

    def run(self):
        """
        YAML içindeki tüm evreleri (stages) ve altındaki aksiyonları (actions) sırayla tetikler.
        """
        stages = self.config.get("stages", [])

        if not stages:
            logger.warning(
                "YAML dosyasında yürütülecek hiçbir 'stages' (evre) bulunamadı."
            )
            return

        # Evreleri sırayla dönüyoruz (Örn: Veri_Yukleme -> Veri_Temizleme)
        for stage in stages:
            stage_name = stage.get("name", "Bilinmeyen Evre")
            logger.info(f"🚀 [Evre Başladı]: {stage_name}")

            # O evrenin altındaki aksiyon listesini sırayla dönüyoruz
            actions = stage.get("actions", [])
            for action in actions:
                if not action:
                    continue

                # YAML'daki her bir satırı (fonskiyon_adi: parametreler) şeklinde söküyoruz
                func_name, kwargs = list(action.items())[0]
                kwargs = kwargs if kwargs is not None else {}

                # loaders altında var mı?
                if hasattr(loaders, func_name):
                    func = getattr(loaders, func_name)
                    logger.info(f"  └─ 📦 [Giriş/Çıkış] {func_name} çalıştırılıyor...")

                    if func_name.startswith("load"):
                        self.data = func(**kwargs)
                    elif func_name.startswith("save"):
                        func(df=self.data, **kwargs)

                # cleaners altında var mı?
                elif hasattr(cleaners, func_name):
                    func = getattr(cleaners, func_name)
                    logger.info(f"  └─ 🧹 [Temizlik] {func_name} çalıştırılıyor...")

                    self.data = func(df=self.data, **kwargs)

                else:
                    error_msg = (
                        f"Deli-Heimdall sisteminde '{func_name}' adında bir eklenti (plugin) bulunamadı. "
                        f"Lütfen loaders veya cleaners klasöründeki dosyalarını kontrol et."
                    )
                    logger.error(f"MİMARİ HATA: {error_msg}")
                    raise AttributeError(f"\n!!! MİMARİ HATA !!!\n{error_msg}")

        logger.info("✅ Deli-Heimdall: Tüm aşamalar başarıyla tamamlandı.")
