import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt
from keras.models import load_model

model = load_model("mnist_model.keras")

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_test_s = x_test.astype("float32") / 255
x_test_s = np.expand_dims(x_test_s, -1)

y_pred = np.argmax(model.predict(x_test_s), axis=1)

wrong = np.where(y_pred != y_test)[0]

plt.figure(figsize=(12, 3))
for i in range(5):
    idx = wrong[i]
    plt.subplot(1, 5, i + 1)
    plt.imshow(x_test[idx], cmap="gray")
    plt.title(f"Stvarno: {y_test[idx]}\nPredikcija:{y_pred[idx]}")
    plt.axis("off")
plt.tight_layout()
plt.show()