import pandas as pd
from dheimdall.utils.logger import logger


def Delete_Empty_Rows(df: pd.DataFrame, column: str) -> pd.DataFrame:

    if df is None or df.empty:
        logger.warning("Temizleme işlemi için verilen DataFrame boş!")
        return df

    if column not in df.columns:
        logger.error(f"Temizleme hatası: '{column}' kolonu veri setinde bulunamadı!")
        return df

    initial_rows = len(df)
    cleaned_df = df.copy()

    # bozuk boş data kontrolü
    if cleaned_df[column].dtype == "object":
        cleaned_df[column] = (
            cleaned_df[column]
            .astype(str)
            .str.strip()
            .replace(["", "None", "nan", "NaN"], pd.NA)
        )

    cleaned_df = cleaned_df.dropna(subset=[column])
    removed_rows = initial_rows - len(cleaned_df)

    if removed_rows > 0:
        logger.info(
            f"🧹 '{column}' kolonundaki boşluklar temizlendi: {removed_rows} satır uçuruldu."
        )
    else:
        logger.info(f"✨ '{column}' kolonunda hiç boş satıra rastlanmadı.")

    return cleaned_df
