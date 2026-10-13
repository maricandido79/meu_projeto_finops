
import numpy as np
import pandas as pd


def aplicar_regras_finops(dados: pd.DataFrame) -> pd.DataFrame:
    resultado = dados.copy()

    condicoes = [
        (
            (resultado["ultimo_acesso_dias"] >= 30)
            & (resultado["media_uso_cpu_pct"] < 2.0)
        ),
        (
            resultado["departamento"].isin(
                ["Desenvolvimento", "Homologacao", "Marketing"]
            )
            & (resultado["horas_ativas_fds"] > 0)
        ),
        (resultado["media_uso_cpu_pct"] > 70.0),
    ]

    acoes = [
        "REVISAR: Possivel recurso inativo",
        "AVALIAR: Possivel agendamento fora do horario",
        "MANTER: Utilizacao elevada",
    ]

    resultado["acao_finops"] = np.select(
        condicoes,
        acoes,
        default="REVISAR: Analisar utilizacao e custo",
    )

    return resultado
