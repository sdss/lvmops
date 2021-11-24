
'''
All coordinates are in ICRS unless specified otherwise
'''
class telescope(object):
    def __init__(self, name="sci", address=None):
        pass

    def goto_park(self):
    '''
    Move telescope to safe park position.
    
    ======
    Comments and desired actions:
    - Check dome safety interlock:
        - if interlock is engaged, do not move the telescope. Return error message (assume people are inside dome)
    - run status (LVMI_interface) to check instrument status
        - if not idle (i.e. carrying out any observations or calibrations), abort observation (halt in LVMI_interface) and park telescope 
        (in this case, we assume user wants to park due to an emergency)
    '''
        pass

    def goto_zenith(self):
    '''
    Point telescope to zenith
    
    ======
    Comments and desired actions:
    - Check dome safety interlock:
        - if interlock is engaged, do not move the telescope. Return error message (assume people are inside dome)
    - run status (LVMI_interface) to check instrument status
        - if not idle (i.e. carrying out any observations or calibrations), repeat status command regularly until it returns idle, 
          then move telescope. Regularly give updates (i.e. "waiting for instrument to become idle before moving telescope")
    '''
        pass

    def goto_eq(self, ra, dec, PA=0, target='optical_axis', deg=True):
    '''
    Point telescope to position using RA and dec
    
    ======
    Comments and desired actions:
    - Check dome safety interlock:
        - if interlock is engaged, do not move the telescope. Return error message (assume people are inside dome)
    - run status (LVMI_interface) to check instrument status
        - if not idle (i.e. carrying out any observations or calibrations), repeat status command regularly until it returns idle, 
          then move telescope. Regularly give updates (i.e. "waiting for instrument to become idle before moving telescope")
    '''
        pass

    def goto_aa(self, alt, az, PA=0, target='optical_axis', deg=True):
    '''
    Point telescope to position using alt/az (i.e. point to screen or manually park)
    
    ======
    Comments and desired actions:
    - Check dome safety interlock:
        - if interlock is engaged, do not move the telescope. Return error message (assume people are inside dome)
    - run status (LVMI_interface) to check instrument status
        - if not idle (i.e. carrying out any observations or calibrations), repeat status command regularly until it returns idle, 
          then move telescope. Regularly give updates (i.e. "waiting for instrument to become idle before moving telescope")
    '''
        pass

    def goto_screen(self): 
    '''
    Point telescope to screen for dome flats
    
    ======
    Comments and desired actions:
    - Check dome safety interlock:
        - if interlock is engaged, do not move the telescope. Return error message (assume people are inside dome)
    - run status (LVMI_interface) to check instrument status
        - if not idle (i.e. carrying out any observations or calibrations), repeat status command regularly until it returns idle, 
          then move telescope. Regularly give updates (i.e. "waiting for instrument to become idle before moving telescope")
    '''
        pass

    
    def offset(self, target=None, delta_ra=None, delta_dec=None, delta_x=None, delta_y=None, offset_gbox=False):
    '''
    Pointing offset: change track rates
    
    ======
    Comments and desired actions:
    '''
        pass
    
   
    def guide_offset(self, target=None, delta_ra=None, delta_dec=None, delta_x=None, delta_y=None):
    '''
    Guiding offset: do NOT change track rates
    
    ======
    Comments and desired actions:
    '''
        pass
    
    def offset_gbox(self, delta_x=None, delta_y=None, delta_pa=None):
    '''
    move the guider set points by specified amount; used to move accurate
    offsets by letting the guider do the work. used, e.g., for dithering.

    ======
    Comments and desired actions:
    '''
        pass
    
    def paoffset(self, delta_PA=None):
    '''
    Apply a relative rotation offset by moving the K-mirror
    
    Parameters:
        delta_PA (float): rotation offset in degrees (+/- = E/W)
    
    Returns:
        None
    '''
        pass

    def autofocus(self):
    '''
    Carry out autofocus routine
    
    '''
        pass
    
    def focusoffset(self, delta_f=None):
    '''
    Apply a relative telescope focus offset        
    
    Parameters:
        delta_f (float): focus offset value 
    '''
        pass
    
    def focus(self, value=None, temp=None):
    '''
    Move focus to a particular value or a first guess given a temperature
    
    Parameters:
        value (float): if provided, focus stage moves to this value
        temp (float): if 'value' is not provided or 'value=None', focus stage moves to best guess based on focus vs temperature model
    Returns:
        None
    '''
        pass
        
    def track_on(self, derotator=True, rates=None):
    '''
    Turn on tracking, optionally track in rotation, optionally 
    supply non-sidereal track rates.
    '''
        pass

    def track_off(self):
    '''
    Turn off tracking.
    '''
        pass

    def guide_on(self, guide_parameters=None):
    '''
    Turn on guiding, or modify parameters of running guide loop.
    guide_parameters is a dictionary containing additional parameters for 
    the guiders, e.g. exposure times, cadence, PID parameters, readout or window modes, ...
    '''
        pass

    def guide_off(self):
    '''
    Turn off guiding, revert to tracking (track_on).
    '''
        pass

    def zero_coordinates(self):
    '''
    Zero-out mount model once pointing is verified.
    '''
        pass
