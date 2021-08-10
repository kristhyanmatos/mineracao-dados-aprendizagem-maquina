import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree


class AprendizagemArvoreDecisao:
    def __init__(self, dados) -> None:
        __dados = dados
        entradas_treino, entradas_teste, saidas_treino, saidas_teste = train_test_split(
            __dados.entradas_arvore_decisao,
            __dados.saidas,
            test_size=0.3,
            random_state=13,
        )

        arvore = DecisionTreeRegressor(max_depth=3)
        arvore.fit(entradas_treino, saidas_treino)

        self.resultado = arvore.predict(entradas_teste)

        print(np.sqrt(mean_squared_error(saidas_teste, self.resultado)))

        plt.figure(figsize=(10, 5))
        plot_tree(arvore, feature_names=entradas_treino.columns)
        plt.show()
