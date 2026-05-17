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
            # gerçekten csv mi değil mi kontrol
            error_str = str(e)
            if "tokenizing data" in error_str or "line" in error_str:
                # Excel dosyalarının ilk 2 baytı her zaman 'PK'dır bunu kontrol edelim.
                # Bu sıkça karşılaşabileceğimiz sadece excel olup olmadığına dair kontrol.
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
                    pass

            # Eğer Excel değil de başka bir yapısal hataysa normal hatayı fırlat
            raise TypeError(
                f"!!! FORMAT HATASI !!!\n"
                f"'{file_path}' okunamadı. Bu yüklediğin şey geçerli bir CSV dosyası değil.\n"
                f"Detaylı Hata: {error_str}"
            )
