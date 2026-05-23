import logging
import os


def get_logger(name: str = "heimdall") -> logging.Logger:
    """
    Heimdall kütüphanesi için hem konsola (Stream) hem de dosyaya (File)
    log yazan esnek ve merkezi logger mekanizması.
    """
    logger = logging.getLogger(name)

    # Eğer logger daha önce doldurulmadıysa (çift handler eklenmesini önlemek için)
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Logların nasıl görüneceğini belirleyen standart şablonumuz
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # 1. HANDLER: Konsola Anlık Çıktı Basma (StreamHandler)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # 2. HANDLER: Dosyaya Kalıcı Kaydetme (FileHandler)
        # Log dosyasını projenin o an çalıştığı dizinde 'heimdall.log' adıyla açar
        log_filename = "heimdall.log"
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Kütüphane standardı: Harici importlarda hata patlamasını önleyen boş handler
        logger.addHandler(logging.NullHandler())

    return logger


# Kütüphane içinden doğrudan çağrılacak hazır logger nesnesi
logger = get_logger()
