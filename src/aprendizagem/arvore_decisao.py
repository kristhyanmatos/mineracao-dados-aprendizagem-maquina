import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree


class AprendizagemArvoreDecisao:
    def __init__(self, dados) -> None:
        __dados = dados
        entradas_treino, entradas_test, saidas_treino, saidas_test = train_test_split(
            __dados.entradas, __dados.saidas, test_size=0.3, random_state=13
        )

        arvore = DecisionTreeRegressor(max_depth=2)
        arvore.fit(entradas_treino, saidas_treino)

        resultado = arvore.predict(entradas_test)

        np.sqrt(mean_squared_error(saidas_test, resultado))
        print(np.sqrt(mean_squared_error(saidas_test, resultado)))

        plt.figure(figsize=(10, 5))
        plot_tree(arvore, feature_names=entradas_treino.columns)
        plt.show()
