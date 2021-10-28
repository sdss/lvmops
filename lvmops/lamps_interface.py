def ldls(object):
    def __init__(self):
    '''
    Create object to control the LDLS continuum source
    '''
        pass

    def power(self):
        pass

    def status(self):
        pass

    def on(self):
        pass

    def off(self):
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
        pass

    def on(self):
        pass

    def off(self):
        pass

    def time_on(self):
    '''
    return the time the lamp has been on
    '''
        pass
