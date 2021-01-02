# import psutil

import pandas as pd
import numpy as np


# Создание датафейма из файла .csv

df = pd.read_csv('brazilian-malware.csv')
df

# Находим длину нашего датафрейма



import matplotlib.pyplot as plt

import seaborn as sns
sns.displot(df['Entropy'])
plt.show()

sns.displot(df['FirstSeenDate'])
plt.show()

sns.displot(df['NumberOfRvaAndSizes'])
plt.show()

sns.displot(df['NumberOfSections'])
plt.show()

sns.displot(df['NumberOfSymbols'])
plt.show()

sns.displot(df['PointerToSymbolTable'])
plt.show()

sns.displot(df['SizeOfImage'])
plt.show()

sns.displot(df['SizeOfInitializedData'])
plt.show()

sns.displot(df['SizeOfOptionalHeader'])
plt.show()

sns.displot(df['SizeOfUninitializedData'])
plt.show()

sns.displot(df['TimeDateStamp'])
plt.show()

# Области однородности для Entropy
ObbOdn1_Entropy = []
ObbOdn2_Entropy = []
ObbOdn3_Entropy = []
ObbOdn4_Entropy = []
ObbOdn5_Entropy = []
ObbOdn6_Entropy = []
ObbOdn7_Entropy = []
ObbOdn8_Entropy = []
ObbOdn9_Entropy = []
ObbOdn10_Entropy = []
ObbOdn11_Entropy = []
ObbOdn12_Entropy = []
ObbOdn13_Entropy = []
ObbOdn14_Entropy = []
ObbOdn15_Entropy = []
ObbOdn16_Entropy = []
ObbOdn17_Entropy = []
ObbOdn18_Entropy = []
ObbOdn19_Entropy = []
ObbOdn20_Entropy = []
for oblodn in df['Entropy']:
    if oblodn <= 0.85:
        ObbOdn1_Entropy.append(oblodn)
    if oblodn > 0.85 and oblodn <= 1.209:
        ObbOdn2_Entropy.append(oblodn)
    if oblodn > 1.209 and oblodn <= 1.475:
        ObbOdn3_Entropy.append(oblodn)
    if oblodn > 1.475 and oblodn <= 1.645:
        ObbOdn4_Entropy.append(oblodn)
    if oblodn > 1.645 and oblodn <= 2.185:
        ObbOdn5_Entropy.append(oblodn)
    if oblodn > 2.185 and oblodn <= 2.45:
        ObbOdn6_Entropy.append(oblodn)
    if oblodn > 2.45 and oblodn <= 2.985:
        ObbOdn7_Entropy.append(oblodn)
    if oblodn > 2.985 and oblodn <= 3.335:
        ObbOdn8_Entropy.append(oblodn)
    if oblodn > 3.335 and oblodn <= 3.515:
        ObbOdn9_Entropy.append(oblodn)
    if oblodn > 3.515 and oblodn <= 3.69:
        ObbOdn10_Entropy.append(oblodn)
    if oblodn > 3.69 and oblodn <= 3.865:
        ObbOdn11_Entropy.append(oblodn)
    if oblodn > 3.865 and oblodn <= 3.9:
        ObbOdn12_Entropy.append(oblodn)
    if oblodn > 3.9 and oblodn <= 4.755:
        ObbOdn13_Entropy.append(oblodn)
    if oblodn > 4.755 and oblodn <= 5.195:
        ObbOdn14_Entropy.append(oblodn)
    if oblodn > 5.195 and oblodn <= 5.465:
        ObbOdn15_Entropy.append(oblodn)
    if oblodn > 5.465 and oblodn <= 5.735:
        ObbOdn16_Entropy.append(oblodn)
    if oblodn > 5.735 and oblodn <= 6.085:
        ObbOdn17_Entropy.append(oblodn)
    if oblodn > 6.085 and oblodn <= 6.975:
        ObbOdn18_Entropy.append(oblodn)
    if oblodn > 6.975 and oblodn <= 7.33:
        ObbOdn19_Entropy.append(oblodn)
    if oblodn > 7.33 and oblodn <= 7.595:
        ObbOdn20_Entropy.append(oblodn)

