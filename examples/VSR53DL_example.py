from pyvsr53dl import VacuumSenseVSR53DL
from AccessCodes import AccessCode as AC
from Commands import Commands as CMD
from DisplayModes import Units as Units
from DisplayModes import Orientation as Orientation
from logger import log as log
import platform

if __name__ == '__main__':
    sensor_address = 1
    sensor_device_label = None
    log.info(f"I'm on {platform.system()}")
    if platform.system() == 'Darwin':
        sensor_device_label = '/dev/ttyUSB0'
    elif platform.system() == 'Windows':
        sensor_device_label = 'COM6'
    elif platform.system() == 'Linux':
        sensor_device_label = '/dev/ttyUSB0'
    else:
        log.info("Fuck, don't know the platform I'm running on...")

    vacuum_sense = VacuumSenseVSR53DL(sensor_device_label, sensor_address)
    vacuum_sense.open_communication()
    # vacuum_sense.restart_device()
    # vacuum_sense.set_baud_rate(115200)
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