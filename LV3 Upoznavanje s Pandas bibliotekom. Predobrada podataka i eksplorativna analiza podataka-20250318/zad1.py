"""
Zadatak 3.4.1 Skripta zadatak_1.py uˇcitava podatkovni skup iz data_C02_emission.csv .
Dodajte programski kod u skriptu pomo´cu kojeg možete odgovoriti na sljede´ca pitanja:
a) Koliko mjerenja sadrži DataFrame? Kojeg je tipa svaka veliˇcina? Postoje li izostale ili
duplicirane vrijednosti? Obrišite ih ako postoje. Kategoriˇcke veliˇcine konvertirajte u tip
category.
b) Koja tri automobila ima najve´cu odnosno najmanju gradsku potrošnju? Ispišite u terminal:
ime proizvo ¯daˇca, model vozila i kolika je gradska potrošnja.
c) Koliko vozila ima veliˇcinu motora izme ¯du 2.5 i 3.5 L? Kolika je prosjeˇcna C02 emisija
plinova za ova vozila?
d) Koliko mjerenja se odnosi na vozila proizvo ¯daˇca Audi? Kolika je prosjeˇcna emisija C02
plinova automobila proizvo ¯daˇca Audi koji imaju 4 cilindara?
e) Koliko je vozila s 4,6,8. . . cilindara? Kolika je prosjeˇcna emisija C02 plinova s obzirom na
broj cilindara?
f) Kolika je prosjeˇcna gradska potrošnja u sluˇcaju vozila koja koriste dizel, a kolika za vozila
koja koriste regularni benzin? Koliko iznose medijalne vrijednosti?
g) Koje vozilo s 4 cilindra koje koristi dizelski motor ima najve´cu gradsku potrošnju goriva?
h) Koliko ima vozila ima ruˇcni tip mjenjaˇca (bez obzira na broj brzina)?
i) Izraˇcunajte korelaciju izme ¯du numeriˇckih veliˇcina. Komentirajte dobiveni rezultat.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('LV3 Upoznavanje s Pandas bibliotekom. Predobrada podataka i eksplorativna analiza podataka-20250318/data_C02_emission.csv')

# a)
print("Broj mjerenja: ", data.shape[0])
print("\nTipovi podataka:\n", data.dtypes)
print("\nIzostale vrijednosti:\n", data.isnull().sum())
print("\nDuplicirane vrijednosti:", data.duplicated().sum())

category_columns = data.select_dtypes(include=['object']).columns
for column in category_columns:
    data[column] = data[column].astype('category')
print(data.dtypes)

# b)
top3_cars = data.nlargest(3, "Fuel Consumption City (L/100km)")
bottom3_cars = data.nsmallest(3, "Fuel Consumption City (L/100km)")
print("\nTri vozila s najvećom gradskom potrošnjom: \n", top3_cars[["Make", "Model", "Fuel Consumption City (L/100km)"]])
print("\nTri vozila s najmanjom gradskom potrošnjom: \n", bottom3_cars[["Make", "Model", "Fuel Consumption City (L/100km)"]])

# c)
filtered_cars = data[(data["Engine Size (L)"] >= 2.5) & (data["Engine Size (L)"] <= 3.5)]
print("\nBroj vozila s veličinom motora između 2.5 i 3.5:\n", len(filtered_cars))
print("Prosječna emisija CO2 tih vozila\n", filtered_cars["CO2 Emissions (g/km)"].mean())

# d)
audi_cars = data[data["Make"] == "Audi"]
print("\nBroj mjerenja za Audi: ", len(audi_cars))

audi_4_cylinders = audi_cars[audi_cars["Cylinders"] == 4]
print("\nProsječna emisija CO2 za Audi s 4 cilindra: ", audi_4_cylinders["CO2 Emissions (g/km)"].mean())

# e)
cylinder_counts = data["Cylinders"].value_counts().sort_index()
print("\nBroj vozila po broju cilindara:\n", cylinder_counts)

cylinder_emissions = data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean()
print("\nProječna emisija CO2 po broju cilindara:\n", cylinder_emissions)

# f)
diesel_cars = data[data["Fuel Type"] == 'D']
regular_gas_cars = data[data["Fuel Type"] == 'X']
print("\nProsječna gradska potrošnja za dizel: ", diesel_cars["Fuel Consumption City (L/100km)"].mean())
print("Prosječna gradska potrošnja za benzin: ", regular_gas_cars["Fuel Consumption City (L/100km)"].mean())

# g) 
highest_consumption_diesel_4_cylinders = diesel_cars[diesel_cars["Cylinders"] == 4].nlargest(1, "Fuel Consumption City (L/100km)")
print("\nVozilo s 4 cilindra na dizel s najvećom gradskom potrošnjom goriva:\n", highest_consumption_diesel_4_cylinders[["Make", "Model", "Fuel Consumption City (L/100km)"]])

# h)
manual_cars = data[data["Transmission"].str.startswith("M")]
print(f"\nBroj vozila s ručnim mjenjačem: {len(manual_cars)}\n")

# i)
correlation_matrix = data.corr(numeric_only=True)
print(correlation_matrix)

plt.imshow(correlation_matrix, cmap='coolwarm')
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Correlation Matrix Heatmap')
plt.show()