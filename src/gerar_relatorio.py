from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


def gerar_relatorio(dados, custo_total, economia_total):
    pasta_projeto = Path(__file__).resolve().parent.parent
    pasta_relatorios = pasta_projeto / "relatorios"
    pasta_relatorios.mkdir(exist_ok=True)

    caminho_pdf = pasta_relatorios / "relatorio-finops.pdf"

    documento = SimpleDocTemplate(
        str(caminho_pdf),
        pagesize=landscape(A4),
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )

    estilos = getSampleStyleSheet()

    titulo = ParagraphStyle(
        "TituloFinOps",
        parent=estilos["Title"],
        alignment=TA_CENTER,
        textColor=colors.HexColor("#243B53"),
        spaceAfter=18,
    )

    conteudo = []

    conteudo.append(
        Paragraph("Relatorio de Analise FinOps", titulo)
    )

    conteudo.append(
        Paragraph(
            "Analise demonstrativa de custos e oportunidades de otimizacao.",
            estilos["Normal"],
        )
    )

    conteudo.append(Spacer(1, 0.5 * cm))

    conteudo.append(
        Paragraph(
            f"Custo mensal total estimado: USD {custo_total:.2f}",
            estilos["Heading2"],
        )
    )

    conteudo.append(
        Paragraph(
            f"Economia potencial estimada: USD {economia_total:.2f}",
            estilos["Heading2"],
        )
    )

    conteudo.append(Spacer(1, 0.5 * cm))

    tabela_dados = [
        [
            "Instancia",
            "Departamento",
            "Custo mensal (USD)",
            "Acao FinOps",
            "Economia potencial (USD)",
        ]
    ]

    for _, linha in dados.iterrows():
        tabela_dados.append(
            [
                str(linha["instancia_id"]),
                str(linha["departamento"]),
                f'{linha["custo_mensal_atual_usd"]:.2f}',
                str(linha["acao_finops"]),
                f'{linha["economia_potencial_usd"]:.2f}',
            ]
        )

    
    tabela = Table(
        tabela_dados,
        colWidths=[2.2 * cm, 3.0 * cm, 3.0 * cm, 8.0 * cm, 3.0 * cm],
        repeatRows=1,
    )

    tabela.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#243B53")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )

    conteudo.append(tabela)

    conteudo.append(Spacer(1, 0.5 * cm))

    conteudo.append(
        Paragraph(
            "Observacao: os dados sao ficticios. A economia potencial "
            "e uma estimativa baseada nas regras do projeto, nao uma "
            "economia real confirmada. Qualquer acao exige validacao.",
            estilos["Italic"],
        )
    )

    documento.build(conteudo)

    return caminho_pdf
