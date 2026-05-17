# main.py içeriği
from Heimdall.core.pipelines.my_pipeline import MyPipeline


def main():
    # 1. Pipeline objesini oluşturuyoruz.
    # Bu sırada __init__ çalışır ve config.yaml dosyasını okur.
    orchestrator = MyPipeline(config_path="config.yaml")
    orchestrator.run()


if __name__ == "__main__":
    main()
