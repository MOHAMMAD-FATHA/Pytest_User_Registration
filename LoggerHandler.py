import logging

logger = logging

# Basic configuration and required format of the file
logger.basicConfig(filename="F:\.metadata\Python_User_Registration\ UserRegistration.log",
                    level=logging.INFO, format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

logger.basicConfig(filename="F:\.metadata\Python_User_Registration\ UserRegistration.log",
                    level=logging.ERROR, format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineo)d')