import itertools
import pandas as pd

# ?expand.grid in R -- lite version
def expand_grid2(x, y, colnames=None):
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



def expand_grid(*itrs, cols=None):
  
  # colname validation and definition
  if cols:
    assert isinstance(cols, list), "cols must be a list"
    assert len(cols) == len(itrs), "The number of column names must match the length of *itrs"
    cnames = cols
  else:
    cnames = ["var{}".format(i+1) for i in range(len(itrs))]
  
  # modified from: https://stackoverflow.com/a/12131385/155406
  product = list(itertools.product(*itrs))
  
  # make the dataframe
  df = pd.DataFrame(product, columns=cnames)
  return(df)