# Математическое ожидание для Entropy
mean1_Entropy = np.mean(ObbOdn1_Entropy)
print(mean1_Entropy, "MEAN1_Entropy")
mean2_Entropy = np.mean(ObbOdn2_Entropy)
print(mean2_Entropy, "MEAN2_Entropy")
mean3_Entropy = np.mean(ObbOdn3_Entropy)
print(mean3_Entropy, "MEAN3_Entropy")
mean4_Entropy = np.mean(ObbOdn4_Entropy)
print(mean4_Entropy, "MEAN4_Entropy")
mean5_Entropy = np.mean(ObbOdn5_Entropy)
print(mean5_Entropy, "MEAN5_Entropy")
mean6_Entropy = np.mean(ObbOdn6_Entropy)
print(mean6_Entropy, "MEAN6_Entropy")
mean7_Entropy = np.mean(ObbOdn7_Entropy)
print(mean7_Entropy, "MEAN7_Entropy")
mean8_Entropy = np.mean(ObbOdn8_Entropy)
print(mean8_Entropy, "MEAN8_Entropy")
mean9_Entropy = np.mean(ObbOdn9_Entropy)
print(mean9_Entropy, "MEAN9_Entropy")
mean10_Entropy = np.mean(ObbOdn10_Entropy)
print(mean10_Entropy, "MEAN10_Entropy")
mean11_Entropy = np.mean(ObbOdn11_Entropy)
print(mean11_Entropy, "MEAN11_Entropy")
mean12_Entropy = np.mean(ObbOdn12_Entropy)
print(mean12_Entropy, "MEAN12_Entropy")
mean13_Entropy = np.mean(ObbOdn13_Entropy)
print(mean13_Entropy, "MEAN13_Entropy")
mean14_Entropy = np.mean(ObbOdn14_Entropy)
print(mean14_Entropy, "MEAN14_Entropy")
mean15_Entropy = np.mean(ObbOdn15_Entropy)
print(mean15_Entropy, "MEAN15_Entropy")
mean16_Entropy = np.mean(ObbOdn16_Entropy)
print(mean16_Entropy, "MEAN16_Entropy")
mean17_Entropy = np.mean(ObbOdn17_Entropy)
print(mean17_Entropy, "MEAN17_Entropy")
mean18_Entropy = np.mean(ObbOdn18_Entropy)
print(mean18_Entropy, "MEAN18_Entropy")
mean19_Entropy = np.mean(ObbOdn19_Entropy)
print(mean19_Entropy, "MEAN19_Entropy")
mean20_Entropy = np.mean(ObbOdn20_Entropy)
print(mean20_Entropy, "MEAN20_Entropy")


# Среднеквадратическое отклонение для Entropy
std1_Entropy = np.std(ObbOdn1_Entropy)
print(std1_Entropy)
std2_Entropy = np.std(ObbOdn2_Entropy)
print(std2_Entropy)
std3_Entropy = np.std(ObbOdn3_Entropy)
print(std3_Entropy)
std4_Entropy = np.std(ObbOdn4_Entropy)
print(std4_Entropy)
std5_Entropy = np.std(ObbOdn5_Entropy)
print(std5_Entropy)
std6_Entropy = np.std(ObbOdn6_Entropy)
print(std6_Entropy)
std7_Entropy = np.std(ObbOdn7_Entropy)
print(std7_Entropy)
std8_Entropy = np.std(ObbOdn8_Entropy)
print(std8_Entropy)
std9_Entropy = np.std(ObbOdn9_Entropy)
print(std9_Entropy)
std10_Entropy = np.std(ObbOdn10_Entropy)
print(std10_Entropy)
std11_Entropy = np.std(ObbOdn11_Entropy)
print(std11_Entropy)
std12_Entropy = np.std(ObbOdn12_Entropy)
print(std12_Entropy)
std13_Entropy = np.std(ObbOdn13_Entropy)
print(std13_Entropy)
std14_Entropy = np.std(ObbOdn14_Entropy)
print(std14_Entropy)
std15_Entropy = np.std(ObbOdn15_Entropy)
print(std15_Entropy)
std16_Entropy = np.std(ObbOdn16_Entropy)
print(std16_Entropy)
std17_Entropy = np.std(ObbOdn17_Entropy)
print(std17_Entropy)
std18_Entropy = np.std(ObbOdn18_Entropy)
print(std18_Entropy)
std19_Entropy = np.std(ObbOdn19_Entropy)
print(std19_Entropy)
std20_Entropy = np.std(ObbOdn20_Entropy)
print(std20_Entropy)

