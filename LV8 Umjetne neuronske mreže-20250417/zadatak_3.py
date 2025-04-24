from PIL import Image
import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt
from keras.models import load_model

def preprocess_image(img_path):
    img = Image.open(img_path).convert('L').resize((28, 28))
    img_array = np.array(img)

    img_array = img_array.astype("float32") / 255
    img_array = np.expand_dims(img_array, axis=(0, -1))

    return img_array

model = load_model("mnist_model.keras")
img = preprocess_image("test4.png")
pred = model.predict(img)
pred_label = np.argmax(pred)
print(f"Predikcija: {pred_label}")
