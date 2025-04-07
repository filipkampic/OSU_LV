import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

def plot_decision_regions(X, y, classifier, resolution=0.02):
    plt.figure()
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
    np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    # plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl)


# ucitaj podatke
data = pd.read_csv("Social_Network_Ads.csv")
print(data.info())

data.hist()
plt.show()

# dataframe u numpy
X = data[["Age","EstimatedSalary"]].to_numpy()
y = data["Purchased"].to_numpy()

# podijeli podatke u omjeru 80-20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify=y, random_state = 10)

# skaliraj ulazne velicine
sc = StandardScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform((X_test))

# Model logisticke regresije
LogReg_model = LogisticRegression(penalty=None) 
LogReg_model.fit(X_train_n, y_train)

# Evaluacija modela logisticke regresije
y_train_p = LogReg_model.predict(X_train_n)
y_test_p = LogReg_model.predict(X_test_n)

print("Logisticka regresija: ")
print("Tocnost train: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
print("Tocnost test: " + "{:0.3f}".format((accuracy_score(y_test, y_test_p))))

# granica odluke pomocu logisticke regresije
plot_decision_regions(X_train_n, y_train, classifier=LogReg_model)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("Tocnost: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
plt.tight_layout()
plt.show()

"""
ZADATAK 1
"""
 # K=5
KNN_model_5 = KNeighborsClassifier(n_neighbors=5)
KNN_model_5.fit(X_train_n, y_train)

y_train_p_KNN = KNN_model_5.predict(X_train_n)
y_test_p_KNN = KNN_model_5.predict(X_test_n)

print("KNN (K=5):")
print("Točnost train: {:.3f}".format(accuracy_score(y_train, y_train_p_KNN)))
print("Točnost test: {:.3f}".format(accuracy_score(y_test, y_test_p_KNN)))

plot_decision_regions(X_train_n, y_train, classifier=KNN_model_5)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("Točnost (K=5): {:.3f}".format(accuracy_score(y_train, y_train_p_KNN)))
plt.tight_layout()
plt.show()

# K=1
KNN_model_1 = KNeighborsClassifier(n_neighbors=1)
KNN_model_1.fit(X_train_n, y_train)

y_train_p_KNN = KNN_model_1.predict(X_train_n)
y_test_p_KNN = KNN_model_1.predict(X_test_n)

print("KNN (K=1):")
print("Točnost train: {:.3f}".format(accuracy_score(y_train, y_train_p_KNN)))
print("Točnost test: {:.3f}".format(accuracy_score(y_test, y_test_p_KNN)))

plot_decision_regions(X_train_n, y_train, classifier=KNN_model_1)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("Točnost (K=1): {:.3f}".format(accuracy_score(y_train, y_train_p_KNN)))
plt.tight_layout()
plt.show()

# K=100
KNN_model_100 = KNeighborsClassifier(n_neighbors=100)
KNN_model_100.fit(X_train_n, y_train)

y_train_p_KNN = KNN_model_100.predict(X_train_n)
y_test_p_KNN = KNN_model_100.predict(X_test_n)

print("KNN (K=100):")
print("Točnost train: {:.3f}".format(accuracy_score(y_train, y_train_p_KNN)))
print("Točnost test: {:.3f}".format(accuracy_score(y_test, y_test_p_KNN)))

plot_decision_regions(X_train_n, y_train, classifier=KNN_model_100)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("Točnost (K=100): {:.3f}".format(accuracy_score(y_train, y_train_p_KNN)))
plt.tight_layout()
plt.show()


"""
ZADATAK 2
"""
K_range = range(1, 51)
cv_scores = []

for k in K_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train_n, y_train, cv=5)
    cv_scores.append(scores.mean())

optimal_k = K_range[np.argmax(cv_scores)]
print(f"Optimalni K prema unakrsnoj validaciji: {optimal_k}")
print(f"Najviša prosjčena točnost: {max(cv_scores):.3f}")

plt.plot(K_range, cv_scores)
plt.xlabel("Broj susjeda K")
plt.ylabel("Prosječna točnost (CV)")
plt.title("Odabir optimalnog K za KNN")
plt.grid()
plt.show()

"""
ZADATAK 3
"""
SVM_model_rbf = svm.SVC(kernel="rbf", gamma=1, C=1)
SVM_model_rbf.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, classifier=SVM_model_rbf)
plt.title("SVM RBF kernel (C=1, gamma=1)")
plt.show()

SVM_model_rbf = svm.SVC(kernel="rbf", gamma=0.1, C=1)
SVM_model_rbf.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, classifier=SVM_model_rbf)
plt.title("SVM RBF kernel (C=1, gamma=0.1)")
plt.show()

SVM_model_rbf = svm.SVC(kernel="rbf", gamma=1, C=0.1)
SVM_model_rbf.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, classifier=SVM_model_rbf)
plt.title("SVM RBF kernel (C=0.1, gamma=1)")
plt.show()

SVM_model_rbf = svm.SVC(kernel="rbf", gamma=1, C=10)
SVM_model_rbf.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, classifier=SVM_model_rbf)
plt.title("SVM RBF kernel (C=10, gamma=1)")
plt.show()

# Mijenjanje kernela
SVM_model_sigmoid = svm.SVC(kernel="sigmoid", gamma=1, C=1)
SVM_model_sigmoid.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, classifier=SVM_model_sigmoid)
plt.title("SVM sigmoid kernel (C=1, gamma=1)")
plt.show()

SVM_model_sigmoid = svm.SVC(kernel="sigmoid", gamma=0.1, C=1)
SVM_model_sigmoid.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, classifier=SVM_model_sigmoid)
plt.title("SVM sigmoid kernel (C=1, gamma=0.1)")
plt.show()

SVM_model_sigmoid = svm.SVC(kernel="sigmoid", gamma=1, C=0.1)
SVM_model_sigmoid.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, classifier=SVM_model_sigmoid)
plt.title("SVM sigmoid kernel (C=0.1, gamma=1)")
plt.show()

SVM_model_sigmoid = svm.SVC(kernel="sigmoid", gamma=1, C=10)
SVM_model_sigmoid.fit(X_train_n, y_train)
plot_decision_regions(X_train_n, y_train, classifier=SVM_model_sigmoid)
plt.title("SVM sigmoid kernel (C=10, gamma=1)")
plt.show()

"""
ZADATAK 4
"""
pipe = make_pipeline(StandardScaler(), svm.SVC(kernel="rbf"))

param_grid = {
    "svc__C": [0.1, 1, 10, 100],
    "svc__gamma": [0.01, 0.1, 1, 10]
}

svm_gscv = GridSearchCV(pipe, param_grid, cv=5, scoring="accuracy")
svm_gscv.fit(X_train, y_train)

print("Najbolje parametri (GridSearchCV):", svm_gscv.best_params_)
print("Najbolje točnost (CV): {:.3f}".format(svm_gscv.best_score_))

best_C = svm_gscv.best_params_["svc__C"]
best_gamma = svm_gscv.best_params_["svc__gamma"]

best_svm = svm.SVC(kernel="rbf", C=best_C, gamma=best_gamma)
best_svm.fit(X_train_n, y_train)

plot_decision_regions(X_train_n, y_train, classifier=best_svm)
plt.title(f"SVM - najbolji C={best_C}, gamma={best_gamma}")
plt.xlabel("x_1")
plt.ylabel("x_2")
plt.tight_layout()
plt.show()
