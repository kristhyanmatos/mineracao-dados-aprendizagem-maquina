import ssl
import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

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
dados_colunas_uteis = dados_brutos[
    [
        "GRAU_RISCO",
        "STATUS_ANALISE",
        "PRODUTO_MOTIVO",
        "TIPO_REACAO_TRANSFUSIONAL",
        "TIPO_HEMOCOMPONENTE",
        "FAIXA_ETARIA_PACIENTE",
        "DS_TEMPORALIDADE_REACAO",
    ]
]

# Remove ruídos
dados_sem_ruidos = dados_colunas_uteis[
    (dados_colunas_uteis["GRAU_RISCO"] != "Não informado")
    & (dados_colunas_uteis["GRAU_RISCO"] != "Grau IV  - Óbito")
    & (dados_colunas_uteis["TIPO_HEMOCOMPONENTE"] != "NÃO INFORMADO")
    & (dados_colunas_uteis["DS_TEMPORALIDADE_REACAO"] != "Não informado")
    & (dados_colunas_uteis["TIPO_REACAO_TRANSFUSIONAL"].notnull())
]

# Normatização dos dados
dados_sem_ruidos["STATUS_ANALISE"].replace(
    {
        "Não Concluída": 0,
        "Concluída": 1,
    },
    inplace=True,
)

dados_sem_ruidos["PRODUTO_MOTIVO"].replace(
    {
        "Uso de sangue ou componente": 0,
    },
    inplace=True,
)

dados_sem_ruidos["TIPO_REACAO_TRANSFUSIONAL"].replace(
    {
        "Reação alérgica (ALG)": 0,
        "Reação febril não hemolítica (RFNH)": 1,
        "Sobrecarga circulatória associada à transfusão (SC/TACO)": 2,
        "Aloimunização/Aparecimento de anticorpos irregulares (ALO/PAI)": 3,
        "Outras reações imediatas (OI)": 4,
        "Lesão pulmonar aguda relacionada à transfusçao (TRALI)": 5,
        "Reação hipotensiva relacionada à transfusão (HIPOT)": 6,
        "Reação hemolítica aguda imunológica (RHAI)": 7,
        "Anafilática (notificadas até 2016)": 8,
        "Reação por contaminação bacteriana (CB)": 9,
        "Outras reações tardias (OT)": 10,
        "Reação hemolítica aguda não imune (RHANI)": 11,
        "Transmissão de doença infecciosa (DT)": 12,
        "Reação hemolítica tardia  (RHT)": 13,
        "Dispneia associada à transfusão (DAT)": 14,
        "Dor aguda relacionada à transfusão (DA)": 15,
        "Distúrbios Metabólicos (DMETAB)": 16,
        "Doença do enxerto contra o hospedeiro pós-transfusional (DECH/GVHD)": 17,
        "Hemossiderose com comprometimento de órgão (HEMOS)": 18,
        "Púrpura pós-transfusional (PPT)": 19,
    },
    inplace=True,
)

dados_sem_ruidos["GRAU_RISCO"].replace(
    {
        "Grau I   - Leve": 0,
        "Grau II  - Moderado": 1,
        "Grau III - Grave": 2,
    },
    inplace=True,
)

