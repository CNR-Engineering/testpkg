import argparse
import logging
import os

from testpkg.base import log

# Create a logger object.
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Run testpkg')
parser.add_argument('--min_level', help='logging minimum level', default='DEBUG')
args = parser.parse_args()

log(args.min_level, logger)

with open(os.path.join('testpkg', 'data', 'CrueConfigMetier.xml'), 'r') as filein:
    print(filein)
