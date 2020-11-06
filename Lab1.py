# import psutil

import pandas as pd

# import numpy as np


# Создание датафейма из файла .csv

dataframe = pd.read_csv("article.csv")
print(dataframe)

# Находим длину нашего датафрейма

n = len(dataframe)
print("\nДлина датафрейма: " + str(n))

import matplotlib.pyplot as plt

plt.figure()
plt.title("X1")
plt.plot(dataframe['x1'])
plt.show()
