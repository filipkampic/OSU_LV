import numpy as np
import matplotlib
import matplotlib.pyplot as plt
 
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# a)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap="coolwarm", marker='o', label="Podaci za učenje")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap="coolwarm", marker='x', label="Podaci za testiranje")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Podaci za učenje i testiranje u ravnini x1-x2")
plt.legend()
plt.show()

# b)
LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)

# c)
theta0 = LogRegression_model.intercept_[0]
theta1, theta2 = LogRegression_model.coef_[0]

print(f"Parametri modela:\nTheta0 = {theta0:.2f}, Theta1 = {theta1:.2f}, Theta2 = {theta2:.2f}")

x1_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
x2_values = -(theta0 + theta1 * x1_values) / theta2

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap="coolwarm", marker='o', label="Podaci za učenje")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap="coolwarm", marker='x', label="Podaci za testiranje")
plt.plot(x1_values, x2_values, "k--", label="Granica odluke")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Granica odluke u ravnini x1-x2")
plt.legend()
plt.show()

# d)
y_test_p = LogRegression_model.predict(X_test)

cm = confusion_matrix(y_test, y_test_p)
disp = ConfusionMatrixDisplay(cm)
disp.plot()
plt.title("Matrica zabune")
plt.show()

acc = accuracy_score(y_test, y_test_p)
prec = precision_score(y_test, y_test_p)
rec = recall_score(y_test, y_test_p)

print(f"Točnost: {acc:.3f}")
print(f"Preciznost: {prec:.3f}")
print(f"Odziv: {rec:.3f}")

# e)
plt.scatter(X_test[y_test == y_test_p, 0], X_test[y_test == y_test_p, 1], c='g')
plt.scatter(X_test[y_test != y_test_p, 0], X_test[y_test != y_test_p, 1], c='k')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Testni skup - zeleno: točno, crno: pogrešno klasificirani")
plt.show()
