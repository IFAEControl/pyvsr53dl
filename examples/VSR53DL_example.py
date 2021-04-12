from pyvsr53dl.vsr53dl import PyVSR53DL
from pyvsr53dl.DisplayModes import Units as Units
from pyvsr53dl.DisplayModes import Orientation as Orientation
from pyvsr53dl.logger import log
import logging

if __name__ == '__main__':
    from pyvsr53dl.sys import dev_tty
    log.setLevel(logging.INFO)
    sensor_address = 1
    vacuum_sense = PyVSR53DL(dev_tty, sensor_address)
    vacuum_sense.open_communication()
    vacuum_sense.get_device_type()
    vacuum_sense.get_product_name()
    vacuum_sense.get_serial_number_device()
    vacuum_sense.get_serial_number_head()
    vacuum_sense.get_response_delay()
    vacuum_sense.get_device_version()
    vacuum_sense.get_firmware_version()
    vacuum_sense.get_bootloader_version()
    vacuum_sense.get_measurement_range()
    vacuum_sense.get_measurement_value()
    vacuum_sense.get_measurement_value_piezo()
    vacuum_sense.get_measurement_value_pirani()
    vacuum_sense.set_display_unit(Units.MBAR)
    vacuum_sense.get_display_unit()
    vacuum_sense.set_display_orientation(Orientation.NORMAL)
    vacuum_sense.get_display_orientation()
    vacuum_sense.get_relay_1_status()
    vacuum_sense.get_relay_2_status()
    vacuum_sense.get_operating_hours()
    vacuum_sense.close_communication()