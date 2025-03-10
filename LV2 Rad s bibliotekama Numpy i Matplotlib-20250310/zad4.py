import numpy as np
import matplotlib.pyplot as plt

crno = np.zeros((50, 50))
bijelo = np.full((50, 50), 255)

gornji_red = np.hstack((crno, bijelo))
donji_red = np.hstack((bijelo, crno))

slika = np.vstack((gornji_red, donji_red))

plt.imshow(slika, cmap="gray")
plt.show()