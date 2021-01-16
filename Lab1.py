import numpy as np
import pandas as pd

# Создание датафейма из файла .csv
# Задание 1.1 https://www.kaggle.com/aman9d/phishing-data
df = pd.read_csv('combined_dataset.csv')
df

# Задание 1.2

import matplotlib.pyplot as plt

import seaborn as sns
sns.displot(df['ranking'])
plt.show()

sns.displot(df['activeDuration'])
plt.show()

sns.displot(df['urlLen'])
plt.show()

sns.displot(df['domainLen'])
plt.show()

sns.displot(df['nosOfSubdomain'])
plt.show()

# Области однородности для Ranking
ObbOdn1_Ranking = []
ObbOdn2_Ranking = []

for oblodn in df['ranking']:
    if oblodn <= 5.43:
        ObbOdn1_Ranking.append(oblodn)
    if oblodn > 5.43:
        ObbOdn2_Ranking.append(oblodn)

# Математическое ожидание для Ranking
mean1_Ranking = np.mean(ObbOdn1_Ranking)
print(mean1_Ranking, "MEAN1_Ranking")
mean2_Ranking = np.mean(ObbOdn2_Ranking)
print(mean2_Ranking, "MEAN2_Ranking")

# Среднеквадратическое отклонение для Ranking
std1_Ranking = np.std(ObbOdn1_Ranking)
print(std1_Ranking)
std2_Ranking = np.std(ObbOdn2_Ranking)
print(std2_Ranking)

# Отрицательный доверительный интервал для Ranking
otric_dover_int_Ranking_1 = mean1_Ranking - 3 * std1_Ranking
print(otric_dover_int_Ranking_1)
otric_dover_int_Ranking_2 = mean2_Ranking - 3 * std2_Ranking
print(otric_dover_int_Ranking_2)

# Положительный доверительный интервал для Ranking
poloj_dover_int_Ranking_1 = mean1_Ranking +  3 * std1_Ranking
print(poloj_dover_int_Ranking_1)
poloj_dover_int_Ranking_2 = mean2_Ranking +  3 * std2_Ranking
print(poloj_dover_int_Ranking_2)

# Области однородности для activeDuration
ObbOdn1_ActiveDuration = []
ObbOdn2_ActiveDuration = []
ObbOdn3_ActiveDuration = []
ObbOdn4_ActiveDuration = []
ObbOdn5_ActiveDuration = []
ObbOdn6_ActiveDuration = []
ObbOdn7_ActiveDuration = []
ObbOdn8_ActiveDuration = []
ObbOdn9_ActiveDuration = []
ObbOdn10_ActiveDuration = []

for oblodn in df['activeDuration']:
    if oblodn <= 2510:
        ObbOdn1_ActiveDuration.append(oblodn)
    if oblodn > 2510 and oblodn <= 3845:
        ObbOdn2_ActiveDuration.append(oblodn)
    if oblodn > 3845 and oblodn <= 4525:
        ObbOdn3_ActiveDuration.append(oblodn)
    if oblodn > 4525 and oblodn <= 5850:
        ObbOdn4_ActiveDuration.append(oblodn)
    if oblodn > 5850 and oblodn <= 7185:
        ObbOdn5_ActiveDuration.append(oblodn)
    if oblodn > 7185 and oblodn <= 7855:
        ObbOdn6_ActiveDuration.append(oblodn)
    if oblodn > 7855 and oblodn <= 8850:
        ObbOdn7_ActiveDuration.append(oblodn)
    if oblodn > 8850 and oblodn <= 10855:
        ObbOdn8_ActiveDuration.append(oblodn)
    if oblodn > 10855 and oblodn <= 11855:
        ObbOdn9_ActiveDuration.append(oblodn)
    if oblodn > 11855:
        ObbOdn10_ActiveDuration.append(oblodn)

# Математическое ожидание для ActiveDuration
mean1_ActiveDuration = np.mean(ObbOdn1_ActiveDuration)
print(mean1_ActiveDuration, "MEAN1_ActiveDuration")
mean2_ActiveDuration = np.mean(ObbOdn2_ActiveDuration)
print(mean2_ActiveDuration, "MEAN2_ActiveDuration")
mean3_ActiveDuration = np.mean(ObbOdn3_ActiveDuration)
print(mean3_ActiveDuration, "MEAN3_ActiveDuration")
mean4_ActiveDuration = np.mean(ObbOdn4_ActiveDuration)
print(mean4_ActiveDuration, "MEAN4_ActiveDuration")
mean5_ActiveDuration = np.mean(ObbOdn5_ActiveDuration)
print(mean5_ActiveDuration, "MEAN5_ActiveDuration")
mean6_ActiveDuration = np.mean(ObbOdn6_ActiveDuration)
print(mean6_ActiveDuration, "MEAN6_ActiveDuration")
mean7_ActiveDuration = np.mean(ObbOdn7_ActiveDuration)
print(mean7_ActiveDuration, "MEAN7_ActiveDuration")
mean8_ActiveDuration = np.mean(ObbOdn8_ActiveDuration)
print(mean8_ActiveDuration, "MEAN8_ActiveDuration")
mean9_ActiveDuration = np.mean(ObbOdn9_ActiveDuration)
print(mean9_ActiveDuration, "MEAN9_ActiveDuration")
mean10_ActiveDuration = np.mean(ObbOdn10_ActiveDuration)
print(mean10_ActiveDuration, "MEAN10_ActiveDuration")

# Среднеквадратическое отклонение для ActiveDuration
std1_ActiveDuration = np.std(ObbOdn1_ActiveDuration)
print(std1_ActiveDuration)
std2_ActiveDuration = np.std(ObbOdn2_ActiveDuration)
print(std2_ActiveDuration)
std3_ActiveDuration = np.std(ObbOdn3_ActiveDuration)
print(std3_ActiveDuration)
std4_ActiveDuration = np.std(ObbOdn4_ActiveDuration)
print(std4_ActiveDuration)
std5_ActiveDuration = np.std(ObbOdn5_ActiveDuration)
print(std5_ActiveDuration)
std6_ActiveDuration = np.std(ObbOdn6_ActiveDuration)
print(std6_ActiveDuration)
std7_ActiveDuration = np.std(ObbOdn7_ActiveDuration)
print(std7_ActiveDuration)
std8_ActiveDuration = np.std(ObbOdn8_ActiveDuration)
print(std8_ActiveDuration)
std9_ActiveDuration = np.std(ObbOdn9_ActiveDuration)
print(std9_ActiveDuration)
std10_ActiveDuration = np.std(ObbOdn10_ActiveDuration)
print(std10_ActiveDuration)

