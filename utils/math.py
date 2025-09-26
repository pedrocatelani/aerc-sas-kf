import json
import random as rd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

# Função para gerar um arquivo para análise de dados.
def generate_predictions():
    tests = []
    for deck, value in results.items():
        random_test = {
            "atr": get_attributes_list(value[0]),
            "expected": value[1],
            "prediction": 0,
        }

        new_x = np.array([random_test["atr"]])
        new_x_poly = poly.transform(new_x)

        prediction = model.predict(new_x_poly)

        print(
            "Valor previsto: {}, Valor esperado: {}, Indivíduo: {}".format(
                prediction, random_test["expected"], deck
            )
        )
        random_test["prediction"] = float(prediction[0])

        tests.append(random_test)

    with open("cross-prediction.json", "w") as payload:
        json.dump(tests, payload)

# Função objetivo
def objective_function(coef: list, term: float, atr: object):
    ae = atr["expectedAember"]
    ac = atr["aemberControl"]
    cc = atr["creatureControl"]
    cp = atr["creatureProtection"]
    ep = atr["effectivePower"]
    dr = atr["disruption"]

    result = (
        (ae * coef[0])
        + (ac * coef[1])
        + (cc * coef[2])
        + (cp * coef[3])
        + (ep * coef[4])
        + (dr * coef[5])
        + ((ae**2) * coef[6])
        + ((ae * ac) * coef[7])
        + ((ae * cc) * coef[8])
        + ((ae * cp) * coef[9])
        + ((ae * ep) * coef[10])
        + ((ae * dr) * coef[11])
        + ((ac**2) * coef[12])
        + ((ac * cc) * coef[13])
        + ((ac * cp) * coef[14])
        + ((ac * ep) * coef[15])
        + ((ac * dr) * coef[16])
        + ((cc**2) * coef[17])
        + ((cc * cp) * coef[18])
        + ((cc * ep) * coef[19])
        + ((cc * dr) * coef[20])
        + ((cp**2) * coef[21])
        + ((cp * ep) * coef[22])
        + ((cp * dr) * coef[23])
        + ((ep**2) * coef[24])
        + ((ep * dr) * coef[25])
        + ((dr**2) * coef[26])
    ) + term

    return result

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
print(poly.get_feature_names_out(input_features=["ae", "ac", "cc", "cp", "ep", "dr"]))


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

generate_predictions()