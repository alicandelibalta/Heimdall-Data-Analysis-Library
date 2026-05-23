import logging
import os


def get_logger(name: str = "heimdall") -> logging.Logger:
    """
    Heimdall kütüphanesi için projenin kök dizininde otomatik olarak bir 'logs'
    klasörü açan ve içine logları kaydeden merkezi logger mekanizması.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # 1. HANDLER: Konsol çıktısı
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # --- KLASÖR KORUMA MEKANİZMASI ---
        # Kodun o an çalıştığı dizinde (Cwd) 'logs' adında bir klasör yolu belirliyoruz
        log_dir = os.path.join(os.getcwd(), "logs")

        # Eğer bu klasör bilgisayarda yoksa, Python otomatik olarak oluştursun!
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Log dosyamızı artık bu güvenli klasörün içine yönlendiriyoruz
        log_filepath = os.path.join(log_dir, "heimdall.log")

        # 2. HANDLER: Dosya çıktısı
        file_handler = logging.FileHandler(log_filepath, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.addHandler(logging.NullHandler())

    return logger


logger = get_logger()
