from random import randrange
from numpy import random
import numpy as np
import pandas as pd

from numpy.random import rand
from . import Variables as var

class MC:
  data = pd.DataFrame(index=["kBT", "energy", "heat capacity"])
  def makeconf(self):
    var.set_initial_state()

  def update_state(self):
    i = randrange(var.Nx - 1)
    j = randrange(var.Ny - 1)
    s = var.s
    s_trial = s.copy()
    s_trial[i,j] = -1 * s[i,j]
    delta_E = -2 * s_trial[i,j] * (s[i-1, j] + s[i+1, j] + s[i, j-1] + s[i, j+1])

    E_trial = var.cal_energy() + delta_E
    if E_trial < var.E:
      var.s = s_trial
      var.E = E_trial
    elif random() < np.exp(-delta_E/var.kBT):
      var.s = s_trial
      var.E = E_trial
    


  def calculate(self):
    self.update_state()
  
  def run(self):
    self.makeconf()
    STEPS = 40000
    OBSERVE = 10
    kBT_list = np.linspace(0.001,6, 201)

    for kBT in kBT_list:
      var.kBT = kBT

  