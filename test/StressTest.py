from pyvsr53dl.vsr53dl import PyVSR53DL
from pyvsr53dl.logger import log
import csv
from datetime import datetime
import logging

log.setLevel(logging.ERROR)

def get_now_timestamp_str():
    now = datetime.now()
    return now.strftime("%m%d%Y%H%M%S")

def open_file():
    filename = f'./results/Stress_test_results_{get_now_timestamp_str()}.csv'
    file = open(filename, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(["Run", "Measurement", "Time Stamp"])
    return writer

def stress_test():
    from pyvsr53dl.sys import dev_tty
    sensor_address = 1
    vacuum_sense = PyVSR53DL(dev_tty, sensor_address)
    vacuum_sense.open_communication()
    writer = open_file()
    for run in range(100000000):
        measurement = vacuum_sense.get_measurement_value()
        print(f"RUN #{run} measurement: {measurement}mbar")
        writer.writerow([run, measurement, get_now_timestamp_str()])
    vacuum_sense.close_communication()


if __name__ == '__main__':
    stress_test()