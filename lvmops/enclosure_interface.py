

class enclosure(object):
    def __init__(self):
        pass
    
    def open(self):
    '''
    Open the dome
    
    ======
    Comments and desired actions:
    - Ensure telescopes are parked before opening dome
    - Error out if the dome safety interlock are not OK (i.e. people on telescope platform)
    - Error out if any calibration lamps are on
    - Error out if dome lights are on
    '''
        pass

    def close(self):
    '''
    Close the dome

    ======
    Comments and desired actions:
    - Close the enclosure
    - Ensure telescopes are parked before closing dome
    - Error out if dome safety interlock is not OK (i.e. people on telescope platform)
    '''
        pass

    def status(self):
    '''
    Return readout of all sensors, lights and dome position.
    '''
        pass

    def dome_lights_on(self):
    '''
    Turn dome lights on
    
    ======
    Comments and desired actions:
    - Error out if dome is open
    '''
        pass

    def dome_lights_off(self):
    '''
    Turn dome lights off
    '''
        pass
