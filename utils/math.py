import json
import numpy as np
from sklearn.linear_model import LinearRegression


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
        win_data.append(value[1])

X = np.array(data)
y = np.array(win_data)


# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# A função F(x) é representada por esses coeficientes
print("Coeficientes (c_n):", model.coef_)
print("Termo de intercepção (b):", model.intercept_)



# "expectedAember": 16.0025,
# "aemberControl": 8.16,
# "creatureControl": 12.5425,
# "creatureProtection": 1.8,
# "effectivePower": 32,
# "disruption": 0.78
# Exemplo de como usar a função para prever um novo valor
new_x = np.array([[16.0025, 8.16, 12.5425, 1.8, 32, 0.78]])
prediction = model.predict(new_x)
print("Valor previsto para o X original:", prediction)
