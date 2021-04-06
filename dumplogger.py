import logging
import logging.handlers
from threading import Thread
import time
import pathlib


class DumpLogger(Thread):
    def __init__(self, *, name: str, savedays: int = 180, encoding: str='utf-8'):
        super().__init__()
        self.daemon = True
        self.name = name

        '''
        logging.basicConfigは使わない
        '''
        self.dateFormatfull = '%Y-%m-%d %H:%M:%S'
        self.dateFormatHMS = '%H:%M:%S'
        logPath = pathlib.Path('logs')
        if logPath.exists() is False:
            logPath.mkdir()
        self.logFile = logPath / f'{name}.log'

        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.DEBUG)
        streamFormat = logging.Formatter('%(asctime)s %(threadName)s:%(funcName)s:%(lineno)d : %(message)s',
                                         datefmt=self.dateFormatHMS)
        streamHandler.setFormatter(fmt=streamFormat)

        fileHandler = logging.handlers.TimedRotatingFileHandler(self.logFile, backupCount=savedays, when='midnight',
                                                                interval=1, encoding=encoding)
        fileHandler.setLevel(logging.DEBUG)
        fileFormat = logging.Formatter('%(asctime)s %(threadName)s:%(funcName)s:%(lineno)d : %(message)s',
                                       datefmt=self.dateFormatfull)
        fileHandler.setFormatter(fmt=fileFormat)

        rootLogger = logging.getLogger(name='__main__')
        rootLogger.setLevel(logging.DEBUG)

        self.logger = rootLogger.getChild(name)
        self.logger.addHandler(streamHandler)
        self.logger.addHandler(fileHandler)

    def run(self) -> None:
        counter = 0
        while True:
            time.sleep(1)
            self.logger.debug(msg=f'countetr={counter}')
            counter += 1


if __name__ == '__main__':
    def main():
        member = ['sono1', 'sono2', 'sono3']
        for m in member:
            w = DumpLogger(name=m, encoding='cp932')  # for windows
            w.start()

        time.sleep(5)


    main()
