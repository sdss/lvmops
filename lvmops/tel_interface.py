
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
    - Error out if the dome safety interlock are not OK (i.e. people on telescope platform)
    '''
        pass

    def goto_zenith(self):
    '''
    Point telescope to zenith
    
    ======
    Comments and desired actions:
    - Error out if the dome safety interlock are not OK (i.e. people on telescope platform)
    '''
        pass

    def goto_eq(self, ra, dec, PA=0, target='optical_axis', deg=True):
        pass

    def goto_aa(self, alt, az, PA=0, target='optical_axis', deg=True):
        pass

    def goto_screen(self): 
    '''
    Point telescope to screen for dome flats
    
    ======
    Comments and desired actions:
    - Error out if the dome safety interlock are not OK (i.e. people on telescope platform)
    '''
        pass

    # pointing offset: change track rates
    def offset(self, target=None, delta_ra=None, delta_dec=None, delta_x=None, delta_y=None, offset_gbox=False):
        pass
    
    # guiding offset: do NOT change track rates
    def guide_offset(self, target=None, delta_ra=None, delta_dec=None, delta_x=None, delta_y=None):
        pass
    
    # change guider set points
    def offset_gbox(self, delta_x=None, delta_y=None, delta_pa=None):
    '''
    move the guider set points by specified amount; used to move accurate
    offsets by letting the guider do the work. used, e.g., for dithering.
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
        pass

    def guide_on(self, guide_parameters=None):
    '''
    Turn on guiding, or modify parameters of running guide loop.
    guide_parameters is a dictionary containing additional parameters for 
    the guiders, e.g. exposure times, cadence, PID parameters, readout or window modes, ...
    '''
        pass

    def guide_off(self):
        pass

    def zero_coordinates(self):
    '''
    Zero-out mount model once pointing is verified.
    '''
        pass
