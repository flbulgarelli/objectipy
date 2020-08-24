# =======
# Imports
# =======
import types

class Obj:
  def __init__(self):
    self._attrs = {}

  def __setattr__(self, name, value):
    if name == '_attrs':
      super().__setattr__(name, value)
    elif isinstance(value, types.FunctionType):
      self._attrs[name] = value.__get__(self, Obj)
    else:
      self._attrs[name] = value

  def __getattr__(self, name):
    if name == '_attrs':
      return super().__getattr__(name)
    else:
      return self._attrs[name]

  def __repr__(self):
    if '__repr__' in self._attrs:
      return self._attrs['__repr__']()
    else:
      return super().__repr__()
