import matplotlib.pyplot as plt


input_values = list(range(1, 1001))
squares = [x**2 for x in input_values]

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(input_values,squares, c=squares, cmap = plt.cm.Blues, s = 10)

ax.set_title("Квадраты чисел", fontsize = 14)
ax.set_xlabel("Значение", fontsize = 14)
ax.set_ylabel("Квадрат значения", fontsize = 14)

ax.tick_params(axis='both', which = 'major', labelsize = 14)

ax.axis([0, 1100, 0, 1100000])
 
plt.show()
