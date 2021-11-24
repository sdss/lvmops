

class enclosure(object):
    def __init__(self):
        pass
    
    def open(self):
    '''
    Open the dome
    
    ======
    Comments and desired actions:
    - Check if telescopes are parked before opening dome
        - if telescopes not parked, check dome safety interlock
            - if interlock is engaged, do not open dome and return error message
            - if interlock is not engaged, park telescope and open dome when complete
    - Check dome safety interlock:
        - if interlock is engaged, do not open dome and return error message (assume people are inside dome)
    - Check status of dome and calibration lamps
        - if any lamps on, do not open dome. Return error message (assume calibrations running or people inside dome)
    '''
        pass

    def close(self):
    '''
    Close the dome

    ======
    Comments and desired actions:
    - Check if telescopes are parked before closing dome
        - if telescopes not parked, check dome safety interlock
            - if interlock is engaged, do not close dome and return error message
            - if interlock is not engaged, park telescope and close dome when complete
    - Check dome safety interlock:
        - if interlock is engaged, do not close dome. Return error message (assume people are inside dome)
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
    - Run status (enclosure_interface) to check status of dome
        - if open, do not turn on dome lights
    - run status (LVMI_interface) to check instrument status
        - if not idle (i.e. carrying out any observations or calibrations), do not turn on the dome lights
    '''
        pass

    def dome_lights_off(self):
    '''
    Turn dome lights off

    ======
    Comments and desired actions:
    - Check dome safety interlock:
        - if interlock is engaged, do not turn off the dome lights (assume people are inside dome)
    '''
        pass
