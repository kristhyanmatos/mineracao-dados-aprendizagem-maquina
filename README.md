# Mineração de dados e aprendizagem máquina

# Normatização dos dados

    - STATUS_ANALISE -
        [00] - Não Concluída
        [01] - Concluída

    - PRODUTO_MOTIVO -
        [00] - Uso de sangue ou componente

    - TIPO_REACAO_TRANSFUSIONAL -
        [00] - Reação alérgica (ALG)
        [01] - Reação febril não hemolítica (RFNH)
        [02] - Sobrecarga circulatória associada à transfusão (SC/TACO)
        [03] - Aloimunização/Aparecimento de anticorpos irregulares (ALO/PAI)
        [04] - Outras reações imediatas (OI)
        [05] - Lesão pulmonar aguda relacionada à transfusçao (TRALI)
        [06] - Reação hipotensiva relacionada à transfusão (HIPOT)
        [07] - Reação hemolítica aguda imunológica (RHAI)
        [08] - Anafilática (notificadas até 2016)
        [09] - Reação por contaminação bacteriana (CB)
        [10] - Outras reações tardias (OT)
        [11] - Reação hemolítica aguda não imune (RHANI)
        [12] - Transmissão de doença infecciosa (DT)
        [13] - Reação hemolítica tardia  (RHT)
        [14] - Dispneia associada à transfusão (DAT)
        [15] - Dor aguda relacionada à transfusão (DA)
        [16] - Distúrbios Metabólicos (DMETAB)
        [17] - Doença do enxerto contra o hospedeiro pós-transfusional (DECH/GVHD)
        [18] - Hemossiderose com comprometimento de órgão (HEMOS)
        [19] - Púrpura pós-transfusional (PPT)

    - GRAU_DE_RISCO -
        [00] - Grau I - Leve
        [01] - Grau II - Moderado
        [02] - Grau III - Grave
        [03] - Grau IV - Óbito

    - TIPO_HEMOCOMPONENTE -
        [00] - OUTRO
        [01] - CONCENTRADO DE HEMÁCIAS
        [02] - CONCENTRADO DE PLAQUETAS
        [03] - PLASMA FRESCO CONGELADO
        [04] - CONCENTRADO DE HEMÁCIAS + PLASMA FRESCO CONGELADO
        [05] - CONCENTRADO DE HEMÁCIAS + CONCENTRADO DE PLAQUETAS
        [06] - CONCENTRADO DE HEMÁCIAS + OUTRO' 'PLASMA - OUTRO TIPO
        [07] - CONCENTRADO DE HEMÁCIAS + CONCENTRADO DE PLAQUETAS + PLASMA FRESCO CONGELADO
        [08] - CRIOPRECIPITADO
        [09] - CONCENTRADO DE GRANULÓCITOS
        [10] - CONCENTRADO DE PLAQUETAS + PLASMA FRESCO CONGELADO
        [11] - CRIOPRECIPITADO + PLASMA FRESCO CONGELADO
        [12] - SANGUE TOTAL
        [13] - CONCENTRADO DE HEMÁCIAS + PLASMA - OUTRO TIPO
        [14] - CONCENTRADO DE HEMÁCIAS + SANGUE TOTAL
        [15] - CONCENTRADO DE HEMÁCIAS + OUTRO + PLASMA - OUTRO TIPO
        [16] - SANGUE TOTAL RECONSTITUÍDO
        [17] - CONCENTRADO DE HEMÁCIAS + CONCENTRADO DE PLAQUETAS + CRIOPRECIPITADO + PLASMA FRESCO CONGELADO
        [18] - CONCENTRADO DE HEMÁCIAS + CRIOPRECIPITADO + PLASMA FRESCO CONGELADO
        [19] - CONCENTRADO DE HEMÁCIAS + PLASMA - OUTRO TIPO + PLASMA FRESCO CONGELADO
        [20] - CONCENTRADO DE PLAQUETAS + OUTRO' 'OUTRO + PLASMA FRESCO CONGELADO
        [21] - PLASMA - OUTRO TIPO + PLASMA FRESCO CONGELADO
        [22] - CONCENTRADO DE HEMÁCIAS + CONCENTRADO DE PLAQUETAS + CRIOPRECIPITADO
        [23] - CONCENTRADO DE PLAQUETAS + CRIOPRECIPITADO + PLASMA FRESCO CONGELADO
        [24] - CONCENTRADO DE PLAQUETAS + CRIOPRECIPITADO
        [25] - CONCENTRADO DE GRANULÓCITOS + CRIOPRECIPITADO + PLASMA FRESCO CONGELADO
        [26] - CONCENTRADO DE HEMÁCIAS + CRIOPRECIPITADO
        [27] - CONCENTRADO DE HEMÁCIAS + CONCENTRADO DE PLAQUETAS + PLASMA - OUTRO TIPO
        [28] - CONCENTRADO DE PLAQUETAS + PLASMA - OUTRO TIPO
        [29] - CONCENTRADO DE HEMÁCIAS + OUTRO + PLASMA FRESCO CONGELADO
        [30] - CONCENTRADO DE PLAQUETAS + PLASMA - OUTRO TIPO + PLASMA FRESCO CONGELADO
        [31] - CRIOPRECIPITADO + OUTRO
        [32] - CONCENTRADO DE GRANULÓCITOS + CONCENTRADO DE PLAQUETAS + CRIOPRECIPITADO
        [33] - CRIOPRECIPITADO + OUTRO + PLASMA FRESCO CONGELADO
        [34] - CONCENTRADO DE HEMÁCIAS + CONCENTRADO DE PLAQUETAS + OUTRO
        [35] - CONCENTRADO DE HEMÁCIAS + CONCENTRADO DE PLAQUETAS + PLASMA - OUTRO TIPO + PLASMA FRESCO CONGELADO
        [36] - CONCENTRADO DE GRANULÓCITOS + CONCENTRADO DE PLAQUETAS
        [37] - PLASMA DE DOADOR CONVALESCENTE

    - FAIXA_ETARIA_PACIENTE -
        [00] - < 1 ANO
        [01] - DE 1 A 4 ANOS
        [02] - DE 5 A 9 ANOS
        [03] - DE 10 A 19 ANOS
        [04] - DE 20 A 29 ANOS
        [05] - DE 30 A 39 ANOS
        [06] - DE 40 A 49 ANOS
        [07] - DE 50 A 59 ANOS
        [08] - DE 60 A 69 ANOS
        [09] - MAIOR DE 70 ANOS

    - DS_TEMPORALIDADE_REACAO -
        [00] - IMEDIATA
        [01] - TARDIA
