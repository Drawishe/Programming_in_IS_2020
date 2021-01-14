import pandas as pd
import numpy as np
df = pd.read_csv('combined_dataset.csv')
df = df.drop(columns='domain')
df

df.shape

df = df.dropna()
df.shape

from sklearn.model_selection import train_test_split

points_train, points_test, labels_train, labels_test = train_test_split(df.iloc[:, :-1], df['label'], test_size=0.25, random_state=0)
print(points_train, points_test)

print(points_train.shape, points_test.shape)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(criterion='entropy', max_depth=6)
dt.fit(points_train, labels_train)

import matplotlib.pyplot as plt
from sklearn import tree
plt.figure()
tree.plot_tree(dt)
plt.show()

prediction = dt.predict(points_test)
print(points_test.assign(predict=prediction))

print(format(dt.score(points_test, labels_test)))

# Математическое ожидание и среднеквадратическое отклонение для ranking
mean_ranking = np.mean(df['ranking'])
print(mean_ranking)
std_ranking = np.std(df['ranking'])
print(std_ranking)

# Отрицательный и положительный доверительные интервалы для ranking
otric_dover_int_ranking = mean_ranking - 3 * std_ranking
poloj_dover_int_ranking = mean_ranking + 3 * std_ranking
print(otric_dover_int_ranking, poloj_dover_int_ranking)

# Математическое ожидание и среднеквадратическое отклонение для isIp
mean_isIp = np.mean(df['isIp'])
print(mean_isIp)
std_isIp = np.std(df['isIp'])
print(std_isIp)

# Отрицательный и положительный доверительные интервалы для isIp
otric_dover_int_isIp = mean_isIp - 3 * std_isIp
poloj_dover_int_isIp = mean_isIp + 3 * std_isIp
print(otric_dover_int_isIp, poloj_dover_int_isIp)

# Математическое ожидание и среднеквадратическое отклонение для valid
mean_valid = np.mean(df['valid'])
print(mean_valid)
std_valid = np.std(df['valid'])
print(std_valid)

# Отрицательный и положительный доверительные интервалы для valid
otric_dover_int_valid = mean_valid - 3 * std_valid
poloj_dover_int_valid = mean_valid + 3 * std_valid
print(otric_dover_int_valid, poloj_dover_int_valid)

# Математическое ожидание и среднеквадратическое отклонение для activeDuration
mean_activeDuration = np.mean(df['activeDuration'])
print(mean_activeDuration)
std_activeDuration = np.std(df['activeDuration'])
print(std_activeDuration)

# Отрицательный и положительный доверительные интервалы для activeDuration
otric_dover_int_activeDuration = mean_activeDuration - 3 * std_activeDuration
poloj_dover_int_activeDuration = mean_activeDuration + 3 * std_activeDuration
print(otric_dover_int_activeDuration, poloj_dover_int_activeDuration)

# Математическое ожидание и среднеквадратическое отклонение для urlLen
mean_urlLen = np.mean(df['urlLen'])
print(mean_urlLen)
std_urlLen = np.std(df['urlLen'])
print(std_urlLen)

# Отрицательный и положительный доверительные интервалы для urlLen
otric_dover_int_urlLen = mean_urlLen - 3 * std_urlLen
poloj_dover_int_urlLen = mean_urlLen + 3 * std_urlLen
print(otric_dover_int_urlLen, poloj_dover_int_urlLen)

# Математическое ожидание и среднеквадратическое отклонение для is@
mean_issob = np.mean(df['is@'])
print(mean_issob)
std_issob = np.std(df['is@'])
print(std_issob)

# Отрицательный и положительный доверительные интервалы для issob
otric_dover_int_issob = mean_issob - 3 * std_issob
poloj_dover_int_issob = mean_issob + 3 * std_issob
print(otric_dover_int_issob, poloj_dover_int_issob)

# Математическое ожидание и среднеквадратическое отклонение для isredirect
mean_isredirect = np.mean(df['isredirect'])
print(mean_isredirect)
std_isredirect = np.std(df['isredirect'])
print(std_isredirect)

# Отрицательный и положительный доверительные интервалы для isredirect
otric_dover_int_isredirect = mean_isredirect - 3 * std_isredirect
poloj_dover_int_isredirect = mean_isredirect + 3 * std_isredirect
print(otric_dover_int_isredirect, poloj_dover_int_isredirect)

