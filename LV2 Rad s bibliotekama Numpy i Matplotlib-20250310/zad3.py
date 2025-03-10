import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("LV2 Rad s bibliotekama Numpy i Matplotlib-20250310/road.jpg")

# a)
bright_img = np.clip(img * 1.5, 0, 255).astype(np.uint8)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(bright_img)
plt.title("Posvijetljena slika")
plt.axis("off")

plt.show()

# b) 
visina, sirina, _ = img.shape
cetvrtina_slike = img[:, sirina//4:sirina//2]

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cetvrtina_slike)
plt.title("Druga četvrtina slike")
plt.axis("off")

plt.show()

# c) 
rotirana_slika = np.rot90(img, k=-1)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rotirana_slika)
plt.title("Rotirana slika")
plt.axis("off")

plt.show()

# d)
zrcalna_slika = np.flip(img, axis=1)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(zrcalna_slika)
plt.title("Zrcalna slika")
plt.axis("off")

plt.show()
