# encoding: utf-8
from random import randint
from datetime import datetime

log_file = 'temp_logfile.log'


def fake_log_gen(log_date, temp, hum, log_file):
    for i in range(24):
        hum_delta = randint(-1, 1)
        hum += hum_delta
        temp_delta = (randint(-5, 5)) / 10
        temp += temp_delta
        date = "{:%Y-%m-%d %H:%M}".format(datetime(log_date.year,log_date.month,log_date.day, i, 0))
        data = ("{}/T:{: .2f}C/H:{: .1f}%\n".format(date, temp, hum))
        with open(log_file, 'a') as f:
            f.write(data)


class Log_utils():
    def __init__(self, *args):
        self.log_file = args[0]

    def extract_infos(self):
        tab_date = []
        tab_temp = []
        tab_hum = []
        with open(self.log_file,'r') as file:
            lignes = file.readlines()
            for l in lignes:
                valeurs = l.split('/')
                tab_date.append(valeurs[0])
                tab_temp.append(float(valeurs[1][3:-2]))
                tab_hum.append(float(valeurs[2][3:-2]))
        return tab_date, tab_temp, tab_hum

    def min_max(self):
        v_min = self.val[0]
        v_max = self.val[0]
        for i in range(0,len(self.val)):
            if self.val[i] < v_min:
                        v_min = self.val[i]
            if self.val[i] > v_max:
                v_max = self.val[i]
        return v_min, v_max, len(self.val)


if __name__ == '__main__':
    fake_log_gen(datetime(2019, 1, 14), 5, 80, log_file)
    logs = Log_utils(log_file)
    date_log, temp, hum = logs.extract_infos()

    t_min, t_max, t_nb = Log_utils.min_max(temp)
    print('\ntemp: {} valeurs\nmin: {}\nmax: {}'.format(t_nb, t_min, t_max))

    h_min, h_max, h_nb = Log_utils.min_max(hum)
    print('\nhum: {} valeurs\nmin: {}\nmax: {}'.format(h_nb, h_min, h_max))

