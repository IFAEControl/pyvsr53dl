import unittest

from DisplayModes import Units
from pyvsr53dl import PyVSR53DL

class TestVacuumSense(unittest.TestCase):

    def test_device_query(self):
        import platform
        sensor_address = 1
        sensor_device_label = None
        if platform.system() == 'Darwin':
            sensor_device_label = '/dev/ttyUSB0'
        elif platform.system() == 'Windows':
            sensor_device_label = 'COM6'
        elif platform.system() == 'Linux':
            sensor_device_label = '/dev/ttyUSB0'
        vacuum_sense = PyVSR53DL(sensor_device_label, sensor_address)
        vacuum_sense.open_communication()

        self.assertAlmostEqual(vacuum_sense.get_device_type(), 'VSR205') 
        self.assertAlmostEqual(vacuum_sense.get_product_name(), 'VSR53DL')
        self.assertAlmostEqual(vacuum_sense.get_serial_number_device(), '20002583')
        self.assertAlmostEqual(vacuum_sense.get_serial_number_head(), '20002583')
        self.assertAlmostEqual(vacuum_sense.get_device_version(), 2.0)
        self.assertAlmostEqual(vacuum_sense.get_firmware_version(), '0215')
        self.assertAlmostEqual(vacuum_sense.get_bootloader_version(), 2.0)
        vacuum_sense.set_display_unit(Units.MBAR)
        self.assertAlmostEqual(vacuum_sense.get_display_unit(), Units.MBAR)

        vacuum_sense.close_communication()