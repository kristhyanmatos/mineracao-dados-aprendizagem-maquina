from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


class AprendizagemRNA:
    def __init__(self, dados) -> None:
        __dados = dados

        entradas_treino, entradas_teste, saidas_treino, saidas_teste = train_test_split(
            __dados.entradas,
            __dados.saidas,
            test_size=0.3,
            random_state=1,
        )

        modelo = MLPClassifier(random_state=1, max_iter=300)
        modelo.fit(entradas_treino, saidas_treino)

        self.resultado = modelo.predict(entradas_teste)

        print(
            classification_report(
                saidas_teste,
                self.resultado,
                target_names=[
                    "Grau I - Leve",
                    "Grau II - Moderado",
                    "Grau III - Grave",
                ],
            )
        )
