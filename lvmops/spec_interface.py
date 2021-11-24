class spec(object):
    def __init__(self):
        pass

    def expose(self, exptime=0.0, Nexp=1, imtype=None, shutter=True, metadata=None, ccdmodes=None):
        '''
        Take an exposure
        
        Parameters:
            exptime (float): exposure time
            Nexp (int): number of exposures
            imtype (string): bias, dark, None
            shutter (Boolean): tells the software whether to acutate shutter
            metadata (): carries additional info to put in FITS header
            ccdmodes (): carries CCD setup information if needed (binning, readout mode/speed)
        
        
        ======
        Comments and desired actions:
            - Check status of dome lamps (status in enclosure_interface)
                - if lamps on, do not expose. Return error message

        '''
        pass

    def dark(self, exptime=0.0, Nexp=1, imtype="dark", metadata=None, ccdmodes=None):
        """
        Take a dark exposure
        
        Parameters:
            exptime (float): exposure time
            Nexp (int): number of exposures
            imtype (string): dark
            metadata (): carries additional info to put in FITS header
            ccdmodes (): carries CCD setup information if needed (binning, readout mode/speed)
        
        
        ======
        Comments and desired actions:
            - Check status of dome lamps (status in enclosure_interface) and calibration lamps (status in lamps_interface)
                - if dome lamps are on, do not expose. Return error message
                - if calibration lamps are on, check instrument status (lvmi_interface) to see if other exposures are being carried out
                    - if idle, turn off calibration lamps and continue
                    - if not idle, repeat status check periodically and turn off calibration lamps when it returns idle

        """
        pass

    def bias(self, Nexp=1, imtype="bias", metadata=None, ccdmodes=None):
        """
        Ensure all dome lights and calibration lamps are off.

        Parameters:
            Nexp (int): number of exposures
            imtype (string): bias
            metadata (): carries additional info to put in FITS header
            ccdmodes (): carries CCD setup information if needed (binning, readout mode/speed)
        
        
        ======
        Comments and desired actions:
            - Check status of dome lamps (status in enclosure_interface) and calibration lamps (status in lamps_interface)
                - if dome lamps are on, do not expose. Return error message
                - if calibration lamps are on, check instrument status (lvmi_interface) to see if other exposures are being carried out
                    - if idle, turn off calibration lamps and continue
                    - if not idle, repeat status check periodically and turn off calibration lamps when it returns idle
       """
        pass

    def get_temperature(self, sensor=None):
    """
    Return temperature of sensors
    """
        pass
