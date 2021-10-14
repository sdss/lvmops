import time
def flat(object):
    def __init__(self):
        self.__power__ = 1
        self.timeon = False

    def power(self):
        err_code = 0
        # check "power"
        return((self.__power__,err_code))

    def on(self):
        err_code = 0
        self.__power__ = 0
        self.timeon = time.time()
        return((),err_code)

    def off(self):
        err_code = 0
        self.__power__ = 0
        self.timeon = False
        return((),err_code)

    def time_on(self):
        if self.power() == 0:
            time_on = time.time() - self.timeon()
        else:
            time_on = False
        return(time_on)


def arc(object):
    def __init__(self):
        self.__power__ = 1
        self.timeon = False


    def power(self):
        err_code = 0
        # check "power"
        return((self.__power__,err_code))

    def on(self):
        err_code = 0
        self.__power__ = 0
        self.timeon = time.time()
        return((),err_code)

    def off(self):
        err_code = 0
        self.__power__ = 0
        self.timeon = False
        return((),err_code)

    def time_on(self):
        if self.power() == 0:
            time_on = time.time() - self.timeon()
        else:
            time_on = False
        return(time_on)
