class spec(object):
    def __init__(self):
        pass

    def expose(self, exptime=0.0, shutter=True, imtype=None, Nexp=1):
        pass

    def dark(self, exptime=0.0, imtype="dark", Nexp=1):
        """
        Ensure all dome lights and calibration lamps are off.
        """
        pass

    def bias(self, Nexp=1):
        """
        Ensure all dome lights and calibration lamps are off.
        """
        pass

    def get_temperature(self, sensor=None):
        pass
