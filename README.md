# Projeto FinOps — Análise e Otimização de Custos

## Sobre o projeto

Este projeto demonstra uma aplicação em Python para analisar custos estimados de infraestrutura em nuvem, identificar possíveis oportunidades de otimização e gerar um relatório financeiro em PDF.

A aplicação utiliza dados fictícios para simular a análise de instâncias, considerando custo por hora, utilização média de CPU, atividade nos finais de semana e tempo desde o último acesso.

## Funcionalidades

* Leitura de dados a partir de arquivo CSV.
* Validação das informações de entrada.
* Cálculo do custo mensal estimado por instância.
* Classificação de recursos conforme regras de análise FinOps.
* Estimativa de economia potencial.
* Geração de relatório em PDF.
* Testes automatizados das principais funções.

## Tecnologias utilizadas

* Python
* Pandas
* NumPy
* ReportLab
* unittest

## Estrutura do projeto

```text
meu_projeto_finops/
├── data/
│   └── custos_exemplo.csv
├── src/
│   ├── carregar_dados.py
│   ├── validar_dados.py
│   ├── analisar_custos.py
│   ├── regras_finops.py
│   └── gerar_relatorio.py
├── tests/
│   └── test_finops.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar

### 1. Instalar as dependências

```bash
python3 -m pip install -r requirements.txt
```

### 2. Executar a aplicação

```bash
python3 main.py
```

### 3. Executar os testes

```bash
python3 -m unittest discover -s tests -v
```

## Observações sobre os resultados

Os dados utilizados são fictícios e servem para fins de demonstração e aprendizagem.

Os custos mensais são estimativas baseadas em 720 horas por mês. A economia potencial é calculada a partir de regras simplificadas e não representa uma economia real confirmada.

Nenhum recurso de nuvem é acessado, alterado ou excluído automaticamente. Recomendações devem ser verificadas antes de qualquer ação.

## Objetivo de aprendizagem

O projeto foi desenvolvido para praticar Python, organização modular de código, análise de dados, automação de relatórios, testes automatizados e conceitos de FinOps.
