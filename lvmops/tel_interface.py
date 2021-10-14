import numpy as np
import time

class __control__(object):
        # This should create an asynchronous move, that returns current position and status at a regular interval
        # Hmm, maybe that is what the telescope should do.... just constantly send position and status, while listening for  commands on a stream....
        def __init__(self, address=None):
            self.address = address # do something to connect with this
            # well there is no connection
            self.__ra__ = 0.0
            self.__dec__ = 0.0
            self.__focus__ = 0.0

        def getra(self):
            err_code = 0
            return(self.__ra__,err_code)

        def getdec(self):
            err_code = 0
            return(self.__dec__,err_code)

        def getfocus(self):
            err_code = 0
            return(self.__focus__,err_code)


        def GoTo(self, ra, dec, fiber=0, PA=0, deg=True, speed=10):
            err_code = 0
            fiber_offset_ra = 0 * fiber
            fiber_offset_dec = 0 * fiber
            self.__ra__ = ra + fiber_offset_ra
            self.__dec__ = dec + fiber_offset_dec
            return((),err_code)

        def setfocus(self, fval, fmin=-1000, fmax=1000):
            err_code = 0
            if (fval < fmin) or (fval>fmax):
                err_code = 1
            else:
                self.__focus__ = fval
            return((),err_code)

        def findfocus(self):
            err_code = 0
            # adjust focus, expose aquisition cameras, use stars available in detector and find optimal value, return value and flag
            optimal_focus_found, err_code = (0.0, 0)
            return((optimal_focus_found, err_code))

        def aquire(self, ra,dec,**kwargs):
            pass


#LVMI
######
#LVMOps

class telescope(object):
    def __init__(self, name="sci", N_fibers=1600, address=None):
        self.name = name
        self.control = __control__(address=address)
        self.N_fibers = N_fibers
        self.ra = self.control.getra()[0]
        self.dec = self.control.getdec()[0]

        self.getra = self.control.getra
        self.getdec = self.control.getdec
        self.focus = self.control.getfocus

    def GoTo(self, ra, dec, fiber=0, PA=0, deg=True,speed=10):
        # out_TextBrowswer should be an async text stream on a port, which the text_browser is constantly reading. But that is
        # Probably already implemented, so I'm keeping this simple. Also, these are dummy functions...
        result = self.control.GoTo(ra,dec, fiber=fiber, PA=PA)
        if result[1] == 0:
            return(0)
        else:
            return(1)

    def autofocus(self):
        self.control.findfocus()
