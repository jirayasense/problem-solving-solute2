
import itertools as it

# --- Utils

def segregate_into_groups(lst, grpSize=2):
    '''
    Segregate List into Tuple of Sequential Groups 9each group size = {grpSize} 
    Eg -> 
          lst = [1,2,3,4,5] 
          size = 2 
          => ans := [(1,2), (3,4), (5, None)] 
    '''
    lst_iter = iter(lst)
    return it.zip_longest(*it.repeat(lst_iter, grpSize), fillvalue=None)