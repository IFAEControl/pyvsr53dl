import logging

# create logger
log = logging.getLogger('VL53DL')
log.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# formatter = logging.Formatter('%(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
log.addHandler(ch)