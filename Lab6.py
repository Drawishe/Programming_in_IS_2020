from PIL import Image, ImageDraw
import numpy as np
import pandas as pd

# Открываем изображения кожи
im1 = Image.open('leather/1.png')
im2 = Image.open('leather/2.png')
im3 = Image.open('leather/3.png')
im4 = Image.open('leather/4.png')
im5 = Image.open('leather/5.png')
im6 = Image.open('leather/6.png')
im7 = Image.open('leather/7.png')
im8 = Image.open('leather/8.png')
im9 = Image.open('leather/9.png')
im10 = Image.open('leather/10.png')

# Считываем пиксели, создаем массив с пикселями кожи
pixelsLeather_1 = list(im1.getdata())
pixelsLeather_2 = list(im2.getdata())
pixelsLeather_3 = list(im3.getdata())
pixelsLeather_4 = list(im4.getdata())
pixelsLeather_5 = list(im5.getdata())
pixelsLeather_6 = list(im6.getdata())
pixelsLeather_7 = list(im7.getdata())
pixelsLeather_8 = list(im8.getdata())
pixelsLeather_9 = list(im9.getdata())
pixelsLeather_10 = list(im10.getdata())

pixels_ALL_Leather = []
pixels_ALL_Leather.extend(pixelsLeather_1)
pixels_ALL_Leather.extend(pixelsLeather_2)
pixels_ALL_Leather.extend(pixelsLeather_3)
pixels_ALL_Leather.extend(pixelsLeather_4)
pixels_ALL_Leather.extend(pixelsLeather_5)
pixels_ALL_Leather.extend(pixelsLeather_6)
pixels_ALL_Leather.extend(pixelsLeather_7)
pixels_ALL_Leather.extend(pixelsLeather_8)
pixels_ALL_Leather.extend(pixelsLeather_9)
pixels_ALL_Leather.extend(pixelsLeather_10)
# print(pixels_ALL_Leather)

# Создаем датафрейм из этого списка, удаляем столбец, отвечающий за прозрачность, присваиваем label = 1, данным значениям, удаляем дубликаты
np.reshape(pixels_ALL_Leather,(len(pixels_ALL_Leather), 4))
df_Leather = pd.DataFrame(data=pixels_ALL_Leather, columns = ['R','G','B','H'])
del df_Leather['H']
df_Leather['label'] = 1
# df_Leather = df_Leather.drop_duplicates()
print(df_Leather)

# Открываем изображения не относящиеся к коже
im11 = Image.open('samples/1.png')
im12 = Image.open('samples/2.png')
im13 = Image.open('samples/3.png')
im14 = Image.open('samples/4.png')
im15 = Image.open('samples/5.png')
im16 = Image.open('samples/6.png')
im17 = Image.open('samples/7.png')

# Считываем пиксели, создаем массив с пикселями не содержащими кожу
pixelsSample_1 = list(im11.getdata())
pixelsSample_2 = list(im12.getdata())
pixelsSample_3 = list(im13.getdata())
pixelsSample_4 = list(im14.getdata())
pixelsSample_5 = list(im15.getdata())
pixelsSample_6 = list(im16.getdata())
pixelsSample_7 = list(im17.getdata())

pixels_NOT_Leather = []
pixels_NOT_Leather.extend(pixelsSample_1)
pixels_NOT_Leather.extend(pixelsSample_2)
pixels_NOT_Leather.extend(pixelsSample_3)
pixels_NOT_Leather.extend(pixelsSample_4)
pixels_NOT_Leather.extend(pixelsSample_5)
pixels_NOT_Leather.extend(pixelsSample_6)
pixels_NOT_Leather.extend(pixelsSample_7)

# Создаем датафрейм из этого списка, удаляем столбец, отвечающий за прозрачность, присваиваем label = 0, данным значениям, удаляем дубликаты
np.reshape(pixels_NOT_Leather,(len(pixels_NOT_Leather), 4))
df_Samples = pd.DataFrame(data=pixels_NOT_Leather, columns = ['R','G','B','H'])
del df_Samples['H']
df_Samples['label'] = 0
df_Samples = df_Samples.drop_duplicates()
print(df_Samples)

# Объединяем датасеты в один
df_Base = pd.concat([df_Leather, df_Samples])
print(df_Base)
# columns = df_Base.columns
# print(columns)
# for column in columns:
#     print(column)
#     print(df_Base[column].value_counts(dropna=False))

# Разбиваем данные на тренировочные и тестовые
from sklearn.model_selection import train_test_split
points_train_RGB, points_test_RGB, labels_train_RGB, labels_test_RGB = train_test_split(df_Base.iloc[:, :-1], df_Base['label'], test_size=0.5, random_state=0)
print(points_train_RGB, points_test_RGB)

# Строим "наивный классификатор Байеса"
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

gnb_RGB = GaussianNB()
gnb_RGB.fit(points_train_RGB, labels_train_RGB)
prediction_RGB = gnb_RGB.predict(points_test_RGB)
# print(points_test.assign(predict=prediction))
print(format(gnb_RGB.score(points_test_RGB, labels_test_RGB)))
# print(labels_train_RGB)

