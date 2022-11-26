from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die(10)

results = []
var_range = 50000
for roll_num in range(var_range):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    freq = results.count(value)
    frequencies.append(freq)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title':'Результат', 'dtick':1}
y_axis_config = {'title':'Частота результатов'}
my_layout = Layout(title= 'Резултаты подбрасывания двух кубиков' + str(var_range) + 'раз',
                   xaxis = x_axis_config, yaxis =y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename = 'd' + str(die_1.num_sides) + '_d' + str(die_2.num_sides) +'.html')
