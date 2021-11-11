class spec(object):
    def __init__(self):
        pass

    def expose(self, exptime=0.0, Nexp=1, imtype=None, shutter=True, metadata=None, ccdmodes=None):
        '''
        shutter tells the software whether to acutate shutter
        metadata carries additional info to put in FITS header
        ccdmodes carries CCD setup information if needed (binning, readout mode/speed)
        '''
        pass

    def dark(self, exptime=0.0, Nexp=1, imtype="dark", metadata=None, ccdmodes=None):
        """
        Ensure all dome lights and calibration lamps are off.
        """
        pass

    def bias(self, Nexp=1, metadata=None, ccdmodes=None):
        """
        Ensure all dome lights and calibration lamps are off.
        """
        pass

    def get_temperature(self, sensor=None):
        pass
