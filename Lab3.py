import pandas as pd
import numpy as np

df = pd.read_csv('combined_dataset.csv')
df = df.drop(columns='domain')
df

df.shape
df = df.dropna()
df.shape

df = df.drop_duplicates()
df.shape

from sklearn.model_selection import train_test_split

points_train, points_test, labels_train, labels_test = train_test_split(df.iloc[:, :-1], df['label'], test_size=0.25, random_state=0)
print(points_train, points_test)

print(points_train.shape, points_test.shape)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(points_train)
points_train.iloc[:, :] = ss.transform(points_train)
points_test.iloc[:, :] = ss.transform(points_test)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=11, metric='euclidean')
knn.fit(points_train, labels_train)

prediction = knn.predict(points_test)
print(prediction)
print(points_test.assign(predict=prediction))

print(format(knn.score(points_test, labels_test)))

ss = StandardScaler()
df['ranking'] = ss.fit_transform(df)
df['isIp'] = ss.fit_transform(df)
df['valid'] = ss.fit_transform(df)
df['activeDuration'] = ss.fit_transform(df)
df['urlLen'] = ss.fit_transform(df)
df['is@'] = ss.fit_transform(df)
df['isredirect'] = ss.fit_transform(df)
df['haveDash'] = ss.fit_transform(df)
df['domainLen'] = ss.fit_transform(df)
df['nosOfSubdomain'] = ss.fit_transform(df)

mean_ranking = np.mean(df['ranking'])
print(mean_ranking)
std_ranking = np.std(df['ranking'])
print(std_ranking)

otric_dover_int_ranking = mean_ranking - 3 * std_ranking
poloj_dover_int_ranking = mean_ranking + 3 * std_ranking
print(otric_dover_int_ranking, poloj_dover_int_ranking)

mean_isIp = np.mean(df['isIp'])
print(mean_isIp)
std_isIp = np.std(df['isIp'])
print(std_isIp)

otric_dover_int_isIp = mean_isIp - 3 * std_isIp
poloj_dover_int_isIp = mean_isIp + 3 * std_isIp
print(otric_dover_int_isIp, poloj_dover_int_isIp)

mean_valid = np.mean(df['valid'])
print(mean_valid)
std_valid = np.std(df['valid'])
print(std_valid)

otric_dover_int_valid = mean_valid - 3 * std_valid
poloj_dover_int_valid = mean_valid + 3 * std_valid
print(otric_dover_int_valid, poloj_dover_int_valid)

mean_activeDuration = np.mean(df['activeDuration'])
print(mean_activeDuration)
std_activeDuration = np.std(df['activeDuration'])
print(std_activeDuration)

otric_dover_int_activeDuration = mean_activeDuration - 3 * std_activeDuration
poloj_dover_int_activeDuration = mean_activeDuration + 3 * std_activeDuration
print(otric_dover_int_activeDuration, poloj_dover_int_activeDuration)


mean_urlLen = np.mean(df['urlLen'])
print(mean_urlLen)
std_urlLen = np.std(df['urlLen'])
print(std_urlLen)

otric_dover_int_urlLen = mean_urlLen - 3 * std_urlLen
poloj_dover_int_urlLen = mean_urlLen + 3 * std_urlLen
print(otric_dover_int_urlLen, poloj_dover_int_urlLen)

mean_issob = np.mean(df['is@'])
print(mean_issob)
std_issob = np.std(df['is@'])
print(std_issob)

otric_dover_int_issob = mean_issob - 3 * std_issob
poloj_dover_int_issob = mean_issob + 3 * std_issob
print(otric_dover_int_issob, poloj_dover_int_issob)

mean_isredirect = np.mean(df['isredirect'])
print(mean_isredirect)
std_isredirect = np.std(df['isredirect'])
print(std_isredirect)

otric_dover_int_isredirect = mean_isredirect - 3 * std_isredirect
poloj_dover_int_isredirect = mean_isredirect + 3 * std_isredirect
print(otric_dover_int_isredirect, poloj_dover_int_isredirect)

mean_haveDash = np.mean(df['haveDash'])
print(mean_haveDash)
std_haveDash = np.std(df['haveDash'])
print(std_haveDash)

otric_dover_int_haveDash = mean_haveDash - 3 * std_haveDash
poloj_dover_int_haveDash = mean_haveDash + 3 * std_haveDash
print(otric_dover_int_haveDash, poloj_dover_int_haveDash)

mean_domainLen = np.mean(df['domainLen'])
print(mean_domainLen)
std_domainLen = np.std(df['domainLen'])
print(std_domainLen)

otric_dover_int_domainLen = mean_domainLen - 3 * std_domainLen
poloj_dover_int_domainLen = mean_domainLen + 3 * std_domainLen
print(otric_dover_int_domainLen, poloj_dover_int_domainLen)

mean_nosOfSubdomain = np.mean(df['nosOfSubdomain'])
print(mean_nosOfSubdomain)
std_nosOfSubdomain = np.std(df['nosOfSubdomain'])
print(std_nosOfSubdomain)

otric_dover_int_nosOfSubdomain = mean_nosOfSubdomain - 3 * std_nosOfSubdomain
poloj_dover_int_nosOfSubdomain = mean_nosOfSubdomain + 3 * std_nosOfSubdomain
print(otric_dover_int_nosOfSubdomain, poloj_dover_int_nosOfSubdomain)









