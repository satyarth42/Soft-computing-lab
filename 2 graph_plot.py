# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:34:31 2018

@author: VP LAB
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,1000)
y = 1/(1+x)

plt.plot(x,y,c='red')
plt.show()