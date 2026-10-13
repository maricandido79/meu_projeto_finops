
import pandas as pd


COLUNAS_OBRIGATORIAS = [
    "instancia_id",
    "departamento",
    "custo_hora_usd",
    "media_uso_cpu_pct",
    "horas_ativas_fds",
    "ultimo_acesso_dias",
]


def validar_dados(dados: pd.DataFrame) -> None:
    colunas_ausentes = [
        coluna
        for coluna in COLUNAS_OBRIGATORIAS
        if coluna not in dados.columns
    ]

    if colunas_ausentes:
        raise ValueError(
            f"Colunas obrigatórias ausentes: {colunas_ausentes}"
        )

    if dados.empty:
        raise ValueError("O arquivo não possui dados.")

    if dados[COLUNAS_OBRIGATORIAS].isnull().any().any():
        raise ValueError("Existem campos vazios nos dados.")

    if (dados["custo_hora_usd"] < 0).any():
        raise ValueError("O custo por hora não pode ser negativo.")

    if not dados["media_uso_cpu_pct"].between(0, 100).all():
        raise ValueError("A utilização de CPU deve estar entre 0 e 100.")

    if (dados["horas_ativas_fds"] < 0).any():
        raise ValueError("As horas de atividade não podem ser negativas.")

    if (dados["ultimo_acesso_dias"] < 0).any():
        raise ValueError("Os dias desde o último acesso não podem ser negativos.")


