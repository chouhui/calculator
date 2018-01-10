#!/usr/bin/env python3
import sys

class Config(object):
    def __init__(self, path):
        self._config = {}
        index = counts.index('-c')
        path = counts[index+1]
        with open(path) as f:
            for i in f:
                name, value = i.split('=')
                self._config[name.strip()] = value.strip()
    def get_config(self):
        return self._config


class UserData(object):
    def __init__(self, path):
        self._userdata = {}
        with open(path) as f:
            for i in f:
                num, value = i.split(',')
                self._userdata[num] = value.strip()
        self.she = 0
        self.ge = 0
        self.gong = 0
  
    def get_userdata(self)
        return self._userdata

    def calculator(co, config):
        l = float(config['JiShuL'])
        H = float(config['JiShuH'])
        YangLao = float(config['YangLao'])
        YiLiao = float(config['YiLiao'])
        ShiYe = float(config['ShiYe'])
        GongShang = float(config['GongShang'])
        ShengYu = float(config['ShengYu'])
        GongJiJin = float(config['GongJiJin'])
        value = float(co['value'])
        if value <= 
        
        
            
def calculator(num_int, ca):
    if num_int <= 0:
        tax = 0
    elif num_int <= 1500:
        tax = num_int * 0.03
    elif num_int <= 4500:
        tax = num_int * 0.10 - 105
    elif num_int <= 9000:
        tax = num_int * 0.20 - 555
    elif num_int <= 35000:
        tax = num_int * 0.25 - 1005
    elif num_int <= 55000:
        tax = num_int * 0.30 - 2755
    elif num_int <= 80000:
        tax = num_int * 0.35 - 5505
    else:
        tax = num_int * 0.45 - 13505
    return tax

for count in counts:
    num, cash = count.split(':')
    try:
        num_int = int(num)
        cash_int = int(cash) - 3500 - int(cash)*0.165
        tax = calculator(cash_int)
        nev = int(cash) - tax - int(cash)*0.165
        print('{}:{:.2f}'.format(num_int,nev))
    except:
        print('Parameter Error')


if __name__ == "__main__":
    
    counts = sys.argv[1:]
    index = counts.index('-c')
    path = counts[index+1]
    index1 = counts.index('-d')
    path1 = counts[index1+1]
    index2 = counts.index('o')
    path2 = counts[index2+1]
    config = Config(path)
    configs = config.get_config()
    user = UserData(path1)
    users = user.get_userdata()
    user.calculator()
    user.dumptofile(path2)
