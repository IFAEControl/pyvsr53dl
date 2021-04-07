from pyvsr53dl.logger import log as log
from pyvsr53dl.AccessCodes import AccessCode as AC
from pyvsr53dl.Commands import Commands as CMD
from pyvsr53dl.DisplayModes import Units as Units
# from DISPLAY import Orientation as Orientation

class ThyrCommPackage():
    """
    Thyracont Communication Protocol Package class to create and compose its messages
    """
    def __init__(self, address):
        self._address = address # 3 bytes
        self._access_code = None # 1 byte
        self._cmd = None # 2 bytes
        self._data_length = 0 # 2 bytes
        self._data = 0 # N bytes
        self._checksum = None # 1 byte

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def access_code(self):
        return self._access_code
    @access_code.setter
    def access_code(self, access_code):
        self._access_code = access_code

    @property
    def cmd(self):
        return self._cmd
    @cmd.setter
    def cmd(self, cmd):
        self._cmd = cmd

    @property
    def data_length(self):
        return self._data_length
    @data_length.setter
    def data_length(self, data_length):
        self._data_length = data_length

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data):
        self._data = data

    def get_checksum(self):
        address = self.get_ascii_list(f'{self.address:03d}')
        access_code = self.get_ascii_list(f'{self.access_code}')
        cmd = self.get_ascii_list(self.cmd)
        length = self.get_ascii_list(f'{self.data_length:02d}')
        checksum_list = [address, access_code, cmd, length]
        if self.data_length:
            checksum_list.append(self.get_ascii_list(f'{self.data}'))
        checksum = sum([sum(values) for values in checksum_list])
        return chr(checksum % 64 + 64)

    def get_package(self):
        """
        Returns the bytes that compose this thyracont communication package ready to send
        :return: comm_package
        """
        if self.data:
            self.data_length = len(str(self.data))
        comm_package = [f'{self.address:03d}', f'{self.access_code}', self.cmd, f'{self.data_length:02d}']
        if self.data_length:
            data = f'{self.data}'
            comm_package.append(data)
        comm_package.append(self.get_checksum())
        comm_package.append('\r')
        return comm_package

    def get_string(self):
        """
        Returns the comm_package into a string
        :return: comm_package_string
        """
        comm_package_string = "".join(self.get_package())
        return comm_package_string

    def get_package_ascii_list(self):
        """
        Returns a list with the ASCII table values of the characters that compose the package string
        :return: package_ascii_list
        """
        package_ascii_list = self.get_ascii_list(self.get_string())
        return package_ascii_list

    def parse_answer(self, answer):
        answer = answer.decode('utf-8')

        log.debug(answer)
        self.address = int(answer[0:3])
        self.access_code = int(answer[3])
        self.cmd = answer[4:6]
        self.data_length = int(answer[6:8])
        if self.data_length:
            self.data = answer[8:8+self.data_length]
        else:
            self.data = 0
        checksum = answer[8+self.data_length]

        log.debug(answer)
        log.debug(f'Device Address: {self.address}')
        log.debug(f'Access Code: {self.access_code}')
        log.debug(f'CMD: {self.cmd}')
        log.debug(f'Data Length: {self.data_length}')
        log.debug(f'Data: {self.data}')
        log.debug(f'Checksum: {self.get_checksum()}')
        if checksum == self.get_checksum():
            log.debug("Checksum matches!")
        else:
            log.debug("Checksum mismatch!")
        return answer


    @staticmethod
    def get_ascii_list(string):
        return [ord(c) for c in(string)]


if __name__ == '__main__':
    SENSOR_ADDRESS = 2
    t_package = ThyrCommPackage(SENSOR_ADDRESS)
    t_package.access_code = AC.WR_TX
    t_package.cmd = CMD.Display_Unit
    t_package.data = Units.MBAR
    log.info(t_package.get_package())
    log.info(t_package.get_string())
    # print([hex(value) for value in t_package.get_package_ascii_list()])
