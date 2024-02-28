import matplotlib.pyplot as plt

años = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
precios = [200000, 210000, 220000, 215000, 225000, 190000, 210000, 245000, 250000]

plt.bar(años, precios)

plt.title('Evolución del Precio de un Hogar en Euros (2015-2023)')
plt.xlabel('Año')
plt.ylabel('Precio en Euros')

plt.show()
