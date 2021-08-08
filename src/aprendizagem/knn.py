from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


class AprendizagemKNN:
    def __init__(self, numero_neighbors, dados) -> None:
        __dados = dados

        self.numero_neighbors = numero_neighbors

        entradas_treino, entradas_teste, saidas_treino, saidas_teste = train_test_split(
            __dados.entradas,
            __dados.saidas,
            test_size=0.3,
            random_state=13,
        )

        modelo = KNeighborsClassifier(n_neighbors=self.numero_neighbors)
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