# Отрицательный доверительный интервал для ActiveDuration
otric_dover_int_ActiveDuration_1 = mean1_ActiveDuration - 3 * std1_ActiveDuration
print(otric_dover_int_ActiveDuration_1)
otric_dover_int_ActiveDuration_2 = mean2_ActiveDuration - 3 * std2_ActiveDuration
print(otric_dover_int_ActiveDuration_2)
otric_dover_int_ActiveDuration_3 = mean3_ActiveDuration - 3 * std3_ActiveDuration
print(otric_dover_int_ActiveDuration_3)
otric_dover_int_ActiveDuration_4 = mean4_ActiveDuration - 3 * std4_ActiveDuration
print(otric_dover_int_ActiveDuration_4)
otric_dover_int_ActiveDuration_5 = mean5_ActiveDuration - 3 * std5_ActiveDuration
print(otric_dover_int_ActiveDuration_5)
otric_dover_int_ActiveDuration_6 = mean6_ActiveDuration - 3 * std6_ActiveDuration
print(otric_dover_int_ActiveDuration_6)
otric_dover_int_ActiveDuration_7 = mean7_ActiveDuration - 3 * std7_ActiveDuration
print(otric_dover_int_ActiveDuration_7)
otric_dover_int_ActiveDuration_8 = mean8_ActiveDuration - 3 * std8_ActiveDuration
print(otric_dover_int_ActiveDuration_8)
otric_dover_int_ActiveDuration_9 = mean9_ActiveDuration - 3 * std9_ActiveDuration
print(otric_dover_int_ActiveDuration_9)
otric_dover_int_ActiveDuration_10 = mean10_ActiveDuration - 3 * std10_ActiveDuration
print(otric_dover_int_ActiveDuration_10)

# Положительный доверительный интервал для ActiveDuration
poloj_dover_int_ActiveDuration_1 = mean1_ActiveDuration +  3 * std1_ActiveDuration
print(poloj_dover_int_ActiveDuration_1)
poloj_dover_int_ActiveDuration_2 = mean2_ActiveDuration +  3 * std2_ActiveDuration
print(poloj_dover_int_ActiveDuration_2)
poloj_dover_int_ActiveDuration_3 = mean3_ActiveDuration +  3 * std3_ActiveDuration
print(poloj_dover_int_ActiveDuration_3)
poloj_dover_int_ActiveDuration_4 = mean3_ActiveDuration +  3 * std4_ActiveDuration
print(poloj_dover_int_ActiveDuration_4)
poloj_dover_int_ActiveDuration_5 = mean3_ActiveDuration +  3 * std5_ActiveDuration
print(poloj_dover_int_ActiveDuration_5)
poloj_dover_int_ActiveDuration_6 = mean3_ActiveDuration +  3 * std6_ActiveDuration
print(poloj_dover_int_ActiveDuration_6)
poloj_dover_int_ActiveDuration_7 = mean3_ActiveDuration +  3 * std7_ActiveDuration
print(poloj_dover_int_ActiveDuration_7)
poloj_dover_int_ActiveDuration_8 = mean3_ActiveDuration +  3 * std8_ActiveDuration
print(poloj_dover_int_ActiveDuration_8)
poloj_dover_int_ActiveDuration_9 = mean3_ActiveDuration +  3 * std9_ActiveDuration
print(poloj_dover_int_ActiveDuration_9)
poloj_dover_int_ActiveDuration_10 = mean3_ActiveDuration +  3 * std10_ActiveDuration
print(poloj_dover_int_ActiveDuration_10)

# Области однородности для urlLen
ObbOdn1_UrlLen = []
ObbOdn2_UrlLen = []
ObbOdn3_UrlLen = []
ObbOdn4_UrlLen = []
ObbOdn5_UrlLen = []
ObbOdn6_UrlLen = []
ObbOdn7_UrlLen = []
ObbOdn8_UrlLen = []
ObbOdn9_UrlLen = []
ObbOdn10_UrlLen = []
ObbOdn11_UrlLen = []
ObbOdn12_UrlLen = []
ObbOdn13_UrlLen = []
ObbOdn14_UrlLen = []
ObbOdn15_UrlLen = []
ObbOdn16_UrlLen = []
ObbOdn17_UrlLen = []
ObbOdn18_UrlLen = []
ObbOdn19_UrlLen = []
ObbOdn20_UrlLen = []
ObbOdn21_UrlLen = []
ObbOdn22_UrlLen = []
ObbOdn23_UrlLen = []
ObbOdn24_UrlLen = []
ObbOdn25_UrlLen = []
ObbOdn26_UrlLen = []
ObbOdn27_UrlLen = []
ObbOdn28_UrlLen = []
ObbOdn29_UrlLen = []
ObbOdn30_UrlLen = []
ObbOdn31_UrlLen = []
ObbOdn32_UrlLen = []
ObbOdn33_UrlLen = []
ObbOdn34_UrlLen = []
ObbOdn35_UrlLen = []
ObbOdn36_UrlLen = []
ObbOdn37_UrlLen = []
ObbOdn38_UrlLen = []
ObbOdn39_UrlLen = []
ObbOdn40_UrlLen = []
ObbOdn41_UrlLen = []
ObbOdn42_UrlLen = []
ObbOdn43_UrlLen = []
ObbOdn44_UrlLen = []
ObbOdn45_UrlLen = []
ObbOdn46_UrlLen = []
ObbOdn47_UrlLen = []
ObbOdn48_UrlLen = []
ObbOdn49_UrlLen = []
ObbOdn50_UrlLen = []
ObbOdn51_UrlLen = []
ObbOdn52_UrlLen = []
ObbOdn53_UrlLen = []
ObbOdn54_UrlLen = []

