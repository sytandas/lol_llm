from __future__ import annotations 
import time, math
from functools import partialmethod, reduce
from itertools import accumulate
import numpy as np
from typing import List, Tuple, Callable, Optional, ClassVar, Type, Union, Sequence

# An instantiation of the Function is the Context
class Function:
  def __init__(self, device:str, *tensors:Tensor):
    self.device = device
    self.needs_input_grad = [t.requires_grad for t in tensors]
    self.requires_grad = True if any(self.needs_input_grad) else None if None in self.needs_input_grad else False
    if self.requires_grad: self.parents = tensors

  def forward(self, *args, **kwargs): raise NotImplementedError(f"forward not implemented for {type(self)}")
  def backward(self, *args, **kwargs): raise RuntimeError(f"backward not implemented for {type(self)}")

class Tensor:
  __slots__ = "lazyd", "req_grad", "grad", "_ctx"
  __deletable__ = ('_ctx',)
  training: ClassVar[bool] = False
  no_grad: ClassVar[bool] = False
  # default_type: ClassVar[DType] = dtypes.float32
