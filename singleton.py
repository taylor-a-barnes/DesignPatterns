"""
   Create a singleton Design Pattern class following the Brog DP
"""

class Singleton(object):
   """Singleton class"""
   __shared_state = {}
   
   def __init__(self, **kwargs)
     self.__dict__ = __shared_state
     __shared_state.update(kwargs)
     
   def __str__(self):
     return str(self.__shared_state)
