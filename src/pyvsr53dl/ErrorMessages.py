"""
Error messages from device
"""
MSG = {
    'NO_DEF' : 'Command is not valid (not defined) for the device',
    '_LOGIC' : 'Access Code is not valid or execution of command is not logical',
    '_RANGE' : 'Error if any data value in send sequence is out of range.',

    'ERROR1' : 'Sensor is defect or stacked out',
    'SYNTAX' : 'Command is valid, but the syntax in data is wrong or the selected mode in data is not valid for your device',

    'LENGTH' : 'Command is valid, but the length of data is out of expected range',
    '_CD_RE' : 'Calibration Data Read Error',
    '_EP_RE' : 'EEPROM Read Error',
    '_UNSUP' : 'Unsupported Data',
    '_SEDIS' : 'Sensor element disabled'
}