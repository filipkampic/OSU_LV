import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("LV2 Rad s bibliotekama Numpy i Matplotlib-20250310/data.csv", delimiter=",", skiprows=1)

# a)
broj_osoba = data.shape[0]
print(f"Broja osoba u istraživanju: {broj_osoba}")

# b)
visina = data[:, 1]
masa = data[:, 2]

plt.scatter(visina, masa, color="b", alpha=0.5)
plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Odnosi visine i mase")
plt.grid(True)
plt.show()

# c)
plt.scatter(visina[::50], masa[::50], color="b", alpha=0.5)
plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Odnosi visine i mase (svaka 50. osoba)")
plt.grid(True)
plt.show()

# d)
print(f"Minimalna visina: {np.min(visina)} cm")
print(f"Maksimalna visina: {np.max(visina)} cm")
print(f"Prosječna visina: {np.mean(visina):.2f} cm")

# e)
muskarci = data[data[:, 0] == 1]
zene = data[data[:, 0] == 0]

print("\nMuškarci:")
print(f"Minimalna visina: {np.min(muskarci[:, 1])} cm")
print(f"Maksimalna visina: {np.max(muskarci[:, 1])} cm")
print(f"Prosječna visina: {np.mean(muskarci[:, 1]):.2f} cm")

print("\nŽene:")
print(f"Minimalna visina: {np.min(zene[:, 1])} cm")
print(f"Maksimalna visina: {np.max(zene[:, 1])} cm")
print(f"Prosječna visina: {np.mean(zene[:, 1]):.2f} cm")
