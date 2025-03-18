"""
Zadatak 3.4.2 Napišite programski kod koji ´ce prikazati sljede´ce vizualizacije:
a) Pomo´cu histograma prikažite emisiju C02 plinova. Komentirajte dobiveni prikaz.
b) Pomo´cu dijagrama raspršenja prikažite odnos izme ¯du gradske potrošnje goriva i emisije
C02 plinova. Komentirajte dobiveni prikaz. Kako biste bolje razumjeli odnose izme ¯du
veliˇcina, obojite toˇckice na dijagramu raspršenja s obzirom na tip goriva.
c) Pomo´cu kutijastog dijagrama prikažite razdiobu izvangradske potrošnje s obzirom na tip
goriva. Primje´cujete li grubu mjernu pogrešku u podacima?
d) Pomo´cu stupˇcastog dijagrama prikažite broj vozila po tipu goriva. Koristite metodu
groupby.
e) Pomo´cu stupˇcastog grafa prikažite na istoj slici prosjeˇcnu C02 emisiju vozila s obzirom na
broj cilindara.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('LV3 Upoznavanje s Pandas bibliotekom. Predobrada podataka i eksplorativna analiza podataka-20250318/data_C02_emission.csv')

# a)
plt.figure()
data["CO2 Emissions (g/km)"].plot(kind="hist", bins=20)
plt.xlabel("CO2 Emisija (g/km)")
plt.ylabel("Broj vozila")
plt.title("Histogram emisije (CO2)")
plt.show()

# b)
fuel_colors = {
    'X': "red",
    'Z': "green",
    'D': "blue",
    'E': 'purple',
    'N': "orange"
}

data.plot.scatter(x="Fuel Consumption City (L/100km)", y="CO2 Emissions (g/km)", c=data["Fuel Type"].map(fuel_colors), s=50, alpha=0.5)
plt.xlabel("Gradska potrošnja goriva (L/100km)")
plt.ylabel("CO2 Emisija (g/km)")
plt.title("Dijagram raspršenja: Gradska potrošnja vs CO2 emisija")
plt.show()

# c)
data.boxplot(column="CO2 Emissions (g/km)", by="Fuel Type")
plt.xlabel("Tip goriva")
plt.ylabel("Izvangradska potrošnja goriva (L/100km)")
plt.title("Kutijasti dijagram: Izvangradska potrošnja po tipu goriva")
plt.show()

# d)
fuel_counts = data.groupby("Fuel Type").size()
plt.bar(fuel_counts.index, fuel_counts.values, color=["blue", "red", "green", "purple", "orange"])
plt.xlabel("Tip goriva")
plt.ylabel("Broj vozila")
plt.title("Broj vozila po tipu goriva")
plt.show()

# e)
cylinder_emissions = data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean()
plt.bar(cylinder_emissions.index, cylinder_emissions.values)
plt.xlabel("Broj cilindara")
plt.ylabel("Prosječna CO2 emisija (g/km)")
plt.title("Prosječna CO2 emisija po broju cilindara")
plt.show()
