import pandas as pd
import os


class LoadCsv:
    @staticmethod
    def _bad_line_handler(line):
        # Pandas hatalı bir satır bulduğunda bu fonksiyonu tetikler.
        # 'line' değişkeni bize hatalı satırın içeriğini bir liste olarak verir.

        log_message = f"[KIRLI VERI] Hatali satir yakalandi -> {line}\n"
        print(f"--- Uyarı: Hatalı satır tespit edildi, log dosyasına yazılıyor...")

        # Proje kök dizinine hata raporu yazıyoruz
        with open("heimdall_bad_lines.txt", "a", encoding="utf-8-sig") as f:
            f.write(log_message)

        return None  # None döndürerek bu satırı ana DataFrame'e ALMAMAISINI söylüyoruz.

    @staticmethod
    def load(file_path, encoding="utf-8"):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(
                f"Hata: '{file_path}' geçerli bir dosya yolu değil!"
            )

        # Her çalıştırmada eski hata günlüğünü temizleyelim ki kafamız karışmasın
        if os.path.exists("heimdall_bad_lines.txt"):
            os.remove("heimdall_bad_lines.txt")

        print(f"--- {file_path} yükleniyor...")

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
        except UnicodeDecodeError:
            print(f"--- Uyarı: {encoding} ile okunamadı, 'latin-1' deneniyor...")
            return pd.read_csv(
                file_path,
                encoding="latin-1",
                sep=None,
                engine="python",
                on_bad_lines=LoadCsv._bad_line_handler,
            )
