import pandas as pd
import numpy as np
import string


# letters
def letters(upper=False, n=None):
  # the data
  if upper:
    l = list(string.ascii_uppercase)
  else:
    l = list(string.ascii_lowercase)
  # if n, how many to randomly sample
  if n > 0:
    l = np.random.choice(l, n)
  
  l = list(l)
  return( l )

  
# state_name
def state_name():
  
