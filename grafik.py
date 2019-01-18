# encoding: utf-8
import pygal
from log_utils import Log_utils

class Grafik():
    def __init__(self, logs):
        self.temp = logs.temp
        self.hum = logs.hum
        self.date_log = logs.date_log
        self.heures = [int(x[-6:-4]) for x in self.date_log]


    def daily_temp(self):
        graph = []
        for i in range(len(self.temp)):
            graph.append((self.heures[i], self.temp[i]))
        chart = pygal.XY()
        chart.title = 'Température(degré Celsius)'
        chart.x_labels = (0, 3, 6, 9, 12, 15, 18, 21)
        chart.add('temp', graph)
        chart.render_to_file('00_graph.svg')

if __name__ == '__main__':
    logs = Log_utils('log_temp_mod.log')
    obj = Grafik(logs)
    obj.daily_temp()



