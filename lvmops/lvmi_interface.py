class lvmi(object):
  '''
  This is an interface class for the whole lvmi system. Here we define functions that use several subsystems at the same time
  '''
    def __init__(self, name="lvmi", address=None):
        pass

    def startup(self):
    '''
    Setup the instrument for the beginning of operations.
    
    ======
    Comments and desired actions:    
    - Ping all relevant servers and check connectivity (scheduler, data storage, weather, www, etc)
    - Home all telescopes and motors. Set everything to a predetermined status.
    - Verify all hardware is responsive and in a defined state.
    - Verify all calibration lamps are off
    '''
      pass

    def park(self):
    '''
    Park hardware for safe stowage at end of operations.
    
    ======
    Comments and desired actions:    
     - Error out if dome safety interlock is not OK (i.e. people on telescope platform)
    '''
      pass

    def shutdown(self):
    '''
    shutdown all critical equipment (in prep for storm, for example.)
    '''
      pass

    def halt(self):
    '''
    E-Stop. Stop all running tasks/commands/motors immediately
    '''
      pass

    def setup_obs(self, obs=None):
    '''
    Point all telescopes to start a fine acquisition for a science observation and home the calibration telescope shutter
  
    Parameters:
    obs (observation): object of class "observation" that contains RA,DEC,PA for science field, two sky fields, and RA,DEC list of calibration stars
      
    Returns:
    None

    ======
    Comments and desired actions:    
     - Error out if dome safety interlock is not OK (i.e. people on telescope platform)
     - Error out if an exposure is already running (i.e. from previous observation)
    '''
      pass
    
    def aquire_obs(self, obs=None, guide=True, offsetcal=True, verify=False):
    '''
    Do fine aquisition for an observation by locking in science and sky telescope guidestars and 1st calibration star.
    
    Parameters:
    obs (observation): object of class "observation" that contains RA,DEC and guide camera X,Y pixel coordinates for science and sky telescope guidestars and calibration stars
    guide (bool): if True start guiding after fine aquisition is finished
    offsetcal (bool): if True (default) apply offset to put 1st calibration star on 1st calibration fiber. 
    verify (bool): if True output aquisition diagnostics (e.g. astrometry residual plots) and ask for user approval to proceed
    
    Returns:
    None
    '''
      pass

    def execute_obs(self, obs=None):
    '''
    Execute observation described by obs object.
    '''      
      pass

    def warmup_lamps(self, lamps=[]):
    '''
    warmup lamps in list, ...

    Parameters:
    - Should we set a wait command to prevent the user moving onto the exposures while lamps are still warming up?
    '''
      pass

    def bias_sequence(self, ...):
    '''
    Execute bias sequence

    ======
    Comments and desired actions:    
    - Should prepare by turning off calibration lamps and dome lights
    '''
      pass

    def dark_sequence(self, ...):      
    '''
    Execute dark sequence
    ======
    Comments and desired actions:    
    - Should prepare by turning off calibration lamps and dome lights
    '''
      pass

    def flat_sequence(self, ...):      
    '''
    Execute screenflat sequence

    ======
    Comments and desired actions:    
    - Should prepare by turning off dome lights
    - check telescope is pointed at screen
    '''
      pass

    def twi_sequence(self, ...):      
    '''
    Execute twilight flat sequence

    ======
    Comments and desired actions:    
    - Should prepare by turning off dome lights
    
    '''
      pass

    def arc_sequence(self, ...):      
    '''
    Execute arc sequence

    ======
    Comments and desired actions:    
    - Should prepare by turning off dome lights
    - check telescope is pointed at screen
    '''
      pass

    def agc_flat_sequence(self, ...):
    '''
    Execute AGC screen flat sequence

    ======
    Comments and desired actions:    
    - Should prepare by turning off dome lights
    - Check telescope is pointed at screen
    '''
      pass
