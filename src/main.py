from aprendizagem.arvore_decisao import AprendizagemArvoreDecisao
from aprendizagem.knn import AprendizagemKNN
from aprendizagem.rna import AprendizagemRNA
from pre_processamento_dados import PreProcesssamentoDados

dados = PreProcesssamentoDados()
knn = AprendizagemKNN(numero_neighbors=10, dados=dados)
arvore_decisao = AprendizagemRNA(dados=dados)
arvore_decisao = AprendizagemArvoreDecisao(dados=dados)
