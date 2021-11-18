def ldls(object):
    def __init__(self):
    '''
    Create object to control the LDLS continuum source
    '''
        pass

    def power(self):
        pass

    def status(self):
    '''
    Return readout of all lamps
    '''
        pass

    def on(self):
    '''
    Turn ldls lamps on
    
    ======
    Comments and desired actions:    
    - should regularly run time_on command once lamps are on to ensure they haven't been left on for too long. 
    - Send error message to SDSS observer(?) if time_on exceeds a predetermined limit. This step will prevent 
    lamps being left on during observations, extend the lifetime of lamps, and prevent overheating of lamps 
    and surrounding components.
    - should we check if the dome is open when running this command? If open,error out or request confirmation to turn on lamps
    '''
        pass

    def off(self):
    '''
    Turn ldls lamps off
    '''
        pass

    def time_on(self):
    '''
    return the time the lamp has been on
    '''
        pass


def penray(object):
    def __init__(self, lamp):
    '''
    Create object to control an arc lamp.

    Inputs:
    lamp : str
        the lamp this object will control, e.g. 'HgCd', 'Xe' 
        from a predetermined list of available lamps.
    '''
        pass

    def status(self):
    '''
    Return readout of all lamps
    '''
        pass

    def on(self):
    '''
    Turn penrey lamps on
    
    ======
    Comments and desired actions:    
    - Should regularly run time_on command once lamps are on to ensure they haven't been left on for too long. 
    - Send error message to SDSS observer(?) if time_on exceeds a predetermined limit. This step will prevent 
    lamps being left on during observations, extend the lifetime of lamps, and prevent overheating of lamps 
    and surrounding components.
    - Should we check if the dome is open when running this command? If open, error out or request confirmation to turn on lamps
    '''
        pass

    def off(self):
    '''
    Turn penray lamps off
    '''
        pass

    def time_on(self):
    '''
    return the time the lamp has been on
    '''
        pass
