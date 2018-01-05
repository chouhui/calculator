#!/usr/bin/env python3

import sys

counts = sys.argv[1:]
def calculator(num_int):
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
