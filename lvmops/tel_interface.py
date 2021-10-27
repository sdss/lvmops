
class telescope(object):
    def __init__(self, name="sci", address=None):
        pass

    def goto(self, ra, dec, PA=0, target='optical_axis', deg=True):
        pass

    def goto_screen(self): 
        pass

    def offset(self, target=None, delta_ra=None, delta_dec=None, delta_x=None, delta_y=None):
        
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
        
        
        
        
        
    
    
    
    
