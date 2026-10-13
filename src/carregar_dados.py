
from pathlib import Path

import pandas as pd


def carregar_dados() -> pd.DataFrame:
    caminho_arquivo = Path(__file__).resolve().parent.parent / "data" / "custos_exemplo.csv"

    dados = pd.read_csv(caminho_arquivo)

    return dados