dados_sem_ruidos["TIPO_HEMOCOMPONENTE"].replace(
    {
        "OUTRO": 0,
        "CONCENTRADO DE HEMÁCIAS": 1,
        "CONCENTRADO DE PLAQUETAS": 2,
        "PLASMA FRESCO CONGELADO": 3,
        "CONCENTRADO DE HEMÁCIAS  +  PLASMA FRESCO CONGELADO": 4,
        "CONCENTRADO DE HEMÁCIAS  +  CONCENTRADO DE PLAQUETAS": 5,
        "CONCENTRADO DE HEMÁCIAS  +  OUTRO": 6,
        "CONCENTRADO DE HEMÁCIAS  +  CONCENTRADO DE PLAQUETAS  +  PLASMA FRESCO CONGELADO": 7,
        "CRIOPRECIPITADO": 8,
        "CONCENTRADO DE GRANULÓCITOS": 9,
        "CONCENTRADO DE PLAQUETAS  +  PLASMA FRESCO CONGELADO": 10,
        "CRIOPRECIPITADO  +  PLASMA FRESCO CONGELADO": 11,
        "SANGUE TOTAL": 12,
        "CONCENTRADO DE HEMÁCIAS  +  PLASMA - OUTRO TIPO": 13,
        "CONCENTRADO DE HEMÁCIAS  +  SANGUE TOTAL": 14,
        "CONCENTRADO DE HEMÁCIAS  +  OUTRO  +  PLASMA - OUTRO TIPO": 15,
        "SANGUE TOTAL RECONSTITUÍDO": 16,
        "CONCENTRADO DE HEMÁCIAS  +  CONCENTRADO DE PLAQUETAS  +  CRIOPRECIPITADO  +  PLASMA FRESCO CONGELADO": 17,
        "CONCENTRADO DE HEMÁCIAS  +  CRIOPRECIPITADO  +  PLASMA FRESCO CONGELADO": 18,
        "CONCENTRADO DE HEMÁCIAS  +  PLASMA - OUTRO TIPO  +  PLASMA FRESCO CONGELADO": 19,
        "CONCENTRADO DE PLAQUETAS  +  OUTRO": 20,
        "PLASMA - OUTRO TIPO  +  PLASMA FRESCO CONGELADO": 21,
        "CONCENTRADO DE HEMÁCIAS  +  CONCENTRADO DE PLAQUETAS  +  CRIOPRECIPITADO": 22,
        "CONCENTRADO DE PLAQUETAS  +  CRIOPRECIPITADO  +  PLASMA FRESCO CONGELADO": 23,
        "CONCENTRADO DE PLAQUETAS  +  CRIOPRECIPITADO": 24,
        "CONCENTRADO DE GRANULÓCITOS  +  CRIOPRECIPITADO  +  PLASMA FRESCO CONGELADO": 25,
        "CONCENTRADO DE HEMÁCIAS  +  CRIOPRECIPITADO": 26,
        "CONCENTRADO DE HEMÁCIAS  +  CONCENTRADO DE PLAQUETAS  +  PLASMA - OUTRO TIPO": 27,
        "CONCENTRADO DE PLAQUETAS  +  PLASMA - OUTRO TIPO": 28,
        "CONCENTRADO DE HEMÁCIAS  +  OUTRO  +  PLASMA FRESCO CONGELADO": 29,
        "CONCENTRADO DE PLAQUETAS  +  PLASMA - OUTRO TIPO  +  PLASMA FRESCO CONGELADO": 30,
        "CRIOPRECIPITADO  +  OUTRO": 31,
        "CONCENTRADO DE GRANULÓCITOS  +  CONCENTRADO DE PLAQUETAS  +  CRIOPRECIPITADO": 32,
        "CRIOPRECIPITADO  +  OUTRO  +  PLASMA FRESCO CONGELADO": 33,
        "CONCENTRADO DE HEMÁCIAS  +  CONCENTRADO DE PLAQUETAS  +  OUTRO": 34,
        "CONCENTRADO DE HEMÁCIAS  +  CONCENTRADO DE PLAQUETAS  +  PLASMA - OUTRO TIPO  +  PLASMA FRESCO CONGELADO": 35,
        "CONCENTRADO DE GRANULÓCITOS  +  CONCENTRADO DE PLAQUETAS": 36,
        "PLASMA DE DOADOR CONVALESCENTE": 37,
        "PLASMA - OUTRO TIPO": 38,
        "OUTRO  +  PLASMA FRESCO CONGELADO": 39,
    },
    inplace=True,
)

dados_sem_ruidos["FAIXA_ETARIA_PACIENTE"].replace(
    {
        "< 1 ANO": 0,
        "DE 1 A 4 ANOS": 1,
        "DE 5 A 9 ANOS": 2,
        "DE 10 A 19 ANOS": 3,
        "DE 20 A 29 ANOS": 4,
        "DE 30 A 39 ANOS": 5,
        "DE 40 A 49 ANOS": 6,
        "DE 50 A 59 ANOS": 7,
        "DE 60 A 69 ANOS": 8,
        "MAIOR DE 70 ANOS": 9,
    },
    inplace=True,
)
dados_sem_ruidos["DS_TEMPORALIDADE_REACAO"].replace(
    {
        "IMEDIATA": 0,
        "TARDIA": 1,
    },
    inplace=True,
)

dados_sem_ruidos.to_csv("dados.csv")

#
print("Quantidad de dados: ")

print("Grau I - Leve: ", len(dados_sem_ruidos[dados_sem_ruidos["GRAU_RISCO"] == 0]))
print(len(dados_sem_ruidos[dados_sem_ruidos["GRAU_RISCO"] == 1]))
print(len(dados_sem_ruidos[dados_sem_ruidos["GRAU_RISCO"] == 2]))

entradas = dados_sem_ruidos[
    [
        "STATUS_ANALISE",
        "PRODUTO_MOTIVO",
        "TIPO_REACAO_TRANSFUSIONAL",
        "TIPO_HEMOCOMPONENTE",
        "FAIXA_ETARIA_PACIENTE",
        "DS_TEMPORALIDADE_REACAO",
    ]
]
saidas = dados_sem_ruidos["GRAU_RISCO"]

numero_neighbors = 10

entradas_treino, entradas_teste, saidas_treino, saidas_teste = train_test_split(
    entradas,
    saidas,
    test_size=0.3,
    random_state=13,
)

modelo = KNeighborsClassifier(n_neighbors=numero_neighbors)
modelo.fit(entradas_treino, saidas_treino)

resultado = modelo.predict(entradas_teste)

print(
    classification_report(
        saidas_teste,
        resultado,
        target_names=[
            "Grau I - Leve",
            "Grau II - Moderado",
            "Grau III - Grave",
        ],
    )
)
