
#
# Python Fit Of Hand Data Table
# by Douglas Higinbotham
#

import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
from   math import *

#
# Data File
#

filename="Hand-Data.csv"

#
# Definitions
#

def loadarray(filename,element):
      np.data=[]
      for l in open(filename):
          try:
             values=l.split(",")
             temp=float(values[element])
             np.data.append(temp)
          except:
             continue
      return np.data 

def loadinv(filename,element):
      np.data=[]
      for l in open(filename):
          try:
             values=l.split(",")
             temp=float(values[element])
             np.data.append(1/(temp))
          except:
             continue
      return np.data 

#
# Load The Data
#

q2=loadarray(filename,0)
ge=loadarray(filename,1)
dge=loadarray(filename,2)
wge=loadinv(filename,2)

print "Loaded ",len(q2)," points from", filename,"."

p2, p2stat = poly.polyfit(q2,ge,2,full=True,w=wge)

ffit2=poly.Polynomial(p2)

plt.figure(1)
plt.errorbar(q2,ge,xerr=0,yerr=dge,linestyle="None",fmt='o')
q2r=np.linspace(0,30,3000)
plt.plot(q2r,ffit2(q2r))
plt.xlim(0,3.2)
plt.ylim(0.65,1.01)
plt.xlabel("q$^2$ [fm$^{-2}$]")
plt.ylabel("G$_E$")
plt.show()

print sqrt(-6*p2[1]),' radius'
print p2[0],p2[1],p2[2]
print p2stat[0]/(len(q2)-2)