for oblodn in df['urlLen']:
    if oblodn <= 28.51:
        ObbOdn1_UrlLen.append(oblodn)
    if oblodn > 28.51 and oblodn <= 44.88:
        ObbOdn2_UrlLen.append(oblodn)
    if oblodn > 44.88 and oblodn <= 51.055:
        ObbOdn3_UrlLen.append(oblodn)
    if oblodn > 51.055 and oblodn <= 63.41:
        ObbOdn4_UrlLen.append(oblodn)
    if oblodn > 63.41 and oblodn <= 69.56:
        ObbOdn5_UrlLen.append(oblodn)
    if oblodn > 69.56 and oblodn <= 73.65:
        ObbOdn6_UrlLen.append(oblodn)
    if oblodn > 73.65 and oblodn <= 77.785:
        ObbOdn7_UrlLen.append(oblodn)
    if oblodn > 77.785 and oblodn <= 81.865:
        ObbOdn8_UrlLen.append(oblodn)
    if oblodn > 81.865 and oblodn <= 88.035:
        ObbOdn9_UrlLen.append(oblodn)
    if oblodn > 88.035 and oblodn <= 92.145:
        ObbOdn10_UrlLen.append(oblodn)
    if oblodn > 92.145 and oblodn <= 100.355:
        ObbOdn11_UrlLen.append(oblodn)
    if oblodn > 100.355 and oblodn <= 104.49:
        ObbOdn12_UrlLen.append(oblodn)
    if oblodn > 104.49 and oblodn <= 110.6:
        ObbOdn13_UrlLen.append(oblodn)
    if oblodn > 110.6 and oblodn <= 116.8:
        ObbOdn14_UrlLen.append(oblodn)
    if oblodn > 116.8 and oblodn <= 121.855:
        ObbOdn15_UrlLen.append(oblodn)
    if oblodn > 121.855 and oblodn <= 129.09:
        ObbOdn16_UrlLen.append(oblodn)
    if oblodn > 129.09 and oblodn <= 139.38:
        ObbOdn17_UrlLen.append(oblodn)
    if oblodn > 139.38 and oblodn <= 143.47:
        ObbOdn18_UrlLen.append(oblodn)
    if oblodn > 143.47 and oblodn <= 149.625:
        ObbOdn19_UrlLen.append(oblodn)
    if oblodn > 149.625 and oblodn <= 153.725:
        ObbOdn20_UrlLen.append(oblodn)
    if oblodn > 153.725 and oblodn <= 161.97:
        ObbOdn21_UrlLen.append(oblodn)
    if oblodn > 161.97 and oblodn <= 168.095:
        ObbOdn22_UrlLen.append(oblodn)
    if oblodn > 168.095 and oblodn <= 178.36:
        ObbOdn23_UrlLen.append(oblodn)
    if oblodn > 178.36 and oblodn <= 186.58:
        ObbOdn24_UrlLen.append(oblodn)
    if oblodn > 186.58 and oblodn <= 200.975:
        ObbOdn25_UrlLen.append(oblodn)
    if oblodn > 200.975 and oblodn <= 205.075:
        ObbOdn26_UrlLen.append(oblodn)
    if oblodn > 205.075 and oblodn <= 213.275:
        ObbOdn27_UrlLen.append(oblodn)
    if oblodn > 213.275 and oblodn <= 217.36:
        ObbOdn28_UrlLen.append(oblodn)
    if oblodn > 217.36 and oblodn <= 225.61:
        ObbOdn29_UrlLen.append(oblodn)
    if oblodn > 225.61 and oblodn <= 239.94:
        ObbOdn30_UrlLen.append(oblodn)
    if oblodn > 239.94 and oblodn <= 246.1:
        ObbOdn31_UrlLen.append(oblodn)
    if oblodn > 246.1 and oblodn <= 250.25:
        ObbOdn32_UrlLen.append(oblodn)
    if oblodn > 250.25 and oblodn <= 256.42:
        ObbOdn33_UrlLen.append(oblodn)
    if oblodn > 256.42 and oblodn <= 260.51:
        ObbOdn34_UrlLen.append(oblodn)
    if oblodn > 260.51 and oblodn <= 266.61:
        ObbOdn35_UrlLen.append(oblodn)
    if oblodn > 266.61 and oblodn <= 270.785:
        ObbOdn36_UrlLen.append(oblodn)
    if oblodn > 270.785 and oblodn <= 274.85:
        ObbOdn37_UrlLen.append(oblodn)
    if oblodn > 274.85 and oblodn <= 280.965:
        ObbOdn38_UrlLen.append(oblodn)
    if oblodn > 280.965 and oblodn <= 285.135:
        ObbOdn39_UrlLen.append(oblodn)
    if oblodn > 285.135 and oblodn <= 289.165:
        ObbOdn40_UrlLen.append(oblodn)
    if oblodn > 289.165 and oblodn <= 301.405:
        ObbOdn41_UrlLen.append(oblodn)
    if oblodn > 301.405 and oblodn <= 305.645:
        ObbOdn42_UrlLen.append(oblodn)
    if oblodn > 305.645 and oblodn <= 315.87:
        ObbOdn43_UrlLen.append(oblodn)
    if oblodn > 315.87 and oblodn <= 320.075:
        ObbOdn44_UrlLen.append(oblodn)
    if oblodn > 320.075 and oblodn <= 324.105:
        ObbOdn45_UrlLen.append(oblodn)
    if oblodn > 324.105 and oblodn <= 328.24:
        ObbOdn46_UrlLen.append(oblodn)
    if oblodn > 328.24 and oblodn <= 334.425:
        ObbOdn47_UrlLen.append(oblodn)
    if oblodn > 334.425 and oblodn <= 340.585:
        ObbOdn48_UrlLen.append(oblodn)
    if oblodn > 340.585 and oblodn <= 344.65:
        ObbOdn49_UrlLen.append(oblodn)
    if oblodn > 344.65 and oblodn <= 352.07:
        ObbOdn50_UrlLen.append(oblodn)
    if oblodn > 352.07 and oblodn <= 359.07:
        ObbOdn51_UrlLen.append(oblodn)
    if oblodn > 359.07 and oblodn <= 367.175:
        ObbOdn52_UrlLen.append(oblodn)
    if oblodn > 367.175 and oblodn <= 372.58:
        ObbOdn53_UrlLen.append(oblodn)
    if oblodn > 372.58:
        ObbOdn54_UrlLen.append(oblodn)

