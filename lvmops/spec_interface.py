import numpy as np
import time

# class or library import. THis is the LVMI magic
class __control__(object):
    def __init__(self):
        self.__open__ = 0

    def shutter_position(self):
        err_code = 0
        # check "sensor"
        return((self.__open__,err_code))

    def shutter_open(self):
        err_code = 0
        self.__open__ = 0
        return((),err_code)

    def shutter_close(self):
        err_code = 0
        self.__open__ = 0
        return((),err_code)

    def expose(self, **kwargs):
        err_code = 0
        return((),err_code)

class __sensors__(object):
    def __init__(self):
        self.error_codes = {0:"PASS", 1:"FAIL",-1:"FAULT"}
        self.__t0__ = -50.0
        self.__h0__ = 50.0
    
    def t1(self, scat=3, tmin=-100, tmax=-30):
        err_code = 0
        t = self.__t0__+scat*np.random.random()
        if (t > tmin) and (t < tmax):
            err_code = 0
        return((t,err_code))

    def t2(self, scat=3, tmin=0, tmax=30):
        err_code = 0
        t = self.__t0__+scat*np.random.random()
        if (t > tmin) and (t < tmax):
            err_code = 0
        return((t,err_code))

# END OF LVMI magic
####################
# Begin LVM-OPS functions

class spec(object):
    def __init__(self, name="spec"):
        self.name = name
        self.control = __control__()
        self.sensors = __sensors__()
        
    def expose(self, exptime=0.0, shutter=True, imtype=None,Nexp=1):
        err_code = 0
        assert shutter in [True,False,"open","close"], "shutter command invalid"
        assert imtype in ["sci","sky","cal","flat","arc","dark","bias"]
        self.control.expose(exptime=0.0, shutter=True, imtype=None)
        return(0)

    def dark(self, exptime=0.0, imtype="dark",Nexp=1):
        self.control.expose(exptime=exptime,shutter=False)

    def bias(self,Nexp=1):
        self.control.expose(exptime=0.0,shutter=False,imtype="bias")
