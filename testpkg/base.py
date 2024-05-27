import coloredlogs
from importlib_resources import files


def log(min_level, logger):
    coloredlogs.install(level=min_level, logger=logger)

    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")

    with files('testpkg').joinpath('data/CrueConfigMetier.xml').open('r') as filein:
        print(type(filein))
        print(filein)
