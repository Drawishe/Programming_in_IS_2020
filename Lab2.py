

import lxml.html as LH
import pandas as pd


# Парсинг файла

with open('plane.html', 'r') as pln:
    contents = str(pln.read())
    table = LH.fromstring(contents)


    for tr in pd.read_html(contents):
        trs = table.xpath('//td/@bgcolor')
        # print(trs)

pln.close()

# Для каждого цвета свой список
# в цикле преобразуем в rgb из hex
R = []
G = []
B = []
Y = []

for hx in trs:
    s = str(hx)
    # print(s)
    # print(type(s))
    hex = s.lstrip('#')
    rgb = list(int(hex[i:i+2], 16) for i in (0, 2, 4))
    # print(rgb)

    R.append(rgb[0])
    G.append(rgb[1])
    B.append(rgb[2])
    # Y - яркость пикселей
    Y.append(round(0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]))

# Dataframe из списка Y
datafr = pd.DataFrame(data = Y, columns = ['x1'])
# print(datafr)

import matplotlib.pyplot as plt
plt.figure('Разброс пикселей')
plt.plot(datafr)
# plt.savefig('pic1.pdf')
plt.show()

# Нормальное распределение
import seaborn as sns
# plt.figure()
sns.displot(datafr)
plt.title('Область однородностей')
# plt.savefig('pic2.pdf')
plt.show()

from colormap import rgb2hex

YRED = []
for spam in Y:
    if spam >= 3 and spam <= 33:
        spam = rgb2hex(255, 0, 0)
        YRED.append(spam)
    else:
        spam = rgb2hex(spam, spam, spam)
        YRED.append(spam)


# итоговая html таблица

test = 0
fo = open('modified_plane.html', 'a')

fo.write('<HTML><HEAD><TITLE>plane_2.html</TITLE></HEAD><BODY><TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0><tr>')
for row in YRED:
    # fo.write('<TR>')

    if test != 294:
        fo.write(f'<TD BGCOLOR={row}>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</TD>')
        test += 1
        # print(test)
    else:
        fo.write('</tr>')
        fo.write('<tr>')
        fo.write(f'<TD BGCOLOR={row}>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</TD>')
        # fo.write('</TR>')
        test = 1


fo.write('</TR></TABLE></BODY></HTML>')
fo.close()