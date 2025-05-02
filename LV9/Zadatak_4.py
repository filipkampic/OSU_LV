import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from matplotlib import pyplot as plt
import os

def train_cnn_model(name, batch_size=64, optimizer='adam', use_small_model=False, use_small_dataset=False):
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    plt.figure(figsize=(6,6))
    for i in range(9):
        plt.subplot(330 + 1 + i)
        plt.imshow(X_train[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()

    if use_small_dataset:
        X_train = X_train[:len(X_train)//2]
        y_train = y_train[:len(y_train)//2]

    X_train_n = X_train.astype('float32') / 255.0
    X_test_n = X_test.astype('float32') / 255.0

    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    model = keras.Sequential()
    model.add(layers.Input(shape=(32,32,3)))

    if use_small_model:
        model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(10, activation='softmax'))
    else:
        model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Dropout(0.3))
        model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Dropout(0.3))
        model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(500, activation='relu'))
        model.add(layers.Dropout(0.3))
        model.add(layers.Dense(10, activation='softmax'))

    model.summary()

    log_dir = f"logs/cnn_{name}"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    callbacks = [
        keras.callbacks.TensorBoard(log_dir=log_dir, update_freq=100),
        keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    ]

    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    history = model.fit(
        X_train_n, y_train,
        epochs=40,
        batch_size=batch_size,
        validation_split=0.1,
        callbacks=callbacks,
        verbose=2
    )

    score = model.evaluate(X_test_n, y_test, verbose=0)
    print(f"Točnost na testnom skupu: {100*score[1]:.2f}%")

# train_cnn_model("baseline")                        
# train_cnn_model("small_batch", batch_size=32)      
# train_cnn_model("different_optimizer", optimizer='adamax')  
# train_cnn_model("small_model", use_small_model=True)  
# train_cnn_model("small_dataset", use_small_dataset=True)   

# 1. Manji batch size vodi do nestabilnijeg učenja, ali može poboljšati generalizaciju.
# 2. Drugačiji optimizer može značajno promijeniti brzinu i kvalitetu učenja.
# 3. Manja mreža uči brže, ali ima manju maksimalnu točnost.
# 4. Smanjeni skup za učenje uzrokuje manju točnost jer mreža vidi manje primjera.
