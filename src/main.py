from aprendizagem.arvore_decisao import AprendizagemArvoreDecisao
from aprendizagem.knn import AprendizagemKNN
from pre_processamento_dados import PreProcesssamentoDados

dados = PreProcesssamentoDados()
# knn = AprendizagemKNN(numero_neighbors=10, dados=dados)
arvore_decisao = AprendizagemArvoreDecisao(dados=dados)
