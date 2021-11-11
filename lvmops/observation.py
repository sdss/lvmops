class Observation(object):
  """
  Observation class:
  
  Parameters:
  -----------
  
  name (str): Observation name.
  scira (float): RA of science field
  scidec (float): DEC of science field
  skyEra (float): RA of 1st sky field
  skyEdec (float): DEC of 1st sky field
  skyWra (float): RA of 2nd sky field
  skyWdec (float): DEC of 2nd sky field
  specra (tuple): RA of spectrophotometric standards
  specdec (tuple): DEC of spectrophotometric standards
  gstars (object): object containing guidestars's RA,DEC,pixX,pixY,AGC_ID,magnitude
  texp (float): science (and sky) exposure time
  spectexp (tuple): exposure time of spectophotometric standards
  """
    
    def __init__(self, name):
      self.scira=None
      self.scidec=None
      self.skyEra=None
      self.skyEdec=None
      self.skyWra=None
      self.skyWdec=None
      self.specra=None  
      self.sepcdec=None
      self.gstars=None
      self.spectexp=None
      
      
    
    
    
