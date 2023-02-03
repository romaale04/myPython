import logging

logging.basicConfig(
    level=logging.DEBUG,
    level=logging.ERROR,
    filename="my_log.log",
    format="%(ascTime)s - %(module)s - %(levelName)s - %(funcName)s - %(message)s",
    datefmt='%d-%m-%Y %H:%M:%S'
)
format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
datefmt='%d-%m-%Y %H:%M:%S'