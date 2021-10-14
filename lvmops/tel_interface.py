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
            return(0)

        def getdec(self):
            err_code = 0
            return(self.__ra__,err_code)

        def getdec(self):
            err_code = 0
            return(self.__dec__,err_code)

        def getfocus(self):
            err_code = 0
            return(self.__focus__,err_code)


        def GoTo(self, ra, dec, fiber=0, deg=True, speed=10):
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

#LVMI
######
#LVMOps

class telescope(object):
    def __init__(self, name="sci", N_fibers=1600, address=None):
        self.name = name
        self.control = __control__(address=address)
        self.N_fibers = N_fibers
        self.ra = self.control.getra
        self.dec = self.control.getdec
        self.focus = self.control.focus
        self.control = __control__()
        self.GoTo = self.control.GoTo

        
    def GoTo(self, ra, dec, fiber=0, deg=True,out_TextBrowser=None,speed=10):
        # out_TextBrowswer should be an async text stream on a port, which the text_browser is constantly reading. But that is
        # Probably already implemented, so I'm keeping this simple. Also, these are dummy functions...
        out_TextBrowser.append("Moving %s from %0.6f:%0.6f to %0.6f:%0.6f ... "%(self.name, self.ra,self.dec,ra,dec))        
        if self.__async_move__(ra,dec) == 0:
            out_TextBrowser.append("GoTo Complete")
        return(0)

    def autofocus(self):
        self.control.findfocus()
