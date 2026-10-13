
import unittest

from src.carregar_dados import carregar_dados
from src.validar_dados import validar_dados
from src.analisar_custos import (
    analisar_custos,
    calcular_custo_total,
    calcular_economia_potencial,
)
from src.regras_finops import aplicar_regras_finops


class TestFinOps(unittest.TestCase):

    def setUp(self):
        dados = carregar_dados()
        validar_dados(dados)

        custos = analisar_custos(dados)
        classificados = aplicar_regras_finops(custos)

        self.resultado = calcular_economia_potencial(classificados)

    def test_carregar_cinco_instancias(self):
        self.assertEqual(len(self.resultado), 5)

    def test_custo_total_mensal(self):
        custo_total = calcular_custo_total(self.resultado)

        self.assertAlmostEqual(custo_total, 2937.60, places=2)

    def test_economia_potencial(self):
        economia_total = self.resultado["economia_potencial_usd"].sum()

        self.assertAlmostEqual(economia_total, 1252.80, places=2)

    def test_instancia_de_producao_deve_ser_mantida(self):
        instancia = self.resultado[
            self.resultado["instancia_id"] == "i-004"
        ].iloc[0]

        self.assertEqual(
            instancia["acao_finops"],
            "MANTER: Utilizacao elevada",
        )


if __name__ == "__main__":
    unittest.main()