# Математическое ожидание и среднеквадратическое отклонение для haveDash
mean_haveDash = np.mean(df['haveDash'])
print(mean_haveDash)
std_haveDash = np.std(df['haveDash'])
print(std_haveDash)

# Отрицательный и положительный доверительные интервалы для haveDash
otric_dover_int_haveDash = mean_haveDash - 3 * std_haveDash
poloj_dover_int_haveDash = mean_haveDash + 3 * std_haveDash
print(otric_dover_int_haveDash, poloj_dover_int_haveDash)

# Математическое ожидание и среднеквадратическое отклонение для domainLen
mean_domainLen = np.mean(df['domainLen'])
print(mean_domainLen)
std_domainLen = np.std(df['domainLen'])
print(std_domainLen)

# Отрицательный и положительный доверительные интервалы для domainLen
otric_dover_int_domainLen = mean_domainLen - 3 * std_domainLen
poloj_dover_int_domainLen = mean_domainLen + 3 * std_domainLen
print(otric_dover_int_domainLen, poloj_dover_int_domainLen)

# Математическое ожидание и среднеквадратическое отклонение для nosOfSubdomain
mean_nosOfSubdomain = np.mean(df['nosOfSubdomain'])
print(mean_nosOfSubdomain)
std_nosOfSubdomain = np.std(df['nosOfSubdomain'])
print(std_nosOfSubdomain)

# Отрицательный и положительный доверительные интервалы для nosOfSubdomain
otric_dover_int_nosOfSubdomain = mean_nosOfSubdomain - 3 * std_nosOfSubdomain
poloj_dover_int_nosOfSubdomain = mean_nosOfSubdomain + 3 * std_nosOfSubdomain
print(otric_dover_int_nosOfSubdomain, poloj_dover_int_nosOfSubdomain)

predict_s_proverkoi = []
def proverka_na_dov_intervals():
    anomalyclass = 2
    for i in points_new.index:
        elem = prediction_new[i]
        if (points_new.iloc[i][0] < otric_dover_int_ranking or points_new.iloc[i][0] > poloj_dover_int_ranking) or (points_new.iloc[i][1] < otric_dover_int_isIp or points_new.iloc[i][1] > poloj_dover_int_isIp) or (points_new.iloc[i][2] < otric_dover_int_valid or points_new.iloc[i][2] > poloj_dover_int_valid) or (points_new.iloc[i][3] < otric_dover_int_activeDuration or points_new.iloc[i][3] > poloj_dover_int_activeDuration) or (points_new.iloc[i][4] < otric_dover_int_urlLen or points_new.iloc[i][4] > poloj_dover_int_urlLen) or (points_new.iloc[i][5] < otric_dover_int_issob or points_new.iloc[i][5] > poloj_dover_int_issob) or (points_new.iloc[i][6] < otric_dover_int_isredirect or points_new.iloc[i][6] > poloj_dover_int_isredirect) or (points_new.iloc[i][7] < otric_dover_int_haveDash or points_new.iloc[i][7] > poloj_dover_int_haveDash) or (points_new.iloc[i][8] < otric_dover_int_domainLen or points_new.iloc[i][8] > poloj_dover_int_domainLen) or (points_new.iloc[i][9] < otric_dover_int_nosOfSubdomain or points_new.iloc[i][9] > poloj_dover_int_nosOfSubdomain):
            predict_s_proverkoi.append(anomalyclass)
        else:
            predict_s_proverkoi.append(int(elem))
    print(predict_s_proverkoi)
    print(len(predict_s_proverkoi))

points_new = pd.DataFrame({'ranking': [0, 200, 170, 10000000],
                           'isIp': [0, 0, 1, 0],
                           'valid': [1, 0, 1, 0],
                           'activeDuration': [0, 1, 0, 0],
                           'urlLen':[0, 10, 22, 20],
                           'is@':[1, 1, 0, 0],
                           'isredirect':[1, 0, 1, 0],
                           'haveDash':[0, 0, 1, 1],
                           'domainLen':[190, 10, 500, 20],
                           'nosOfSubdomain':[1, 3, 2, 2],
                           })

prediction_new = dt.predict(points_new)

print(proverka_na_dov_intervals())

points_new.assign(label=predict_s_proverkoi)




