# Математическое ожидание для UrlLen
mean1_UrlLen = np.mean(ObbOdn1_UrlLen)
print(mean1_UrlLen, "MEAN1_UrlLen")
mean2_UrlLen = np.mean(ObbOdn2_UrlLen)
print(mean2_UrlLen, "MEAN2_UrlLen")
mean3_UrlLen = np.mean(ObbOdn3_UrlLen)
print(mean3_UrlLen, "MEAN3_UrlLen")
mean4_UrlLen = np.mean(ObbOdn4_UrlLen)
print(mean4_UrlLen, "MEAN4_UrlLen")
mean5_UrlLen = np.mean(ObbOdn5_UrlLen)
print(mean5_UrlLen, "MEAN5_UrlLen")
mean6_UrlLen = np.mean(ObbOdn6_UrlLen)
print(mean6_UrlLen, "MEAN6_UrlLen")
mean7_UrlLen = np.mean(ObbOdn7_UrlLen)
print(mean7_UrlLen, "MEAN7_UrlLen")
mean8_UrlLen = np.mean(ObbOdn8_UrlLen)
print(mean8_UrlLen, "MEAN8_UrlLen")
mean9_UrlLen = np.mean(ObbOdn9_UrlLen)
print(mean9_UrlLen, "MEAN9_UrlLen")
mean10_UrlLen = np.mean(ObbOdn10_UrlLen)
print(mean10_UrlLen, "MEAN10_UrlLen")
mean11_UrlLen = np.mean(ObbOdn11_UrlLen)
print(mean11_UrlLen, "MEAN11_UrlLen")
mean12_UrlLen = np.mean(ObbOdn12_UrlLen)
print(mean12_UrlLen, "MEAN12_UrlLen")
mean13_UrlLen = np.mean(ObbOdn13_UrlLen)
print(mean13_UrlLen, "MEAN13_UrlLen")
mean14_UrlLen = np.mean(ObbOdn14_UrlLen)
print(mean14_UrlLen, "MEAN14_UrlLen")
mean15_UrlLen = np.mean(ObbOdn15_UrlLen)
print(mean15_UrlLen, "MEAN15_UrlLen")
mean16_UrlLen = np.mean(ObbOdn16_UrlLen)
print(mean16_UrlLen, "MEAN16_UrlLen")
mean17_UrlLen = np.mean(ObbOdn17_UrlLen)
print(mean17_UrlLen, "MEAN17_UrlLen")
mean18_UrlLen = np.mean(ObbOdn18_UrlLen)
print(mean18_UrlLen, "MEAN18_UrlLen")
mean19_UrlLen = np.mean(ObbOdn19_UrlLen)
print(mean19_UrlLen, "MEAN19_UrlLen")
mean20_UrlLen = np.mean(ObbOdn20_UrlLen)
print(mean20_UrlLen, "MEAN20_UrlLen")
mean21_UrlLen = np.mean(ObbOdn21_UrlLen)
print(mean21_UrlLen, "MEAN21_UrlLen")
mean22_UrlLen = np.mean(ObbOdn22_UrlLen)
print(mean22_UrlLen, "MEAN22_UrlLen")
mean23_UrlLen = np.mean(ObbOdn23_UrlLen)
print(mean23_UrlLen, "MEAN23_UrlLen")
mean24_UrlLen = np.mean(ObbOdn24_UrlLen)
print(mean24_UrlLen, "MEAN24_UrlLen")
mean25_UrlLen = np.mean(ObbOdn25_UrlLen)
print(mean25_UrlLen, "MEAN25_UrlLen")
mean26_UrlLen = np.mean(ObbOdn26_UrlLen)
print(mean26_UrlLen, "MEAN26_UrlLen")
mean27_UrlLen = np.mean(ObbOdn27_UrlLen)
print(mean27_UrlLen, "MEAN27_UrlLen")
mean28_UrlLen = np.mean(ObbOdn28_UrlLen)
print(mean28_UrlLen, "MEAN28_UrlLen")
mean29_UrlLen = np.mean(ObbOdn29_UrlLen)
print(mean29_UrlLen, "MEAN29_UrlLen")
mean30_UrlLen = np.mean(ObbOdn30_UrlLen)
print(mean30_UrlLen, "MEAN30_UrlLen")
mean31_UrlLen = np.mean(ObbOdn31_UrlLen)
print(mean31_UrlLen, "MEAN31_UrlLen")
mean32_UrlLen = np.mean(ObbOdn32_UrlLen)
print(mean32_UrlLen, "MEAN32_UrlLen")
mean33_UrlLen = np.mean(ObbOdn33_UrlLen)
print(mean33_UrlLen, "MEAN33_UrlLen")
mean34_UrlLen = np.mean(ObbOdn34_UrlLen)
print(mean34_UrlLen, "MEAN34_UrlLen")
mean35_UrlLen = np.mean(ObbOdn35_UrlLen)
print(mean35_UrlLen, "MEAN35_UrlLen")
mean36_UrlLen = np.mean(ObbOdn36_UrlLen)
print(mean36_UrlLen, "MEAN36_UrlLen")
mean37_UrlLen = np.mean(ObbOdn37_UrlLen)
print(mean37_UrlLen, "MEAN37_UrlLen")
mean38_UrlLen = np.mean(ObbOdn38_UrlLen)
print(mean38_UrlLen, "MEAN38_UrlLen")
mean39_UrlLen = np.mean(ObbOdn39_UrlLen)
print(mean39_UrlLen, "MEAN39_UrlLen")
mean40_UrlLen = np.mean(ObbOdn40_UrlLen)
print(mean40_UrlLen, "MEAN40_UrlLen")
mean41_UrlLen = np.mean(ObbOdn41_UrlLen)
print(mean41_UrlLen, "MEAN41_UrlLen")
mean42_UrlLen = np.mean(ObbOdn42_UrlLen)
print(mean42_UrlLen, "MEAN42_UrlLen")
mean43_UrlLen = np.mean(ObbOdn43_UrlLen)
print(mean43_UrlLen, "MEAN43_UrlLen")
mean44_UrlLen = np.mean(ObbOdn44_UrlLen)
print(mean44_UrlLen, "MEAN44_UrlLen")
mean45_UrlLen = np.mean(ObbOdn45_UrlLen)
print(mean45_UrlLen, "MEAN45_UrlLen")
mean46_UrlLen = np.mean(ObbOdn46_UrlLen)
print(mean46_UrlLen, "MEAN46_UrlLen")
mean47_UrlLen = np.mean(ObbOdn47_UrlLen)
print(mean47_UrlLen, "MEAN47_UrlLen")
mean48_UrlLen = np.mean(ObbOdn48_UrlLen)
print(mean48_UrlLen, "MEAN48_UrlLen")
mean49_UrlLen = np.mean(ObbOdn49_UrlLen)
print(mean49_UrlLen, "MEAN49_UrlLen")
mean50_UrlLen = np.mean(ObbOdn50_UrlLen)
print(mean50_UrlLen, "MEAN50_UrlLen")
mean51_UrlLen = np.mean(ObbOdn51_UrlLen)
print(mean51_UrlLen, "MEAN51_UrlLen")
mean52_UrlLen = np.mean(ObbOdn52_UrlLen)
print(mean52_UrlLen, "MEAN52_UrlLen")
mean53_UrlLen = np.mean(ObbOdn53_UrlLen)
print(mean53_UrlLen, "MEAN53_UrlLen")
mean54_UrlLen = np.mean(ObbOdn54_UrlLen)
print(mean54_UrlLen, "MEAN54_UrlLen")

# Среднеквадратическое отклонение для UrlLen
std1_UrlLen = np.std(ObbOdn1_UrlLen)
print(std1_UrlLen)
std2_UrlLen = np.std(ObbOdn2_UrlLen)
print(std2_UrlLen)
std3_UrlLen = np.std(ObbOdn3_UrlLen)
print(std3_UrlLen)
std4_UrlLen = np.std(ObbOdn4_UrlLen)
print(std4_UrlLen)
std5_UrlLen = np.std(ObbOdn5_UrlLen)
print(std5_UrlLen)
std6_UrlLen = np.std(ObbOdn6_UrlLen)
print(std6_UrlLen)
std7_UrlLen = np.std(ObbOdn7_UrlLen)
print(std7_UrlLen)
std8_UrlLen = np.std(ObbOdn8_UrlLen)
print(std8_UrlLen)
std9_UrlLen = np.std(ObbOdn9_UrlLen)
print(std9_UrlLen)
std10_UrlLen = np.std(ObbOdn10_UrlLen)
print(std10_UrlLen)
std11_UrlLen = np.std(ObbOdn11_UrlLen)
print(std11_UrlLen)
std12_UrlLen = np.std(ObbOdn12_UrlLen)
print(std12_UrlLen)
std13_UrlLen = np.std(ObbOdn13_UrlLen)
print(std13_UrlLen)
std14_UrlLen = np.std(ObbOdn14_UrlLen)
print(std14_UrlLen)
std15_UrlLen = np.std(ObbOdn15_UrlLen)
print(std15_UrlLen)
std16_UrlLen = np.std(ObbOdn16_UrlLen)
print(std16_UrlLen)
std17_UrlLen = np.std(ObbOdn17_UrlLen)
print(std17_UrlLen)
std18_UrlLen = np.std(ObbOdn18_UrlLen)
print(std18_UrlLen)
std19_UrlLen = np.std(ObbOdn19_UrlLen)
print(std19_UrlLen)
std20_UrlLen = np.std(ObbOdn20_UrlLen)
print(std20_UrlLen)
std21_UrlLen = np.std(ObbOdn21_UrlLen)
print(std21_UrlLen)
std22_UrlLen = np.std(ObbOdn22_UrlLen)
print(std22_UrlLen)
std23_UrlLen = np.std(ObbOdn23_UrlLen)
print(std23_UrlLen)
std24_UrlLen = np.std(ObbOdn24_UrlLen)
print(std24_UrlLen)
std25_UrlLen = np.std(ObbOdn25_UrlLen)
print(std25_UrlLen)
std26_UrlLen = np.std(ObbOdn26_UrlLen)
print(std26_UrlLen)
std27_UrlLen = np.std(ObbOdn27_UrlLen)
print(std27_UrlLen)
std28_UrlLen = np.std(ObbOdn28_UrlLen)
print(std28_UrlLen)
std29_UrlLen = np.std(ObbOdn29_UrlLen)
print(std29_UrlLen)
std30_UrlLen = np.std(ObbOdn30_UrlLen)
print(std30_UrlLen)
std31_UrlLen = np.std(ObbOdn31_UrlLen)
print(std31_UrlLen)
std32_UrlLen = np.std(ObbOdn32_UrlLen)
print(std32_UrlLen)
std33_UrlLen = np.std(ObbOdn33_UrlLen)
print(std33_UrlLen)
std34_UrlLen = np.std(ObbOdn34_UrlLen)
print(std34_UrlLen)
std35_UrlLen = np.std(ObbOdn35_UrlLen)
print(std35_UrlLen)
std36_UrlLen = np.std(ObbOdn36_UrlLen)
print(std36_UrlLen)
std37_UrlLen = np.std(ObbOdn37_UrlLen)
print(std37_UrlLen)
std38_UrlLen = np.std(ObbOdn38_UrlLen)
print(std38_UrlLen)
std39_UrlLen = np.std(ObbOdn39_UrlLen)
print(std39_UrlLen)
std40_UrlLen = np.std(ObbOdn40_UrlLen)
print(std40_UrlLen)
std41_UrlLen = np.std(ObbOdn41_UrlLen)
print(std41_UrlLen)
std42_UrlLen = np.std(ObbOdn42_UrlLen)
print(std42_UrlLen)
std43_UrlLen = np.std(ObbOdn43_UrlLen)
print(std43_UrlLen)
std44_UrlLen = np.std(ObbOdn44_UrlLen)
print(std44_UrlLen)
std45_UrlLen = np.std(ObbOdn45_UrlLen)
print(std45_UrlLen)
std46_UrlLen = np.std(ObbOdn46_UrlLen)
print(std46_UrlLen)
std47_UrlLen = np.std(ObbOdn47_UrlLen)
print(std47_UrlLen)
std48_UrlLen = np.std(ObbOdn48_UrlLen)
print(std48_UrlLen)
std49_UrlLen = np.std(ObbOdn49_UrlLen)
print(std49_UrlLen)
std50_UrlLen = np.std(ObbOdn50_UrlLen)
print(std50_UrlLen)
std51_UrlLen = np.std(ObbOdn51_UrlLen)
print(std51_UrlLen)
std52_UrlLen = np.std(ObbOdn52_UrlLen)
print(std52_UrlLen)
std53_UrlLen = np.std(ObbOdn53_UrlLen)
print(std53_UrlLen)
std54_UrlLen = np.std(ObbOdn54_UrlLen)
print(std54_UrlLen)

