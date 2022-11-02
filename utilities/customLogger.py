import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".//Logs/automation.log",
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG,force=True)
        # logging.basicConfig(filename="C:\\Users\\Lenovo\\PycharmProjects\\nopcommerceApp\\Logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
