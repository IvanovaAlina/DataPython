import csv
from matplotlib import pyplot as plt

filename = 'data/data_temp1.csv'
f = open(filename)
reader = csv.reader(f)
header_row = next(reader)

#получение заголовков с индексацией (для определения столбцов
for index, column_head in enumerate(header_row):
    print(index, column_head)

highs = []
for row in reader:
    #print(row[26])
    if row[26] != "":
        high = int(row[26])
        highs.append(high)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c="red")

plt.show()
