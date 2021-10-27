class lvmi(object):
  '''
  This is an interface class for the whole lvmi system. Here we define functions that use several subsystems at the same time
  '''
    def __init__(self, name="lvmi", address=None):
        pass

    def setup_obs(self, obs=None):
      '''
      Point all telescopes to start a fine acquisition for a science observation and home the calibration telescope shutter
    
      Parameters:
      obs (observation): object of class "observation" that contains RA,DEC,PA for science field, two sky fields, and RA,DEC list of calibration stars
       
      Returns:
      None
      '''
      pass
    
    def aquire_obs(self, obs=None, guide=True, offsetcal=True, verify=False)"
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
      
      