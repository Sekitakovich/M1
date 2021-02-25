from loguru import logger
import signal
from threading import Event


class TimeKeeper(object):
    def __init__(self, *, intervalSecs: int = 1):
        self.counter = 0
        self.intervalSecs = intervalSecs
        self.ev = Event()
        signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, self.intervalSecs, self.intervalSecs)

    def handler(self, number, stack):
        self.counter += 1
        self.ev.set()


if __name__ == '__main__':
    def main():
        tk = TimeKeeper()
        while True:
            try:
                tk.ev.wait()
            except (KeyboardInterrupt) as e:
                logger.error(e)
                break
            else:
                tk.ev.clear()
                logger.info(f'counter = {tk.counter}')


    main()
