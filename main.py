from src.carregar_dados import carregar_dados
from src.validar_dados import validar_dados
from src.analisar_custos import (
    analisar_custos,
    calcular_custo_total,
    calcular_economia_potencial,
)
from src.regras_finops import aplicar_regras_finops
from src.gerar_relatorio import gerar_relatorio


def main():
    # 1. Carregar e validar os dados
    dados = carregar_dados()
    validar_dados(dados)

    # 2. Analisar custos e classificar recursos
    custos = analisar_custos(dados)
    classificados = aplicar_regras_finops(custos)

    # 3. Calcular a economia potencial
    resultado = calcular_economia_potencial(classificados)

    # 4. Calcular os indicadores
    custo_total = calcular_custo_total(resultado)
    economia_total = resultado["economia_potencial_usd"].sum()

    # 5. Mostrar os resultados no terminal
    print("\n=== RELATORIO FINOPS ===")
    print(
        resultado[
            [
                "instancia_id",
                "departamento",
                "custo_mensal_atual_usd",
                "acao_finops",
                "economia_potencial_usd",
            ]
        ].to_string(index=False)
    )

    print("\nCusto mensal total estimado: USD", round(custo_total, 2))
    print("Economia potencial estimada: USD", round(economia_total, 2))

    # 6. Gerar o arquivo PDF
    caminho_pdf = gerar_relatorio(
        resultado,
        custo_total,
        economia_total,
    )

    print("\nRelatorio PDF salvo em:", caminho_pdf)


if __name__ == "__main__":
    main()
