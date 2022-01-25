from pyvsr53dl.vsr53dl import PyVSR53DL
from pyvsr53dl.logger import log
import logging
import time

if __name__ == '__main__':
    from pyvsr53dl.sys import dev_tty
    log.setLevel(logging.INFO)
    sensor_address = 1
    vacuum_sense = PyVSR53DL(dev_tty, sensor_address)
    vacuum_sense.open_communication()
    vacuum_sense.get_device_type()
    vacuum_sense.get_product_name()
    try:
        while(True):
            vacuum_sense.get_measurement_value()
            time.sleep(1.0)
    except KeyboardInterrupt:
        vacuum_sense.close_communication()