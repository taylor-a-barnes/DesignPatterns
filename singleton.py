"""
   Create a singleton Design Pattern class following the Brog DP
"""

class Singleton(object):
   """Singleton class"""
   _shared_data = {}
   
   def __init__(self, **kwargs):
     self.__dict__ = self._shared_data
     _shared_data.update(kwargs)
     
   def __str__(self):
     return str(self._shared_data)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

param = Singleton(VT='Virginia Tech')

print(param)
print(param,VT)

y = Singleton(MSS='MolSSI software scientist')

print(param.MSS)
