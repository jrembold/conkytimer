#!/bin/python

import time
import argparse
from pathlib import Path

workdir = Path().absolute()


try: 
    with open(f'{workdir}/currenttime.txt', 'r+') as f:
        v = int(f.read())
        if v > 0:
            minutes, seconds = divmod(v, 60)
            print(f'{minutes}:{seconds:02}')
            v -= 1
            f.seek(0)
            f.write(f'{v}\n')
            f.truncate()
        else:
            print('${color red}0:00')
except:
    print('Countdown finished')