# Отрицательный доверительный интервал для UrlLen
otric_dover_int_UrlLen_1 = mean1_UrlLen - 3 * std1_UrlLen
print(otric_dover_int_UrlLen_1)
otric_dover_int_UrlLen_2 = mean2_UrlLen - 3 * std2_UrlLen
print(otric_dover_int_UrlLen_2)
otric_dover_int_UrlLen_3 = mean3_UrlLen - 3 * std3_UrlLen
print(otric_dover_int_UrlLen_3)
otric_dover_int_UrlLen_4 = mean4_UrlLen - 3 * std4_UrlLen
print(otric_dover_int_UrlLen_4)
otric_dover_int_UrlLen_5 = mean5_UrlLen - 3 * std5_UrlLen
print(otric_dover_int_UrlLen_5)
otric_dover_int_UrlLen_6 = mean6_UrlLen - 3 * std6_UrlLen
print(otric_dover_int_UrlLen_6)
otric_dover_int_UrlLen_7 = mean7_UrlLen - 3 * std7_UrlLen
print(otric_dover_int_UrlLen_7)
otric_dover_int_UrlLen_8 = mean8_UrlLen - 3 * std8_UrlLen
print(otric_dover_int_UrlLen_8)
otric_dover_int_UrlLen_9 = mean9_UrlLen - 3 * std9_UrlLen
print(otric_dover_int_UrlLen_9)
otric_dover_int_UrlLen_10 = mean10_UrlLen - 3 * std10_UrlLen
print(otric_dover_int_UrlLen_10)
otric_dover_int_UrlLen_11 = mean11_UrlLen - 3 * std11_UrlLen
print(otric_dover_int_UrlLen_11)
otric_dover_int_UrlLen_12 = mean12_UrlLen - 3 * std12_UrlLen
print(otric_dover_int_UrlLen_12)
otric_dover_int_UrlLen_13 = mean13_UrlLen - 3 * std13_UrlLen
print(otric_dover_int_UrlLen_13)
otric_dover_int_UrlLen_14 = mean14_UrlLen - 3 * std14_UrlLen
print(otric_dover_int_UrlLen_14)
otric_dover_int_UrlLen_15 = mean15_UrlLen - 3 * std15_UrlLen
print(otric_dover_int_UrlLen_15)
otric_dover_int_UrlLen_16 = mean16_UrlLen - 3 * std16_UrlLen
print(otric_dover_int_UrlLen_16)
otric_dover_int_UrlLen_17 = mean17_UrlLen - 3 * std17_UrlLen
print(otric_dover_int_UrlLen_17)
otric_dover_int_UrlLen_18 = mean18_UrlLen - 3 * std18_UrlLen
print(otric_dover_int_UrlLen_18)
otric_dover_int_UrlLen_19 = mean19_UrlLen - 3 * std19_UrlLen
print(otric_dover_int_UrlLen_19)
otric_dover_int_UrlLen_20 = mean20_UrlLen - 3 * std20_UrlLen
print(otric_dover_int_UrlLen_20)
otric_dover_int_UrlLen_21 = mean21_UrlLen - 3 * std21_UrlLen
print(otric_dover_int_UrlLen_21)
otric_dover_int_UrlLen_22 = mean22_UrlLen - 3 * std22_UrlLen
print(otric_dover_int_UrlLen_22)
otric_dover_int_UrlLen_23 = mean23_UrlLen - 3 * std23_UrlLen
print(otric_dover_int_UrlLen_23)
otric_dover_int_UrlLen_24 = mean24_UrlLen - 3 * std24_UrlLen
print(otric_dover_int_UrlLen_24)
otric_dover_int_UrlLen_25 = mean25_UrlLen - 3 * std25_UrlLen
print(otric_dover_int_UrlLen_25)
otric_dover_int_UrlLen_26 = mean26_UrlLen - 3 * std26_UrlLen
print(otric_dover_int_UrlLen_26)
otric_dover_int_UrlLen_27 = mean27_UrlLen - 3 * std27_UrlLen
print(otric_dover_int_UrlLen_27)
otric_dover_int_UrlLen_28 = mean28_UrlLen - 3 * std28_UrlLen
print(otric_dover_int_UrlLen_28)
otric_dover_int_UrlLen_29 = mean29_UrlLen - 3 * std29_UrlLen
print(otric_dover_int_UrlLen_29)
otric_dover_int_UrlLen_30 = mean30_UrlLen - 3 * std30_UrlLen
print(otric_dover_int_UrlLen_30)
otric_dover_int_UrlLen_31 = mean31_UrlLen - 3 * std31_UrlLen
print(otric_dover_int_UrlLen_31)
otric_dover_int_UrlLen_32 = mean32_UrlLen - 3 * std32_UrlLen
print(otric_dover_int_UrlLen_32)
otric_dover_int_UrlLen_33 = mean33_UrlLen - 3 * std33_UrlLen
print(otric_dover_int_UrlLen_33)
otric_dover_int_UrlLen_34 = mean34_UrlLen - 3 * std34_UrlLen
print(otric_dover_int_UrlLen_34)
otric_dover_int_UrlLen_35 = mean35_UrlLen - 3 * std35_UrlLen
print(otric_dover_int_UrlLen_35)
otric_dover_int_UrlLen_36 = mean36_UrlLen - 3 * std36_UrlLen
print(otric_dover_int_UrlLen_36)
otric_dover_int_UrlLen_37 = mean37_UrlLen - 3 * std37_UrlLen
print(otric_dover_int_UrlLen_37)
otric_dover_int_UrlLen_38 = mean38_UrlLen - 3 * std38_UrlLen
print(otric_dover_int_UrlLen_38)
otric_dover_int_UrlLen_39 = mean39_UrlLen - 3 * std39_UrlLen
print(otric_dover_int_UrlLen_39)
otric_dover_int_UrlLen_40 = mean40_UrlLen - 3 * std40_UrlLen
print(otric_dover_int_UrlLen_40)
otric_dover_int_UrlLen_41 = mean41_UrlLen - 3 * std41_UrlLen
print(otric_dover_int_UrlLen_41)
otric_dover_int_UrlLen_42 = mean42_UrlLen - 3 * std42_UrlLen
print(otric_dover_int_UrlLen_42)
otric_dover_int_UrlLen_43 = mean43_UrlLen - 3 * std43_UrlLen
print(otric_dover_int_UrlLen_43)
otric_dover_int_UrlLen_44 = mean44_UrlLen - 3 * std44_UrlLen
print(otric_dover_int_UrlLen_44)
otric_dover_int_UrlLen_45 = mean45_UrlLen - 3 * std45_UrlLen
print(otric_dover_int_UrlLen_45)
otric_dover_int_UrlLen_46 = mean46_UrlLen - 3 * std46_UrlLen
print(otric_dover_int_UrlLen_46)
otric_dover_int_UrlLen_47 = mean47_UrlLen - 3 * std47_UrlLen
print(otric_dover_int_UrlLen_47)
otric_dover_int_UrlLen_48 = mean48_UrlLen - 3 * std48_UrlLen
print(otric_dover_int_UrlLen_48)
otric_dover_int_UrlLen_49 = mean49_UrlLen - 3 * std49_UrlLen
print(otric_dover_int_UrlLen_49)
otric_dover_int_UrlLen_50 = mean50_UrlLen - 3 * std50_UrlLen
print(otric_dover_int_UrlLen_50)
otric_dover_int_UrlLen_51 = mean51_UrlLen - 3 * std51_UrlLen
print(otric_dover_int_UrlLen_51)
otric_dover_int_UrlLen_52 = mean52_UrlLen - 3 * std52_UrlLen
print(otric_dover_int_UrlLen_52)
otric_dover_int_UrlLen_53 = mean53_UrlLen - 3 * std53_UrlLen
print(otric_dover_int_UrlLen_53)
otric_dover_int_UrlLen_54 = mean54_UrlLen - 3 * std54_UrlLen
print(otric_dover_int_UrlLen_54)

