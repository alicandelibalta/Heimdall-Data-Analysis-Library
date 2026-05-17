import pandas as pd
import os
from datetime import datetime


class SaveCsv:
    @staticmethod
    def save(df, output_path):
        # 1. Dosya ismini ve uzantısını ayırıyoruz
        file_base, file_ext = os.path.splitext(output_path)

        # Uzantı yoksa veya .csv değilse zorla .csv yapıyoruz
        if not file_ext or file_ext.lower() != ".csv":
            file_ext = ".csv"

        # 2. Zaman damgası oluştur (YılAyGün_SaatDakika)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        # 3. Dinamik dosya ismi
        final_path = f"{file_base}_{timestamp}{file_ext}"

        # 4. Klasör yoksa otomatik oluştur
        directory = os.path.dirname(final_path)
        if directory and not os.path.exists(directory):
            print(f"--- Klasör oluşturuluyor: {directory}")
            os.makedirs(directory)

        # 5. Aynı isimde mükerrer dosya kontrolü
        counter = 1
        while os.path.exists(final_path):
            final_path = f"{file_base}_{timestamp}_{counter}{file_ext}"
            counter += 1

        # 6. Gerçek Pandas Kaydetme İşlemi
        try:
            print(f"--- Veri şu yola kaydediliyor: {final_path}")
            df.to_csv(final_path, index=False, encoding="utf-8-sig")
            return True
        except Exception as e:
            print(f"--- Kaydetme hatası: {e}")
            return False
