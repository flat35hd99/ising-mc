import numpy as np
from random import random, randrange

class Variables:
  N = 10
  Nx = N
  Ny = N
  s = np.ones([Nx, Ny], int)
  kBT = 0.001
  E = 0

  def set_initial_state(self):
    half = Variables.s.size / 2
    stock = []
    k = 0
    while k < range(half):
      i = randrange(Variables.Nx - 1)
      j = randrange(Variables.Ny - 1)
      if (i, j) in stock:
        continue
      Variables.s[i,j] = -1 * Variables.s[i,j]
      k += 1
    self.cal_enegry()

  def cal_energy(self):
    _energy = 0
    for i in range(-1,Variables.Nx):
      for j in range(0,Variables.Ny):
        l=i
        m=j

        if l==-1:
          l = Variables.Nx
        if l == Variables.Nx:
          l = 0
        if m ==-1:
          m  =Variables.Ny
        if m== Variables.Ny:
          m=0

        ll = i + 1
        if ll == Variables.Nx:
          ll=0
        _energy += Variables.s[l, m]*Variables.s[ll, m] 

    for i in range(0,Variables.Nx):
      for j in range(-1,Variables.Ny):

        l=i
        m=j

        if l==-1:
          l=Variables.Nx
        if l == Variables.Nx:
          l=0
        if m ==-1:
          m=Variables.Ny
        if m== Variables.Ny:
          m=0

        mm=j+1
        if mm == Variables.Ny:
          mm=0
        _energy += Variables.s[l, m] * Variables.s[l, mm]
    
    return _energy