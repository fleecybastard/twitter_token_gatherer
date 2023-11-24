import logging
import sys

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

hdlr = logging.StreamHandler(stream=sys.stdout)
hdlr.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')

hdlr.setFormatter(formatter)

logger.addHandler(hdlr)