# Положительный доверительный интервал для UrlLen
poloj_dover_int_UrlLen_1 = mean1_UrlLen +  3 * std1_UrlLen
print(poloj_dover_int_UrlLen_1)
poloj_dover_int_UrlLen_2 = mean2_UrlLen +  3 * std2_UrlLen
print(poloj_dover_int_UrlLen_2)
poloj_dover_int_UrlLen_3 = mean3_UrlLen +  3 * std3_UrlLen
print(poloj_dover_int_UrlLen_3)
poloj_dover_int_UrlLen_4 = mean4_UrlLen +  3 * std4_UrlLen
print(poloj_dover_int_UrlLen_4)
poloj_dover_int_UrlLen_5 = mean5_UrlLen +  3 * std5_UrlLen
print(poloj_dover_int_UrlLen_5)
poloj_dover_int_UrlLen_6 = mean6_UrlLen +  3 * std6_UrlLen
print(poloj_dover_int_UrlLen_6)
poloj_dover_int_UrlLen_7 = mean7_UrlLen +  3 * std7_UrlLen
print(poloj_dover_int_UrlLen_7)
poloj_dover_int_UrlLen_8 = mean8_UrlLen +  3 * std8_UrlLen
print(poloj_dover_int_UrlLen_8)
poloj_dover_int_UrlLen_9 = mean9_UrlLen +  3 * std9_UrlLen
print(poloj_dover_int_UrlLen_9)
poloj_dover_int_UrlLen_10 = mean10_UrlLen +  3 * std10_UrlLen
print(poloj_dover_int_UrlLen_10)
poloj_dover_int_UrlLen_11 = mean11_UrlLen +  3 * std11_UrlLen
print(poloj_dover_int_UrlLen_11)
poloj_dover_int_UrlLen_12 = mean12_UrlLen +  3 * std12_UrlLen
print(poloj_dover_int_UrlLen_12)
poloj_dover_int_UrlLen_13 = mean13_UrlLen +  3 * std13_UrlLen
print(poloj_dover_int_UrlLen_13)
poloj_dover_int_UrlLen_14 = mean14_UrlLen +  3 * std14_UrlLen
print(poloj_dover_int_UrlLen_14)
poloj_dover_int_UrlLen_15 = mean15_UrlLen +  3 * std15_UrlLen
print(poloj_dover_int_UrlLen_15)
poloj_dover_int_UrlLen_16 = mean16_UrlLen +  3 * std16_UrlLen
print(poloj_dover_int_UrlLen_16)
poloj_dover_int_UrlLen_17 = mean17_UrlLen +  3 * std17_UrlLen
print(poloj_dover_int_UrlLen_17)
poloj_dover_int_UrlLen_18 = mean18_UrlLen +  3 * std18_UrlLen
print(poloj_dover_int_UrlLen_18)
poloj_dover_int_UrlLen_19 = mean19_UrlLen +  3 * std19_UrlLen
print(poloj_dover_int_UrlLen_19)
poloj_dover_int_UrlLen_20 = mean20_UrlLen +  3 * std20_UrlLen
print(poloj_dover_int_UrlLen_20)
poloj_dover_int_UrlLen_21 = mean21_UrlLen +  3 * std21_UrlLen
print(poloj_dover_int_UrlLen_21)
poloj_dover_int_UrlLen_22 = mean22_UrlLen +  3 * std22_UrlLen
print(poloj_dover_int_UrlLen_22)
poloj_dover_int_UrlLen_23 = mean23_UrlLen +  3 * std23_UrlLen
print(poloj_dover_int_UrlLen_23)
poloj_dover_int_UrlLen_24 = mean24_UrlLen +  3 * std24_UrlLen
print(poloj_dover_int_UrlLen_24)
poloj_dover_int_UrlLen_25 = mean25_UrlLen +  3 * std25_UrlLen
print(poloj_dover_int_UrlLen_25)
poloj_dover_int_UrlLen_26 = mean26_UrlLen +  3 * std26_UrlLen
print(poloj_dover_int_UrlLen_26)
poloj_dover_int_UrlLen_27 = mean27_UrlLen +  3 * std27_UrlLen
print(poloj_dover_int_UrlLen_27)
poloj_dover_int_UrlLen_28 = mean28_UrlLen +  3 * std28_UrlLen
print(poloj_dover_int_UrlLen_28)
poloj_dover_int_UrlLen_29 = mean29_UrlLen +  3 * std29_UrlLen
print(poloj_dover_int_UrlLen_29)
poloj_dover_int_UrlLen_30 = mean30_UrlLen +  3 * std30_UrlLen
print(poloj_dover_int_UrlLen_30)
poloj_dover_int_UrlLen_31 = mean31_UrlLen +  3 * std31_UrlLen
print(poloj_dover_int_UrlLen_31)
poloj_dover_int_UrlLen_32 = mean32_UrlLen +  3 * std32_UrlLen
print(poloj_dover_int_UrlLen_32)
poloj_dover_int_UrlLen_33 = mean33_UrlLen +  3 * std33_UrlLen
print(poloj_dover_int_UrlLen_33)
poloj_dover_int_UrlLen_34 = mean34_UrlLen +  3 * std34_UrlLen
print(poloj_dover_int_UrlLen_34)
poloj_dover_int_UrlLen_35 = mean35_UrlLen +  3 * std35_UrlLen
print(poloj_dover_int_UrlLen_35)
poloj_dover_int_UrlLen_36 = mean36_UrlLen +  3 * std36_UrlLen
print(poloj_dover_int_UrlLen_36)
poloj_dover_int_UrlLen_37 = mean37_UrlLen +  3 * std37_UrlLen
print(poloj_dover_int_UrlLen_37)
poloj_dover_int_UrlLen_38 = mean38_UrlLen +  3 * std38_UrlLen
print(poloj_dover_int_UrlLen_38)
poloj_dover_int_UrlLen_39 = mean39_UrlLen +  3 * std39_UrlLen
print(poloj_dover_int_UrlLen_39)
poloj_dover_int_UrlLen_40 = mean40_UrlLen +  3 * std40_UrlLen
print(poloj_dover_int_UrlLen_40)
poloj_dover_int_UrlLen_41 = mean41_UrlLen +  3 * std41_UrlLen
print(poloj_dover_int_UrlLen_41)
poloj_dover_int_UrlLen_42 = mean42_UrlLen +  3 * std42_UrlLen
print(poloj_dover_int_UrlLen_42)
poloj_dover_int_UrlLen_43 = mean43_UrlLen +  3 * std43_UrlLen
print(poloj_dover_int_UrlLen_43)
poloj_dover_int_UrlLen_44 = mean44_UrlLen +  3 * std44_UrlLen
print(poloj_dover_int_UrlLen_44)
poloj_dover_int_UrlLen_45 = mean45_UrlLen +  3 * std45_UrlLen
print(poloj_dover_int_UrlLen_45)
poloj_dover_int_UrlLen_46 = mean46_UrlLen +  3 * std46_UrlLen
print(poloj_dover_int_UrlLen_46)
poloj_dover_int_UrlLen_47 = mean47_UrlLen +  3 * std47_UrlLen
print(poloj_dover_int_UrlLen_47)
poloj_dover_int_UrlLen_48 = mean48_UrlLen +  3 * std48_UrlLen
print(poloj_dover_int_UrlLen_48)
poloj_dover_int_UrlLen_49 = mean49_UrlLen +  3 * std49_UrlLen
print(poloj_dover_int_UrlLen_49)
poloj_dover_int_UrlLen_50 = mean50_UrlLen +  3 * std50_UrlLen
print(poloj_dover_int_UrlLen_50)
poloj_dover_int_UrlLen_51 = mean51_UrlLen +  3 * std51_UrlLen
print(poloj_dover_int_UrlLen_51)
poloj_dover_int_UrlLen_52 = mean52_UrlLen +  3 * std52_UrlLen
print(poloj_dover_int_UrlLen_52)
poloj_dover_int_UrlLen_53 = mean53_UrlLen +  3 * std53_UrlLen
print(poloj_dover_int_UrlLen_53)
poloj_dover_int_UrlLen_54 = mean54_UrlLen +  3 * std54_UrlLen
print(poloj_dover_int_UrlLen_54)

