
class telescope(object):
    def __init__(self, name="sci", address=None):
        pass

    def goto_park(self):
    '''
    Move telescope to safe park position.
    '''
        pass

    def goto_zenith(self):
        pass

    def goto_eq(self, ra, dec, PA=0, target='optical_axis', deg=True):
        pass

    def goto_aa(self, alt, az, PA=0, target='optical_axis', deg=True):
        pass

    def goto_screen(self): 
        pass

    # pointing offset: change track rates
    def offset(self, target=None, delta_ra=None, delta_dec=None, delta_x=None, delta_y=None):
        pass
    
    # guiding offset: do NOT change track rates
    def guide_offset(self, target=None, delta_ra=None, delta_dec=None, delta_x=None, delta_y=None):
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
    '''
        pass

    def guide_off(self):
        pass

    def zero_coordinates(self):
    '''
    Zero-out mount model once pointing is verified.
    '''
        pass