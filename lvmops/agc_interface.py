class agc(object):
    def __init__(self, camera=None):
        pass

    def status(self):
    '''
    Return status of agc (i.e. power status, exposing/reading out/idle ).
    '''
        pass

    def reset(self):
        pass

    def power_on(self):
    '''
    Turn on power to agc.
    '''
        pass

    def power_off(self):
    '''
    Turn off power to agc.
    '''
        pass

    def expose(self, exptime=0.0, imtype=None, Nexp=1, save=True):
    '''
    Take exposure
    
    Parameters:
        exptime (float): exposure time
        imtype (string): bias, flat, none
        Nexp (int): number of exposures
        save (Boolean): save the image(s)

    Returns:
        None
    '''
        pass

    def bias(self, Nexp=1):
    '''
    Take bias exposure
    
    Parameters:
        Nexp (int): number of exposures
        
    Returns:
        None
    '''
        pass
