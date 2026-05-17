import pandas as pd
import os


class LoadCsv:
    @staticmethod
    def _bad_line_handler(line):
        # CSV içindeki gerçek hatalı satırları buraya yazmaya devam ediyoruz
        log_message = f"[KIRLI VERI] Hatali satir yakalandi -> {line}\n"
        with open("heimdall_bad_lines.txt", "a", encoding="utf-8") as f:
            f.write(log_message)
        return None

    @staticmethod
    def load(file_path, encoding="utf-8"):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(
                f"Hata: '{file_path}' geçerli bir dosya yolu değil!"
            )

        if os.path.exists("heimdall_bad_lines.txt"):
            os.remove("heimdall_bad_lines.txt")

        # 1. Ön Kontrol: Uzantı bariyere takılıyor mu?
        if file_path.endswith((".xlsx", ".xls")):
            raise ValueError(
                f"Hata: '{file_path}' bir Excel dosyasıdır! "
                f"LoadCsv sınıfı sadece CSV dosyalarını işleyebilir."
            )

        print(f"--- {file_path} CSV olarak yükleniyor...")

        try:
            return pd.read_csv(
                file_path,
                encoding=encoding,
                sep=None,
                engine="python",
                on_bad_lines=LoadCsv._bad_line_handler,
                quotechar='"',
                escapechar="\\",
            )
        except Exception as e:
            # 2. Arka Kapı Kontrolü: Uzantısı .csv yapılmış ama içi aslında Excel olan uyanık dosya kontrolü
            error_str = str(e)
            if "tokenizing data" in error_str or "line" in error_str:
                # Excel dosyalarının ilk 2 baytı her zaman 'PK' (Zip formatı) karakterleridir.
                # Emin olmak için dosyanın ilk birkaç karakterine göz atalım:
                try:
                    with open(file_path, "rb") as f:
                        start_bytes = f.read(4)

                    if b"PK\x03\x04" in start_bytes:
                        raise TypeError(
                            f"!!! KRITIK UYARI !!!\n"
                            f"'{file_path}' dosyasının uzantısı .csv görünüyor ama İÇERİĞİ BİR EXCEL DOSYASI!\n"
                            f"Lütfen dosyayı kontrol edin ve gerçek bir CSV olarak dışa aktarın."
                        )
                except Exception:
                    pass  # Dosya okunamazsa normal hata akışına bırak

            # Eğer Excel değil de başka bir yapısal hataysa normal hatayı fırlat
            raise Exception(f"CSV okunurken beklenmedik hata: {e}")
