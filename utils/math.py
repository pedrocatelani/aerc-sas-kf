import json
import random as rd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split


# Função utilitária (é uma arma secreta que utilizaremos no futuro!)
def get_attributes_list(deck: object):
    ae = deck["expectedAember"]
    ac = deck["aemberControl"]
    cc = deck["creatureControl"]
    cp = deck["creatureProtection"]
    ep = deck["effectivePower"]
    dr = deck["disruption"]

    attributes = [ae, ac, cc, cp, ep, dr]

    return attributes


with open("model_result.json", "r") as payload:
    results = json.load(payload)

# Dados de exemplo retirados do model_result
data = []
win_data = []

for key, value in results.items():
    if key != "MODEL DECK - Joranhdeer, Eater of Duvida":
        data.append(get_attributes_list(value[0]))
        win_data.append(value[1])  # 2 para Wins, 1 para WinRate

X = np.array(data)
y = np.array(win_data)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42
)

# Cria uma instância de PolynomialFeatures com grau 2
# Isso adiciona atributos como x1^2, x2^2 e x1*x2
poly = PolynomialFeatures(degree=2, include_bias=False)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)


# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train_poly, y_train)


# Calculando o coeficiente de determinação
# Quanto mais próximo de 1.0, melhor, sendo acima de 0.75 considerado um sucesso
# Varia de -∞ a 1.0
predictions = model.predict(X_test_poly)
score = r2_score(y_test, predictions)
print(f"R-squared: {score}")

# A função F(x) é representada por esses coeficientes
print("Coeficientes (c_n):", model.coef_)
print("Termo de intercepção (b):", model.intercept_)


# Exemplo de como usar a função para prever um novo valor
tests = []
for i in range(0, 10):
    num = rd.randint(1, len(results))
    random_test = {
        "atr": get_attributes_list(results["Aliance{}".format(num)][0]),
        "expected": results["Aliance{}".format(num)][1],
        "deck": num,
    }
    tests.append(random_test)

for t in tests:
    new_x = np.array([t["atr"]])
    new_x_poly = poly.transform(new_x)
    prediction = model.predict(new_x_poly)
    print(
        "Valor previsto: {}, Valor esperado: {}, Indivíduo: {}".format(
            prediction, t["expected"], t["deck"]
        )
    )
