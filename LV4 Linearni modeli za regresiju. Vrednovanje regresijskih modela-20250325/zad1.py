"""
Zadatak 4.5.1 Skripta zadatak_1.py uˇcitava podatkovni skup iz data_C02_emission.csv.
 Potrebno je izgraditi i vrednovati model koji procjenjuje emisiju C02 plinova na temelju os
talih numeriˇckih ulaznih veliˇcina. Detalje oko ovog podatkovnog skupa mogu se prona´ci u 3.
 laboratorijskoj vježbi.
 a) Odaberite željene numeriˇ cke veliˇ cine specificiranjem liste s nazivima stupaca. Podijelite
 podatke na skup za uˇ cenje i skup za testiranje u omjeru 80%-20%.
 b) Pomo´ cu matplotlib biblioteke i dijagrama raspršenja prikažite ovisnost emisije C02 plinova
 o jednoj numeriˇckoj veliˇcini. Pri tome podatke koji pripadaju skupu za uˇcenje oznaˇcite
 plavom bojom, a podatke koji pripadaju skupu za testiranje oznaˇ cite crvenom bojom.
 c) Izvršite standardizaciju ulaznih veliˇ cina skupa za uˇ cenje. Prikažite histogram vrijednosti
 jedne ulazne veliˇ cine prije i nakon skaliranja. Na temelju dobivenih parametara skaliranja
 transformirajte ulazne veliˇ cine skupa podataka za testiranje.
 d) Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i
 povežite ih s izrazom 4.6.
 e) Izvršite procjenu izlazne veliˇ cine na temelju ulaznih veliˇ cina skupa za testiranje. Prikažite
 pomo´ cu dijagrama raspršenja odnos izme¯ du stvarnih vrijednosti izlazne veliˇ cine i procjene
 dobivene modelom.
 f) Izvršite vrednovanje modela na naˇcin da izraˇcunate vrijednosti regresijskih metrika na
 skupu podataka za testiranje.
 g) Što se doga¯ da s vrijednostima evaluacijskih metrika na testnom skupu kada mijenjate broj
 ulaznih veliˇ cina?
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error, root_mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, r2_score

data = pd.read_csv("data_C02_emission.csv")

# a)
input_variables = ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)", "Fuel Consumption Hwy (L/100km)", "Fuel Consumption Comb (L/100km)", "Fuel Consumption Comb (mpg)"]
output = "CO2 Emissions (g/km)"

X = data[input_variables]
y = data[output]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# b)
plt.scatter(X_train["Engine Size (L)"], y_train, c='b', label="Podaci učenja")
plt.scatter(X_test["Engine Size (L)"], y_test, c='r', label="Podaci testiranja")
plt.xlabel("Veličina motora (L)")
plt.ylabel("CO2 Emisija (g/km)")
plt.title("Emisija CO2 vs Veličina motora")
plt.legend()
plt.show()

# c) 
sc = StandardScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)

plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
plt.hist(X_train.iloc[:, input_variables.index("Engine Size (L)")], bins=20, color='b')
plt.title("Histogram veličine motora prije skaliranja")
plt.xlabel("Veličina motora (L)")
plt.ylabel("Broj primjera")

plt.subplot(1, 2, 2)
plt.hist(X_train_n[:, input_variables.index("Engine Size (L)")], bins=20, color='r')
plt.title("Histogram veličine motora nakon skaliranja")
plt.xlabel("Veličina motora (L)")
plt.ylabel("Broj primjera")

plt.tight_layout()
plt.show()

# d)
linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)

print(linearModel.intercept_)
print(linearModel.coef_)

# e) 
y_test_p = linearModel.predict(X_test_n)

plt.scatter(y_test, y_test_p, c='b')
plt.xlabel("Stvarne vrijednosti CO2 emisije (g/km)")
plt.ylabel("Predviđene vrijednosti CO2 emisije (g/km)")
plt.title("Stvarne vs Predviđene vrijednosti CO2 emisije")
plt.show()

# f)
MSE = mean_squared_error(y_test, y_test_p)
RMSE = root_mean_squared_error(y_test, y_test_p)
MAE = mean_absolute_error(y_test, y_test_p)
MAPE = mean_absolute_percentage_error(y_test, y_test_p)
R2 = r2_score(y_test, y_test_p)

print(f"MSE: {MSE}\nRMSE: {RMSE}\nMAE: {MAE}\nMAPE: {MAPE}\nR2: {R2}")