# Кросс-валидация RGB
scores = cross_val_score(gnb_RGB, df_Base[df_Base.columns[:3]], df_Base['label'], cv=10)

print(scores, "SCORES RGB")
print(scores.mean(), "SCORES MEAN RGB")
print(scores.std(), "SCORES STD RGB")

# Переводим значения RGB в HSV
import colorsys
HSV_Leather = []
for i in pixels_ALL_Leather:
    HSV_Leather.append(colorsys.rgb_to_hsv(i[0], i[1], i[2]))
# print(HSV_ALL_Leather)

HSV_Samples = []
for i in pixels_NOT_Leather:
    HSV_Samples.append(colorsys.rgb_to_hsv(i[0], i[1], i[2]))
# print(HSV_Samples)

# Присваиваем метки, объединяем датасет
df_HSV_Leather = pd.DataFrame(data=HSV_Leather, columns=['H', 'S', 'V'])
df_HSV_Leather['label'] = 1

df_HSV_Samples = pd.DataFrame(data=HSV_Samples, columns=['H', 'S', 'V'])
df_HSV_Samples['label'] = 0
df_BaseHSV = pd.concat([df_HSV_Leather, df_HSV_Samples])
# print(df_BaseHSV)
columns = df_BaseHSV.columns
print(columns)
for column in columns:
    print(column)
    print(df_BaseHSV[column].value_counts(dropna=False))

# Разбиваем данные на тренировочные и тестовые
# Строим "наивный классификатор Байеса"
points_train_HSV, points_test_HSV, labels_train_HSV, labels_test_HSV = train_test_split(df_BaseHSV.iloc[:, :-1], df_BaseHSV['label'], test_size=0.25, random_state=0)
# print(points_train_HSV, points_test_HSV)
gnb_HSV = GaussianNB()
gnb_HSV.fit(points_train_HSV, labels_train_HSV)
prediction_HSV = gnb_HSV.predict(points_test_HSV)
# print(points_test.assign(predict=prediction))
print(format(gnb_HSV.score(points_test_HSV, labels_test_HSV)))
# print(labels_train_HSV)

# Кросс-валидация HSV
scores_HSV = cross_val_score(gnb_HSV, df_BaseHSV[df_BaseHSV.columns[:3]], df_BaseHSV['label'], cv=10)

print(scores_HSV, "SCORES HSV")
print(scores_HSV.mean(), "SCORES MEAN HSV")
print(scores_HSV.std(), "SCORES STD HSV")

# Тест на изображении
imgTEST = Image.open('1222.png')
width = imgTEST.size[0] #Определяем ширину.
print(width)
height = imgTEST.size[1] #Определяем высоту.
print(height)
pixelsTEST = list(imgTEST.getdata())

# Создаем массив RGB
RGB_TEST = []
for i in pixelsTEST:
    RGB_TEST.append((i[0], i[1], i[2]))
# len(RGB_TEST)

# Заполняем датафрейм RGB
points_new_RGB = pd.DataFrame(data=RGB_TEST, columns=['R', 'G', 'B'])
predict_TEST_RGB = gnb_RGB.predict(points_new_RGB)
points_new_RGB = points_new_RGB.assign(label=predict_TEST_RGB)
df_TEST_NEW_RGB = pd.DataFrame(data=points_new_RGB)
# print(points_new_RGB[column].value_counts())

columns = df_TEST_NEW_RGB.columns
print(columns)
for column in columns:
    print(column)
    print(df_TEST_NEW_RGB[column].value_counts(dropna=False))

RGB = []
for it, i in enumerate(RGB_TEST):
    i = list(i)
    i.append(predict_TEST_RGB[it])
    RGB.append(i)
RGB_2 = []
for it, i in enumerate(RGB):
    if (predict_TEST_RGB[it]==1):
        i[0] = 255
        i[1] = 0
        i[2] = 0
    RGB_2.append((i[0], i[1], i[2]))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

array = np.array(RGB_2).reshape(height, width, 3)
plt.imshow(array.astype(np.uint8))

# Преобразуем из RGB в HSV
HSV_TEST = []
for i in pixelsTEST:
        HSV_TEST.append(colorsys.rgb_to_hsv(i[0], i[1], i[2]))

# np.reshape(HSV_TEST,(len(HSV_TEST), 4))
points_new = pd.DataFrame(data=HSV_TEST, columns=['H', 'S', 'V'])
# del points_new['Z']
predidict_TEST = gnb_HSV.predict(points_new)
points_new = points_new.assign(label=predidict_TEST)
df_TEST_NEW = pd.DataFrame(data=points_new)

columns = df_TEST_NEW.columns
print(columns)
for column in columns:
    print(column)
    print(df_TEST_NEW[column].value_counts(dropna=False))

HSV_2 =[]
for it, i in enumerate(HSV_TEST):
    i = list(i)
    i.append(predidict_TEST[it])
    HSV_2.append(i)
RGB_3 = []
for it, i in enumerate(HSV_2):
    if (predidict_TEST[it]==1):
        i[0] = 0
        i[1] = 1
        i[2] = 100
    RGB_3.append(colorsys.hsv_to_rgb(i[0], i[1], i[2]))

array = np.array(RGB_3).reshape(height, width, 3)
plt.imshow(array.astype(np.uint8))

