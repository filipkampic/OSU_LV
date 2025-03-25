import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error, root_mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, r2_score

data = pd.read_csv("data_C02_emission.csv")

input_variables = ["Fuel Type", "Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)", "Fuel Consumption Hwy (L/100km)", "Fuel Consumption Comb (L/100km)", "Fuel Consumption Comb (mpg)"]
output = "CO2 Emissions (g/km)"

X = data[input_variables]
y = data[output]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

ohe = OneHotEncoder()
X_encoded_train = ohe.fit_transform(X_train[["Fuel Type"]]).toarray()
X_encoded_test = ohe.transform(X_test[["Fuel Type"]]).toarray()

linearModel = lm.LinearRegression()
linearModel.fit(X_encoded_train, y_train)

y_test_p = linearModel.predict(X_encoded_test)

MSE = mean_squared_error(y_test, y_test_p)
RMSE = root_mean_squared_error(y_test, y_test_p)
MAE = mean_absolute_error(y_test, y_test_p)
MAPE = mean_absolute_percentage_error(y_test, y_test_p)
R2 = r2_score(y_test, y_test_p)

print(f"MSE: {MSE}\nRMSE: {RMSE}\nMAE: {MAE}\nMAPE: {MAPE}\nR2: {R2}")

errors = abs(y_test - y_test_p)
max_error = errors.max()
max_error_index = errors.idxmax()
max_error_model = data.loc[max_error_index, "Model"]
print(f"Max error: {max_error}, Model: {max_error_model}")