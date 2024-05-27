import coloredlogs
from importlib import resources as impresources
import os

from . import data


def log(min_level, logger):
    coloredlogs.install(level=min_level, logger=logger)

    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")

    with open(impresources.files(data) / 'CrueConfigMetier.xml', 'r') as filein:
        print(filein)
