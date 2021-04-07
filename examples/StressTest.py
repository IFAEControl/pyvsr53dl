from src.pyvsr53dl import PyVSR53DL
import csv
from datetime import datetime


def get_now_timestamp_str():
    now = datetime.now()
    return now.strftime("%m%d%Y%H%M%S")

def stress_test():
    from src.sys import dev_tty
    sensor_address = 1
    vacuum_sense = PyVSR53DL(dev_tty, sensor_address)
    vacuum_sense.open_communication()
    filename = f'Stress_test_results_{get_now_timestamp_str()}.csv'
    file = open(filename, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(["Run", "Measurement", "Time Stamp"])
    for run in range(1000):
        measurement = vacuum_sense.get_measurement_value()
        print(f"RUN #{run} measurement: {measurement}mbar")
        writer.writerow([run, measurement, get_now_timestamp_str()])
    vacuum_sense.close_communication()


if __name__ == '__main__':
    stress_test()