# Области однородности для DomainLen
ObbOdn1_DomainLen = []
ObbOdn2_DomainLen = []
ObbOdn3_DomainLen = []
ObbOdn4_DomainLen = []
ObbOdn5_DomainLen = []
ObbOdn6_DomainLen = []
ObbOdn7_DomainLen = []
ObbOdn8_DomainLen = []
ObbOdn9_DomainLen = []
ObbOdn10_DomainLen = []
ObbOdn11_DomainLen = []

for oblodn in df['domainLen']:
    if oblodn <= 4.91:
        ObbOdn1_DomainLen.append(oblodn)
    if oblodn > 4.91 and oblodn <= 7.02:
        ObbOdn2_DomainLen.append(oblodn)
    if oblodn > 7.02 and oblodn <= 15.04:
        ObbOdn3_DomainLen.append(oblodn)
    if oblodn > 15.04 and oblodn <= 19.938:
        ObbOdn4_DomainLen.append(oblodn)
    if oblodn > 19.938 and oblodn <= 29:
        ObbOdn5_DomainLen.append(oblodn)
    if oblodn > 29 and oblodn <= 33.955:
        ObbOdn6_DomainLen.append(oblodn)
    if oblodn > 33.955 and oblodn <= 38.1:
        ObbOdn7_DomainLen.append(oblodn)
    if oblodn > 38.1 and oblodn <= 39.84:
        ObbOdn8_DomainLen.append(oblodn)
    if oblodn > 39.84 and oblodn <= 41.935:
        ObbOdn9_DomainLen.append(oblodn)
    if oblodn > 41.935 and oblodn <= 46.13:
        ObbOdn10_DomainLen.append(oblodn)
    if oblodn > 46.13:
        ObbOdn11_DomainLen.append(oblodn)

# Математическое ожидание для DomainLen
mean1_DomainLen = np.mean(ObbOdn1_DomainLen)
print(mean1_DomainLen, "MEAN1_DomainLen")
mean2_DomainLen = np.mean(ObbOdn2_DomainLen)
print(mean2_DomainLen, "MEAN2_DomainLen")
mean3_DomainLen = np.mean(ObbOdn3_DomainLen)
print(mean3_DomainLen, "MEAN3_DomainLen")
mean4_DomainLen = np.mean(ObbOdn4_DomainLen)
print(mean4_DomainLen, "MEAN4_DomainLen")
mean5_DomainLen = np.mean(ObbOdn5_DomainLen)
print(mean5_DomainLen, "MEAN5_DomainLen")
mean6_DomainLen = np.mean(ObbOdn6_DomainLen)
print(mean6_DomainLen, "MEAN6_DomainLen")
mean7_DomainLen = np.mean(ObbOdn7_DomainLen)
print(mean7_DomainLen, "MEAN7_DomainLen")
mean8_DomainLen = np.mean(ObbOdn8_DomainLen)
print(mean8_DomainLen, "MEAN8_DomainLen")
mean9_DomainLen = np.mean(ObbOdn9_DomainLen)
print(mean9_DomainLen, "MEAN9_DomainLen")
mean10_DomainLen = np.mean(ObbOdn10_DomainLen)
print(mean10_DomainLen, "MEAN10_DomainLen")
mean11_DomainLen = np.mean(ObbOdn11_DomainLen)
print(mean11_DomainLen, "MEAN11_DomainLen")

# Среднеквадратическое отклонение для DomainLen
std1_DomainLen = np.std(ObbOdn1_DomainLen)
print(std1_DomainLen)
std2_DomainLen = np.std(ObbOdn2_DomainLen)
print(std2_DomainLen)
std3_DomainLen = np.std(ObbOdn3_DomainLen)
print(std3_DomainLen)
std4_DomainLen = np.std(ObbOdn4_DomainLen)
print(std4_DomainLen)
std5_DomainLen = np.std(ObbOdn5_DomainLen)
print(std5_DomainLen)
std6_DomainLen = np.std(ObbOdn6_DomainLen)
print(std6_DomainLen)
std7_DomainLen = np.std(ObbOdn7_DomainLen)
print(std7_DomainLen)
std8_DomainLen = np.std(ObbOdn8_DomainLen)
print(std8_DomainLen)
std9_DomainLen = np.std(ObbOdn9_DomainLen)
print(std9_DomainLen)
std10_DomainLen = np.std(ObbOdn10_DomainLen)
print(std10_DomainLen)
std11_DomainLen = np.std(ObbOdn11_DomainLen)
print(std11_DomainLen)

