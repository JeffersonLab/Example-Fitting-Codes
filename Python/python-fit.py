
#
# Python Fit Of Hand Data 
# by Douglas Higinbotham
#

import numpy as np
import numpy.polynomial.polynomial as poly
from   scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib import container
from   math import *
#
# Definition For Reading Data From ASCII File
#

def loaddata(filename,cutoff):
    data=[]
    for l in open(filename):
       try:
          values=l.split(",")
          q2=float(values[0])
          ge=float(values[1])
          dge=float(values[2])
          if q2 <= cutoff:
             data.append([q2,ge,dge])
       except:
          continue
    return np.transpose(data) # Changing From Python List To Transposed NumPY Array

#
# Definition Of Charge Form Factor Functions
#

def dd(q2): # Doug Dipole Function
    return (1+q2/0.66/25.7)**(-2)

def sd(q2): # Standard Dipole Function
    return (1+q2/0.71/25.7)**(-2)

def jan(q2): 
      x=q2/25.7
      jan = 1 -3.36591660e+00*x + 1.45487683e+01*x**2 -8.87959239e+01*x**3 + \
            4.61097705e+02*x**4 -1.67562381e+03*x**5 + 4.07646487e+03*x**6  \
           -6.45411460e+03*x**7 + 6.34035079e+03*x**8 -3.49373923e+03*x**9 + 8.22601568e+02*x**10
      return jan

#
# Definition of Fit Functions
#

def func1(q2,p1,p2):
    global A
    A = p2 
    return (1+p1*q2+p2*q2**2)

def func2(q2,p1):
    return (1+p1*q2+A*q2**2)

#
# Calculation of Proton Radius
#

def rcalc(p1):
    try:
       radius=sqrt(-6*p1)
    except:
       radius=-1
    return radius

#
# Load The Data
#

filename="Hand-Data.csv"
cutoff=3.0
hand=loaddata(filename,cutoff)
q2=hand[0]
ge=hand[1]
dge=hand[2]
wge=1/dge
print ("Loaded ",len(q2)," points from", filename,".")

filename="Carlson.csv"
carlson=loaddata(filename,cutoff)
nq2=carlson[0]
nge=carlson[1]
ndge=carlson[2]
nwge=1/ndge
print ("Loaded ",len(nq2)," points from", filename,".")

p2, p2stat = poly.polyfit(q2,ge,2,full=True,w=wge)
np2, np2stat = poly.polyfit(nq2,nge,2,full=True,w=nwge)

ffit2=poly.Polynomial(p2)
nffit2=poly.Polynomial(np2)

#
# Do The Hand Paper Fits
#

popt1, pcov1 = curve_fit(func1, q2, ge,sigma=dge)
print ("1st Fit Parameters", popt1)
#Derived Chi Squared Value For This Model
chi_squared = np.sum(((func1(q2, *popt1) - ge) / dge) ** 2)
reduced_chi_squared = chi_squared / (len(q2) - len(popt1))
print ("with a chi2 of {0:.3f} ".format(chi_squared))
print ("with a reduced chi2 of {0:.3f} ".format(reduced_chi_squared))

filename="Hand-Data.csv"
cutoff=1.05
hand=loaddata(filename,cutoff)
lq2=hand[0]
lge=hand[1]
ldge=hand[2]
lwge=1/dge

popt2, pcov2 = curve_fit(func2, lq2, lge,sigma=ldge)
print ("2nd Fit Parameters", popt2)

print ("Loaded ",len(lq2)," points from", filename,".")
chi_squared = np.sum(((func2(lq2, *popt2) - lge) / ldge) ** 2)
reduced_chi_squared = chi_squared / (len(lq2) - len(popt2))
print ("with a chi2 of ",chi_squared)
print ("with a redcued chi2 of ",reduced_chi_squared)

e1=np.asarray(pcov1[0])
e2=np.asarray(pcov2[0])
print (e1,e2)

print ("Proton Radius 1st Fit = ",rcalc(popt1[0])," +/- ",rcalc((popt1[0]-sqrt(e1[0])))-rcalc(popt1[0]))
print ("Proton Radius 2nd Fit = ",rcalc(popt2[0])," +/- ",rcalc((popt2[0]-sqrt(e2[0])))-rcalc(popt2[0]))

q2r=np.linspace(0,30,3000)

#
# Make Plot of Results
#

plt.rcParams['font.size'] = 14
plt.figure(figsize=(12,6))
plt.errorbar(nq2,nge,xerr=0,yerr=ndge,linestyle="None",fmt='o',label="Grifioen & Carlson Analysis",color="black",zorder=5)
plt.errorbar(q2,ge,xerr=0,yerr=dge,linestyle="None",fmt='o',label="Hand Form Factor Data",color="blue",zorder=10)
plt.plot(q2r,func2(q2r,*popt2), label="Quadratic Fit of Hand Data",color="blue",zorder=0)
plt.plot(q2r,dd(q2r), label="Doug 0.84fm Dipole",color="red",zorder=10)
plt.plot(q2r,jan(q2r), label="Jan 0.88fm Polynomial",color="green",zorder=10)
plt.plot(q2r,sd(q2r), label="Standard 0.81fm Dipole",color="lime",zorder=0)
plt.xlim(0,3.2)
plt.ylim(0.7,1.01)
plt.xlabel("Q$^2$ [fm$^{-2}$]")
plt.ylabel("$\mathrm{G}_{\mathrm{E}}$")

# Remove Error Bars From Legend
ax = plt.gca()
handles, labels = ax.get_legend_handles_labels()
new_handles = []
for h in handles:
    #only need to edit the errorbar legend entries
    if isinstance(h, container.ErrorbarContainer):
        new_handles.append(h[0])
    else:
        new_handles.append(h)
ax.legend(new_handles, labels,loc=1)

#plt.legend(loc=1)
plt.show()


#
# Result of Fitting Carlson Data
#
print ()
print ("Results of Fitting Carlson Points")
print ()
print (sqrt(-6*np2[1]),' radius')
print (np2[1],' linear parameter,',np2[2], 'quadratic parameter')
print (np2stat[0]/(len(nq2)-2))

#
# Exit
#
raise SystemExit()
