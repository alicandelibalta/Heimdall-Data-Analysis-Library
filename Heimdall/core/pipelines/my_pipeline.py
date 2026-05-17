from ..loaders import LoadCsv, SaveCsv
from ...utils.config_manager import ConfigManager


class MyPipeline:
    def __init__(self, config_path="config.yaml"):
        self.data = None
        # YAML'ı oku
        self.config = ConfigManager.read_config(config_path)
        print(
            f"--- Heimdall: '{self.config.get('project_name', 'Adsız Proje')}' başlatıldı."
        )

    def run(self):
        # YAML'daki adımları sırayla çalıştır
        steps = self.config.get("pipeline", [])

        for step_config in steps:
            step_name = step_config.get("step")

            if step_name == "load":
                self.load(step_config.get("path"))

            elif step_name == "save":
                self.save(step_config.get("path"))

        print("--- Heimdall: Tüm süreç başarıyla tamamlandı.")

    def load(self, path):
        self.data = LoadCsv.load(path)
        return self

    def save(self, path):
        if self.data is not None:
            SaveCsv.save(self.data, path)
        return self