# Отрицательный доверительный интервал для Entropy
otric_dover_int_Entropy_1 = mean1_Entropy - 3 * std1_Entropy
print(otric_dover_int_Entropy_1)
otric_dover_int_Entropy_2 = mean2_Entropy - 3 * std2_Entropy
print(otric_dover_int_Entropy_2)
otric_dover_int_Entropy_3 = mean3_Entropy - 3 * std3_Entropy
print(otric_dover_int_Entropy_3)
otric_dover_int_Entropy_4 = mean4_Entropy - 3 * std4_Entropy
print(otric_dover_int_Entropy_4)
otric_dover_int_Entropy_5 = mean5_Entropy - 3 * std5_Entropy
print(otric_dover_int_Entropy_5)
otric_dover_int_Entropy_6 = mean6_Entropy - 3 * std6_Entropy
print(otric_dover_int_Entropy_6)
otric_dover_int_Entropy_7 = mean7_Entropy - 3 * std7_Entropy
print(otric_dover_int_Entropy_7)
otric_dover_int_Entropy_8 = mean8_Entropy - 3 * std8_Entropy
print(otric_dover_int_Entropy_8)
otric_dover_int_Entropy_9 = mean9_Entropy - 3 * std9_Entropy
print(otric_dover_int_Entropy_9)
otric_dover_int_Entropy_10 = mean10_Entropy - 3 * std10_Entropy
print(otric_dover_int_Entropy_10)
otric_dover_int_Entropy_11 = mean11_Entropy - 3 * std11_Entropy
print(otric_dover_int_Entropy_11)
otric_dover_int_Entropy_12 = mean12_Entropy - 3 * std12_Entropy
print(otric_dover_int_Entropy_12)
otric_dover_int_Entropy_13 = mean13_Entropy - 3 * std13_Entropy
print(otric_dover_int_Entropy_13)
otric_dover_int_Entropy_14 = mean14_Entropy - 3 * std14_Entropy
print(otric_dover_int_Entropy_14)
otric_dover_int_Entropy_15 = mean15_Entropy - 3 * std15_Entropy
print(otric_dover_int_Entropy_15)
otric_dover_int_Entropy_16 = mean16_Entropy - 3 * std16_Entropy
print(otric_dover_int_Entropy_16)
otric_dover_int_Entropy_17 = mean17_Entropy - 3 * std17_Entropy
print(otric_dover_int_Entropy_17)
otric_dover_int_Entropy_18 = mean18_Entropy - 3 * std18_Entropy
print(otric_dover_int_Entropy_18)
otric_dover_int_Entropy_19 = mean19_Entropy - 3 * std19_Entropy
print(otric_dover_int_Entropy_19)
otric_dover_int_Entropy_20 = mean20_Entropy - 3 * std20_Entropy
print(otric_dover_int_Entropy_20)


# Положительный доверительный интервал для Entropy
poloj_dover_int_Entropy_1 = mean1_Entropy +  3 * std1_Entropy
print(poloj_dover_int_Entropy_1)
poloj_dover_int_Entropy_2 = mean2_Entropy +  3 * std2_Entropy
print(poloj_dover_int_Entropy_2)
poloj_dover_int_Entropy_3 = mean3_Entropy +  3 * std3_Entropy
print(poloj_dover_int_Entropy_3)
poloj_dover_int_Entropy_4 = mean4_Entropy +  3 * std4_Entropy
print(poloj_dover_int_Entropy_4)
poloj_dover_int_Entropy_5 = mean5_Entropy +  3 * std5_Entropy
print(poloj_dover_int_Entropy_5)
poloj_dover_int_Entropy_6 = mean6_Entropy +  3 * std6_Entropy
print(poloj_dover_int_Entropy_6)
poloj_dover_int_Entropy_7 = mean7_Entropy +  3 * std7_Entropy
print(poloj_dover_int_Entropy_7)
poloj_dover_int_Entropy_8 = mean8_Entropy +  3 * std8_Entropy
print(poloj_dover_int_Entropy_8)
poloj_dover_int_Entropy_9 = mean9_Entropy +  3 * std9_Entropy
print(poloj_dover_int_Entropy_9)
poloj_dover_int_Entropy_10 = mean10_Entropy +  3 * std10_Entropy
print(poloj_dover_int_Entropy_10)
poloj_dover_int_Entropy_11 = mean11_Entropy +  3 * std11_Entropy
print(poloj_dover_int_Entropy_11)
poloj_dover_int_Entropy_12 = mean12_Entropy +  3 * std12_Entropy
print(poloj_dover_int_Entropy_12)
poloj_dover_int_Entropy_13 = mean13_Entropy +  3 * std13_Entropy
print(poloj_dover_int_Entropy_13)
poloj_dover_int_Entropy_14 = mean14_Entropy +  3 * std14_Entropy
print(poloj_dover_int_Entropy_14)
poloj_dover_int_Entropy_15 = mean15_Entropy +  3 * std15_Entropy
print(poloj_dover_int_Entropy_15)
poloj_dover_int_Entropy_16 = mean16_Entropy +  3 * std16_Entropy
print(poloj_dover_int_Entropy_16)
poloj_dover_int_Entropy_17 = mean17_Entropy +  3 * std17_Entropy
print(poloj_dover_int_Entropy_17)
poloj_dover_int_Entropy_18 = mean18_Entropy +  3 * std18_Entropy
print(poloj_dover_int_Entropy_18)
poloj_dover_int_Entropy_19 = mean19_Entropy +  3 * std19_Entropy
print(poloj_dover_int_Entropy_19)
poloj_dover_int_Entropy_20 = mean20_Entropy +  3 * std20_Entropy
print(poloj_dover_int_Entropy_20)

# Всё о NumberOfRvaAndSizes
mean_NORAS = np.mean(df['NumberOfRvaAndSizes'])
print(mean_NORAS, "MEAN_NumberOfRvaAndSizes")
std_NORAS = np.std(df['NumberOfRvaAndSizes'])
print(std_NORAS, "STD_NumberOfRvaAndSizes")
otric_dover_int_NORAS = mean_NORAS - 3 * std_NORAS
print(otric_dover_int_NORAS, "Otric_NumberOfRvaAndSizes")
poloj_dover_int_NORAS = mean_NORAS +  3 * std_NORAS
print(poloj_dover_int_NORAS, "Poloj_NumberOfRvaAndSizes")





