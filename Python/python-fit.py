
#
# Python Fit Of Hand Data Table
# by Douglas Higinbotham
#

import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
from   math import *

#
# Defining Functions
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

def dd(q2): # Doug Dipole Function
    return (1+q2/0.66/25.7)**(-2)

def sd(q2): # Standard Dipole Function
    return (1+q2/0.71/25.7)**(-2)

#
# Load The Data
#

filename="Hand-Data.csv"
q2=loadarray(filename,0)
ge=loadarray(filename,1)
dge=loadarray(filename,2)
wge=loadinv(filename,2)

filename="Carlson.csv"
nq2=loadarray(filename,0)
nge=loadarray(filename,1)
ndge=loadarray(filename,2)
nwge=loadinv(filename,2)

print "Loaded ",len(q2)," points from", filename,"."

p2, p2stat = poly.polyfit(q2,ge,2,full=True,w=wge)
np2, np2stat = poly.polyfit(nq2,nge,2,full=True,w=nwge)

ffit2=poly.Polynomial(p2)
nffit2=poly.Polynomial(np2)

#
# Make Plot of Results
#
plt.rcParams['font.size'] = 14
plt.figure(figsize=(12,6))
plt.errorbar(nq2,nge,xerr=0,yerr=ndge,linestyle="None",fmt='o',label="Carlson Form Factor Data",color="black",zorder=5)
plt.errorbar(q2,ge,xerr=0,yerr=dge,linestyle="None",fmt='o',label="Hand Form Factor Data",color="blue",zorder=10)
q2r=np.linspace(0,30,3000)
plt.plot(q2r,ffit2(q2r), label="Quadratic Fit of Hand Data",color="blue",zorder=0)
#plt.plot(q2r,nffit2(q2r), label="Quadratic Fit of Carlson Data",color="gold",zorder=5)
plt.plot(q2r,dd(q2r), label="Doug 0.84fm Dipole",color="red",zorder=0)
plt.plot(q2r,sd(q2r), label="Standard 0.81fm Dipole",color="lime",zorder=0)
plt.xlim(0,3.2)
plt.ylim(0.7,1.01)
plt.xlabel("Q$^2$ [fm$^{-2}$]")
plt.ylabel("$\mathrm{G}_{\mathrm{E}}$")
plt.legend(loc=1)
plt.show()


#
# Results of Fitting Hand Data
#

print sqrt(-6*p2[1]),' radius'
print p2[1],' linear parameter,',p2[2], 'quadratic parameter'
print p2stat[0]/(len(q2)-2)

#
# Result of Fitting Carlson Data
#

print sqrt(-6*np2[1]),' radius'
print np2[1],' linear parameter,',np2[2], 'quadratic parameter'
print np2stat[0]/(len(nq2)-2)

raise SystemExit()
