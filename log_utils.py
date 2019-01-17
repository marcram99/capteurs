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
    """Classe permettant de gérer les logs généré par les capteurs du raspberry pi
        en paramètre d'entrée de la classe : le fichier de log"""

    def __init__(self, *args):
        self.log_file = args[0]
        self.date_log, self.temp, self.hum = self.extract_infos()
        self.args_dict = {"hum": self.hum,
                         "temp": self.temp,
                         "date": self.date_log}
    def __str__(self):
        resultat = self.min_max()
        return "fichier : {}\nnb lignes: {}\n---------------\n{} ".format(self.log_file, len(self.date_log),resultat)

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

    def min_max(self, *args):
        """affiche la val min. et max. de la table passée en argument
            si pas d'arguments: affiche une string avec tout les min/max de l'objet"""
        if args:
            if args[0] in self.args_dict:
                val = self.args_dict[args[0]]
                v_min = val[0]
                v_max = val[0]
                for i in range(0, len(val)):
                    if val[i] < v_min:
                        v_min = val[i]
                    if val[i] > v_max:
                        v_max = val[i]
                print('{}: {} - {}'.format(args[0], v_min, v_max))
                return v_min, v_max
            else:
                raise Exception('args pas pris en charge...')
        else:
            resultat=''
            for key in self.args_dict:
                val = self.args_dict[key]
                v_min = val[0]
                v_max = val[0]
                for i in range(0, len(val)):
                    if val[i] < v_min:
                        v_min = val[i]
                    if val[i] > v_max:
                        v_max = val[i]
                resultat += ('{}: {} - {}\n'.format(key, v_min, v_max))
            print(resultat)
            return resultat

    def search_by_date(self, date):
        nb_res = 0
        print('valeurs pour date: {}'.format(date))
        for num in range(len(self.date_log)):
            if self.date_log[num] == date:
                print(' - temp:{} hum:{}'.format(self.temp[num], self.hum[num]))
                nb_res += 1
        if nb_res == 0:
            print(' - pas de résultats trouvés')

    def search_by_temp(self,temperature):
        temp = '{:.1f}'.format(temperature)
        nb_res = 0
        print('dates pour température: {}'.format(temp))
        for num in range(len(self.temp)):
            if self.temp[num] == temp:
                print(' - {}'.format(self.date_log[num]))
                nb_res += 1
        if nb_res == 0:
            print(' - pas de résultats trouvés')

if __name__ == '__main__':
    #fake_log_gen(datetime(2019, 1, 14), 5, 80, log_file)
    logs = Log_utils(log_file)

    logs.search_by_date('2019-01-14 03:00')
    logs.search_by_temp(5.123)



