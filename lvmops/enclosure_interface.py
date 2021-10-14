import numpy as np
class controls(object):
    def __init__(self):
        self.error_codes = {0:"PASS", 1:"FAIL",-1:"FAULT"}
        # These are dummy plugs to fake values. Think of them like routines which poll the actual physical object
        self.__dome_open__ = 0

    def open_dome(self):
        err_code = 0
        self.__dome_open__ = 0
        return ("dome open",err_code)

    def open_dome(self):
        err_code = 0
        self.__dome_open__ = 1
        return ("dome closed", err_code)

    def status(self):
        """Check uplink to hardware"""
        err_code = 0

        """ Spooky magic, check uplink... and change err_code of failed or timeout"""
        return((),err_code)

class sensors(object):
    def __init__(self, dome_open):
        self.error_codes = {0:"PASS", 1:"FAIL",-1:"FAULT"}
        self.__dome_open__ = dome_open
        self.__t0__ = 27.0
        self.__h0__ = 50.0
    
    def t1(self, scat=3, tmin=0, tmax=30):
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

    def h0(self,scat=5, hmin=0, hmax=75):
        err_code = 0
        h = self.__h0__+scat*np.random.random()
        if (h > hmin) and (h < hmax):
            err_code = 0
        return((h,err_code))

    def dome_open_status(self):
        err_code = 0
        if self.__dome_open__ not in [0,1]:
            err_code = -1
        return((self.__dome_open__,err_code))

    def status(self, PASSFAIL:False):
        if PASSFAIL:
            # All good, no errors
            status_code = 0
            status_code += self.t1()[1]
            status_code += self.t2()[1]
            status_code += self.h0()[1]
            status_code += self.dome_open_status()[1]
            if self.dome_open_status()[1] == 0:
                dome_open = [True,False][self.dome_open_status()[0]]
            else:
                dome_open = "Unknown"

            if status_code != 0:
                status_code = 1    
            status = {"Sensor Status":self.error_codes[status_code], "DomeOpen":dome_open}

        else:
            status = {}
            status["t1"] = self.t1()[0]
            status["t2"] = self.t2()[0]
            status["h0"] = self.h0()[0]
            status["dome_sensor"] = self.dome_open_status()[1]
            if status["dome_sensor"] in [0,1]:
                status["dome_open"] = ["open","closed"][self.dome_open_status()[0]]
            else:
                status["dome_open"] = "FAULT"

        return(status)

class enclosure():
    def __init__(self):
        self.controls = controls()
        self.sensors = sensors(self.controls.__dome_open__)


if __name__ == "__main__":
    from lvmops import enclosure_interface
    encl = enclosure_interface.enclosure()
    print(encl.sensors.status(PASSFAIL=True))
    status_check = encl.sensors.enclosure_status(PASSFAIL=False)
    for sens in status_check:
        if type(status_check[sens]) is str:
            print("%s: %s"%(sens, status_check[sens]))
        if type(status_check[sens]) is int:
            print("%s: %i"%(sens, status_check[sens]))
        if type(status_check[sens]) is float:
            print("%s: %0.3f"%(sens, status_check[sens]))