
import pandas as pd


HORAS_MES_ESTIMADAS = 720
REDUCAO_AGENDAMENTO_ESTIMADA = 0.65


def analisar_custos(dados: pd.DataFrame) -> pd.DataFrame:
    resultado = dados.copy()

    resultado["custo_mensal_atual_usd"] = (
        resultado["custo_hora_usd"] * HORAS_MES_ESTIMADAS
    )

    return resultado


def calcular_custo_total(dados: pd.DataFrame) -> float:
    return float(dados["custo_mensal_atual_usd"].sum())


def calcular_economia_potencial(dados: pd.DataFrame) -> pd.DataFrame:
    resultado = dados.copy()

    recurso_inativo = (
        resultado["acao_finops"] == "REVISAR: Possivel recurso inativo"
    )

    avaliar_agendamento = (
        resultado["acao_finops"]
        == "AVALIAR: Possivel agendamento fora do horario"
    )

    resultado["economia_potencial_usd"] = 0.0

    resultado.loc[recurso_inativo, "economia_potencial_usd"] = (
        resultado.loc[recurso_inativo, "custo_mensal_atual_usd"]
    )

    resultado.loc[avaliar_agendamento, "economia_potencial_usd"] = (
        resultado.loc[avaliar_agendamento, "custo_mensal_atual_usd"]
        * REDUCAO_AGENDAMENTO_ESTIMADA
    )

    return resultado
