import platform

if platform.system() == 'Darwin':
    dev_tty = '/dev/ttyUSB0'
elif platform.system() == 'Windows':
    dev_tty = 'COM6'
elif platform.system() == 'Linux':
    dev_tty = '/dev/ttyUSB0'
