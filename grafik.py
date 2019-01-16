# encoding: utf-8

import pygal

def data_extract(file):
    hum = []
    temp = []
    date = []
    with open(file, 'r') as f:
        lignes = f.readlines()
        for l in lignes:
            data = l.split('/')
            date.append(data[0])
            temp.append(float(data[1][3:-3]))
            hum.append(int(data[2][3:-3]))

    return date, temp, hum

date, temp, hum = data_extract('temp_logfile.log')
print(temp)


line_chart = pygal.Bar()
line_chart.title = 'Température(en degré Celsius)'
line_chart.add('hum', hum)  # Add some values
line_chart.add('temp', temp)  # Add some values
line_chart.render_to_file('temp_chart.svg')                          # Save the svg to a file
