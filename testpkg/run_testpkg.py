import argparse
import coloredlogs
import logging
import os


# Create a logger object.
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Run testpkg')
parser.add_argument('--min_level', help='logging minimum level', default='DEBUG')
args = parser.parse_args()

# If you don't want to see log messages from libraries, you can pass a
# specific logger object to the install() function. In this case only log
# messages originating from that logger will show up on the terminal.
coloredlogs.install(level=args.min_level, logger=logger)

# Some examples.
logger.debug("this is a debugging message")
logger.info("this is an informational message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")

with open(os.path.join('testpkg', 'data', 'CrueConfigMetier.xml'), 'r') as filein:
    print(filein)
