import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)
ax.set_title("Квадраты чисел", fontsize = 14)
ax.set_xlabel("Значение", fontsize = 14)
ax.set_ylabel("Квадрат значения", fontsize = 14)
ax.tick_params(axis='both', labelsize = 14)


plt.show()