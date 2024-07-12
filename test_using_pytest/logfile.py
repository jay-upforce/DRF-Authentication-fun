import logging

class logClass:
    def getLogs(self):
        logger = logging.getLogger()
        FileHandler = logging.FileHandler("Logs/mylog.log", mode='w')   # log file name
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        FileHandler.setFormatter(formatter)
        logger.addHandler(FileHandler)
        logger.setLevel(logging.DEBUG)
        return logger