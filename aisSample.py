import pathlib
from datetime import datetime as dt, timedelta


class Emulator(object):
    def __init__(self, *, log: str):
        src = pathlib.Path(log)
        with open(file=src, mode='rt') as f:
            all = f.read().split('\n')
            for index, line in enumerate(all, 0):
                if line:
                    ymd, hms, header, nmea = line.split(' ')
                    at = dt.strptime(ymd + ' ' + hms, '%Y-%m-%d %H:%M:%S.%f')
                    print(f'{index:06d} {at} {nmea}')
            # while True:
            #     line = f.readline()
            #     if line:
            #         ymd, hms, header, nmea = line.split(' ')
            #         ooo = nmea.encode()
            #         pass
            #     else:
            #         break
        pass


if __name__ == '__main__':
    def main():
        em = Emulator(log='2019-07-15.log.txt')
        pass


    main()
