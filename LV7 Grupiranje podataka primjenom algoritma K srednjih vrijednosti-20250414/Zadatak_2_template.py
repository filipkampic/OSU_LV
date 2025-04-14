import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img_path = "imgs\\imgs\\test_1.jpg"
img = Image.imread(img_path)

# prikazi originalnu sliku
# plt.figure()
# plt.title("Originalna slika")
# plt.imshow(img)
# plt.tight_layout()
# plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
if "test_4.jpg" not in img_path:
    img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

# zadatak 1
unique_colors = np.unique(img_array, axis=0)
num_unique_colors = unique_colors.shape[0]

print(f"Broj različitih boja u slici: {num_unique_colors}")

# zadatak 2
km = KMeans(n_clusters=5, init="k-means++", n_init=5, random_state=0)
km.fit(img_array)
labels = km.predict(img_array)
centers = km.cluster_centers_

img_array_aprox = centers[labels]
img_aprox = img_array_aprox.reshape(w, h, d)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Originalna slika")
plt.imshow(img)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Rekonstruirana slika (K-Means (5 boja))")
plt.imshow(img_aprox)
plt.axis("off")

plt.tight_layout()
plt.show()

# zadatak 3
inertias = []
K_range = range(1, 11)

for n_clusters in K_range:
    kmeans = KMeans(n_clusters=n_clusters, init="k-means++", n_init=5, random_state=0)
    kmeans.fit(img_array)
    inertias.append(kmeans.inertia_)
    
plt.figure()
plt.plot(K_range, inertias, marker='o')
plt.title("Lakat metoda")
plt.xlabel("Broj klastera")
plt.ylabel("Inercija")
plt.tight_layout()
plt.show()

# zadatak 4
n_clusters = 2
km = KMeans(n_clusters=n_clusters, init="k-means++", n_init=5, random_state=0)
km.fit(img_array)
labels = km.predict(img_array)

for cluster in range(n_clusters):
    binary_mask = (labels == cluster).astype(np.uint8)
    binary_image = binary_mask.reshape(w, h)

    plt.figure()
    plt.title(f"Binarna slika za grupu {cluster}")
    plt.imshow(binary_image, cmap="gray")
    plt.axis("off")
    plt.show()
