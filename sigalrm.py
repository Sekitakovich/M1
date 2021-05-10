import signal
from threading import Event
from datetime import datetime as dt
from loguru import logger


class TimeKeeper(object):
    def __init__(self, *, intervalSecs: float = 1):
        self.counter = 0
        self.intervalSecs = intervalSecs
        self.ev = Event()
        self.top = dt.now()
        self.now = self.top
        signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, self.intervalSecs, self.intervalSecs)

    def handler(self, number, stack):
        self.counter += 1
        self.now = dt.now()
        self.ev.set()


if __name__ == '__main__':
    def main():
        tk = TimeKeeper(intervalSecs=0.1)
        while True:
            try:
                tk.ev.wait()
            except (KeyboardInterrupt) as e:
                logger.error(e)
                break
            else:
                tk.ev.clear()
                logger.info(f'[{tk.counter}] {tk.now}')


    main()
