import itertools
import pandas as pd

# ?expand.grid in R -- lite version
def expand_grid(x, y, colnames=None, *argv):
    """
    A relatively comparable function to expand.grid in R
    
    Returns a dataframe
    
    TODO: remove hardcoding and multiple 
    """
    
    # checks
    assert isinstance(x, list), "x is not a list"
    assert isinstance(y, list), "y is not a list"
    if colnames is not None:
      assert isinstance(colnames, list), "colnames is not a list"
    
    
    # create the cartesian product
    xy = list(itertools.product(x,y))
    if colnames:
      combos = pd.DataFrame(xy, columns=colnames)
    else:
      combos = pd.DataFrame(xy)
    
    # return the dataframe
    return(combos)


## another function
def test_argv(*argv):
  # data validation
  assert len(argv) > 0, "must include 1 or more list objects"
  x = list()
  # the tests
  if argv:
    for arg in argv:
      x.append(arg)
  # return stuff
  return(x)


## another function
def test_kwargs(**kwargs):
  # data validation
  assert len(kwargs) > 0, "must include at least 1 argument"
  
  # dict comprehension
  x = {'{}'.format(key) for key, value in kwargs}
  
  # return stuff
  return(x)


## args
def test_kwargs(*args):
  # data validation
  assert len(args) > 0, "must include at least 1 argument"
  
  # dict comprehension
  x = {('v{}'.format(key), value) for (key, value) in enumerate(args)}
  
  # return stuff
  return(x)

## asnother
def product_dict(**kwargs):
    keys = kwargs.keys()
    vals = kwargs.values()
    for instance in itertools.product(*vals):
        yield dict(zip(keys, instance))



