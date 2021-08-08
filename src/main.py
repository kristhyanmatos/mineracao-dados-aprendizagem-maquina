import ssl
import pandas

ssl._create_default_https_context = ssl._create_unverified_context

# Fonte do dado
# https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_HEMOVIGILANCIA.csv

dados_brutos = pandas.read_csv(
    "DADOS_ABERTOS_HEMOVIGILANCIA.csv",
    encoding="ISO-8859-1",
    sep=";",
)

"""Pré-processamento"""

# Seleciona colunas úteis
dados_brutos = dados_brutos[
    [
        "STATUS_ANALISE",
        "PRODUTO_MOTIVO",
        "TIPO_REACAO_TRANSFUSIONAL",
        "GRAU_RISCO",
        "TIPO_HEMOCOMPONENTE",
        "FAIXA_ETARIA_PACIENTE",
        "DS_TEMPORALIDADE_REACAO",
    ]
]

# Remove ruídos
dados_brutos = dados_brutos[
    (dados_brutos["GRAU_RISCO"] != "Não informado")
    & (dados_brutos["TIPO_HEMOCOMPONENTE"] != "NÃO INFORMADO")
    & (dados_brutos["DS_TEMPORALIDADE_REACAO"] != "Não informado")
    & (dados_brutos["TIPO_REACAO_TRANSFUSIONAL"].notnull())
]

# Normatização dos dados
print(dados_brutos)

dados_brutos.to_csv("dados.csv")
