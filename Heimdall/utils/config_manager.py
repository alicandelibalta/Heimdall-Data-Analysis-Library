import yaml
import os


class ConfigManager:
    @staticmethod
    def read_config(path="config.yaml"):
        # Dosya yolunu kontrol edelim (OS burada devreye giriyor)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Ayar dosyası bulunamadı: {path}")

        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