# Отрицательный доверительный интервал для DomainLen
otric_dover_int_DomainLen_1 = mean1_DomainLen - 3 * std1_DomainLen
print(otric_dover_int_DomainLen_1)
otric_dover_int_DomainLen_2 = mean2_DomainLen - 3 * std2_DomainLen
print(otric_dover_int_DomainLen_2)
otric_dover_int_DomainLen_3 = mean3_DomainLen - 3 * std3_DomainLen
print(otric_dover_int_DomainLen_3)
otric_dover_int_DomainLen_4 = mean4_DomainLen - 3 * std4_DomainLen
print(otric_dover_int_DomainLen_4)
otric_dover_int_DomainLen_5 = mean5_DomainLen - 3 * std5_DomainLen
print(otric_dover_int_DomainLen_5)
otric_dover_int_DomainLen_6 = mean6_DomainLen - 3 * std6_DomainLen
print(otric_dover_int_DomainLen_6)
otric_dover_int_DomainLen_7 = mean7_DomainLen - 3 * std7_DomainLen
print(otric_dover_int_DomainLen_7)
otric_dover_int_DomainLen_8 = mean8_DomainLen - 3 * std8_DomainLen
print(otric_dover_int_DomainLen_8)
otric_dover_int_DomainLen_9 = mean9_DomainLen - 3 * std9_DomainLen
print(otric_dover_int_DomainLen_9)
otric_dover_int_DomainLen_10 = mean10_DomainLen - 3 * std10_DomainLen
print(otric_dover_int_DomainLen_10)
otric_dover_int_DomainLen_11 = mean11_DomainLen - 3 * std11_DomainLen
print(otric_dover_int_DomainLen_11)

# Положительный доверительный интервал для DomainLen
poloj_dover_int_DomainLen_1 = mean1_DomainLen +  3 * std1_DomainLen
print(poloj_dover_int_DomainLen_1)
poloj_dover_int_DomainLen_2 = mean2_DomainLen +  3 * std2_DomainLen
print(poloj_dover_int_DomainLen_2)
poloj_dover_int_DomainLen_3 = mean3_DomainLen +  3 * std3_DomainLen
print(poloj_dover_int_DomainLen_3)
poloj_dover_int_DomainLen_4 = mean4_DomainLen +  3 * std4_DomainLen
print(poloj_dover_int_DomainLen_4)
poloj_dover_int_DomainLen_5 = mean5_DomainLen +  3 * std5_DomainLen
print(poloj_dover_int_DomainLen_5)
poloj_dover_int_DomainLen_6 = mean6_DomainLen +  3 * std6_DomainLen
print(poloj_dover_int_DomainLen_6)
poloj_dover_int_DomainLen_7 = mean7_DomainLen +  3 * std7_DomainLen
print(poloj_dover_int_DomainLen_7)
poloj_dover_int_DomainLen_8 = mean8_DomainLen +  3 * std8_DomainLen
print(poloj_dover_int_DomainLen_8)
poloj_dover_int_DomainLen_9 = mean9_DomainLen +  3 * std9_DomainLen
print(poloj_dover_int_DomainLen_9)
poloj_dover_int_DomainLen_10 = mean10_DomainLen +  3 * std10_DomainLen
print(poloj_dover_int_DomainLen_10)
poloj_dover_int_DomainLen_11 = mean11_DomainLen +  3 * std11_DomainLen
print(poloj_dover_int_DomainLen_11)

# Области однородности для nosOfSubdomain
ObbOdn1_nosOfSubdomain = []
ObbOdn2_nosOfSubdomain = []
ObbOdn3_nosOfSubdomain = []
ObbOdn3_nosOfSubdomain = []
for oblodn in df['nosOfSubdomain']:
    if oblodn <= 10.385:
        ObbOdn1_nosOfSubdomain.append(oblodn)
    if oblodn > 10.385 and oblodn <= 16.03:
        ObbOdn2_nosOfSubdomain.append(oblodn)
    if oblodn > 1.301 and oblodn <= 9.559:
        ObbOdn2_nosOfSubdomain.append(oblodn)
    if oblodn > 9.559:
        ObbOdn3_nosOfSubdomain.append(oblodn)

# Математическое ожидание для nosOfSubdomain
mean1_nosOfSubdomain = np.mean(ObbOdn1_nosOfSubdomain)
print(mean1_nosOfSubdomain, "MEAN1_nosOfSubdomain")
mean2_nosOfSubdomain = np.mean(ObbOdn2_nosOfSubdomain)
print(mean2_nosOfSubdomain, "MEAN2_nosOfSubdomain")
mean3_nosOfSubdomain = np.mean(ObbOdn3_nosOfSubdomain)
print(mean3_nosOfSubdomain, "MEAN3_nosOfSubdomain")

# Среднеквадратическое отклонение для nosOfSubdomain
std1_nosOfSubdomain = np.std(ObbOdn1_nosOfSubdomain)
print(std1_nosOfSubdomain)
std2_nosOfSubdomain = np.std(ObbOdn2_nosOfSubdomain)
print(std2_nosOfSubdomain)
std3_nosOfSubdomain = np.std(ObbOdn3_nosOfSubdomain)
print(std3_nosOfSubdomain)

# Отрицательный доверительный интервал для nosOfSubdomain
otric_dover_int_nosOfSubdomain_1 = mean1_nosOfSubdomain - 3 * std1_nosOfSubdomain
print(otric_dover_int_nosOfSubdomain_1)
otric_dover_int_nosOfSubdomain_2 = mean2_nosOfSubdomain - 3 * std2_nosOfSubdomain
print(otric_dover_int_nosOfSubdomain_2)
otric_dover_int_nosOfSubdomain_3 = mean3_nosOfSubdomain - 3 * std3_nosOfSubdomain
print(otric_dover_int_nosOfSubdomain_3)

# Положительный доверительный интервал для nosOfSubdomain
poloj_dover_int_nosOfSubdomain_1 = mean1_nosOfSubdomain +  3 * std1_nosOfSubdomain
print(poloj_dover_int_nosOfSubdomain_1)
poloj_dover_int_nosOfSubdomain_2 = mean2_nosOfSubdomain +  3 * std2_nosOfSubdomain
print(poloj_dover_int_nosOfSubdomain_2)
poloj_dover_int_nosOfSubdomain_3 = mean3_nosOfSubdomain +  3 * std3_nosOfSubdomain
print(poloj_dover_int_nosOfSubdomain_3)

plt.figure()
df['domain'].value_counts().plot.bar()
plt.show()

plt.figure()
df['isIp'].value_counts().plot.bar()
plt.show()

plt.figure()
df['valid'].value_counts().plot.bar()
plt.show()

plt.figure()
df['is@'].value_counts().plot.bar()
plt.show()

plt.figure()
df['isredirect'].value_counts().plot.bar()
plt.show()

plt.figure()
df['haveDash'].value_counts().plot.bar()
plt.show()








