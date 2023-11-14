from visca.camera import Camera

class Optim(Camera):

    """ Mapping from shutter speed to hex setting """
    speed_table = {}
    speed_table['1/10000'] = '21'
    speed_table['1/6000'] = '20'
    speed_table['1/4000'] = '1F'
    speed_table['1/3000'] = '1E'
    speed_table['1/2000'] = '1D'
    speed_table['1/1500'] = '1C'
    speed_table['1/1000'] = '1B'
    speed_table['1/725'] = '1A'
    speed_table['1/500'] = '19'
    speed_table['1/350'] = '18'
    speed_table['1/250'] = '17'
    speed_table['1/180'] = '16'
    speed_table['1/125'] = '15'
    speed_table['1/100'] = '14'
    speed_table['1/90'] = '13'
    speed_table['1/60'] = '12'
    speed_table['1/50'] = '11'
    speed_table['1/30'] = '10'
    speed_table['1/20'] = '0F'
    speed_table['1/15'] = '0E'
    speed_table['1/10'] = '0D'
    speed_table['1/8'] = '0C'
    speed_table['1/6'] = '0B'
    speed_table['1/4'] = '0A'
    speed_table['1/3'] = '09'
    speed_table['1/2'] = '08'
    speed_table['2/3'] = '07'
    speed_table['1/1'] = '06'


    def __init__(self, output='/dev/ttyUSB0'):
        """Sony VISCA control class.

        :param output: Serial port string. (default: 'COM1')
        :type output: str
        """
        self.interp = interp1d([int(f[:-1], 16) for f in self.values], self.y)
        super(self.__class__, self).__init__(output=output)

    def init(self):
        """Initializes camera object by connecting to serial port.

        :return: Camera object.
        :rtype: Camera
        """
        super(self.__class__, self).init()
        return self

    def comm(self, com):
        """Sends hexadecimal string to serial port.

        :param com: Command string. Hexadecimal format.
        :type com: str
        :return: Success.
        :rtype: bool
        """
        super(self.__class__, self).command(com)

    def set_shutter_speed(self, speed):
        """set the shutter speed on the camera when in manual mode

        Args:
            speed (str): shutter speed in 1/s
        """
        if speed in speed_table:
            cmd = '8101044A0000' + '0' + speed_table[speed][0] + '0' + speed_table[speed][1] + 'FF'
            return self.command(cmd)




    