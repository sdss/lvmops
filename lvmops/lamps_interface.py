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
    - check dome safety interlock
        - if engaged, do not turn on lights. Return error message
    - once lights are on, regularly run time_on command once lamps are on to ensure they haven't been left on for too long. 
        - give warning if they have been on for a set time (time TBD, depends on how quickly they would overheat or 
          leak heat into enclosure/instrument. this step also prevents the lamps being left on accidentally)
        - after another set time, check status in lvmi_interface, and if idle, turn off lamps 
    - Run status (enclosure_interface) to check status of dome
        - if open, do not turn on dome lights. Return error message
    - Run status (lvmi_interface) to check status of instrument
        - if not idle (i.e. exposing a dark image), repeat command until it returns idle
        - if idle, turn on lamps
    '''
        pass

    def off(self):
    '''
    Turn ldls lamps off
    
    ======
    Comments and desired actions:    
    - Run status (lvmi_interface) to check status of instrument
        - if not idle (i.e. exposing), repeat command until it returns idle
        - if idle, turn off lamps
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
    - check dome safety interlock
        - if engaged, do not turn on lights. Return error message
    - once lights are on, regularly run time_on command once lamps are on to ensure they haven't been left on for too long. 
        - give warning if they have been on for a set time (time TBD, depends on how quickly they would overheat or 
          leak heat into enclosure/instrument. this step also prevents the lamps being left on accidentally)
        - after another set time, check status in lvmi_interface, and if idle, turn off lamps 
    - Run status (enclosure_interface) to check status of dome
        - if open, do not turn on dome lights. Return error message
    - Run status (lvmi_interface) to check status of instrument
        - if not idle (i.e. exposing a dark image), repeat command until it returns idle
        - if idle, turn on lamps
    '''
        pass

    def off(self):
    '''
    Turn penray lamps off

    ======
    Comments and desired actions:    
    - Run status (lvmi_interface) to check status of instrument
        - if not idle (i.e. exposing), repeat command until it returns idle
        - if idle, turn off lamps
    '''
        pass

    def time_on(self):
    '''
    return the time the lamp has been on
    '''
        pass
