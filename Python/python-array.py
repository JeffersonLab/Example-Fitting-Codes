
#
# Python Fit Of Hand Data Table
# by Douglas Higinbotham
#

filename="full.csv"

import numpy as np
import numpy.polynomial.polynomial as poly
import numpy.polynomial.laguerre as lagu
import matplotlib.pyplot as plt

from matplotlib import container
from math import *
from scipy.optimize import curve_fit

#
# Defining Functions
#

def func(q2,n1,m1):
      return (1+n1*q2)/(1+m1*q2)

def zero(q2):
      zero=0*q2
      return zero 

def loadarray(filename,element,typ):
      np.ttt=[]
      for l in open(filename):
          try:
             values=l.split(",")
             one=typ(values[element])
             np.ttt.extend([one])
#             np.ttt.append([one])
          except:
             continue
      return np.asarray(np.ttt)

def loadarray2(filename,cut):
      np.ttt=[]
      for l in open(filename):
          try:
             values=l.split(",")
             one=float(values[0])
             two=float(values[1])
             three=float(values[2])
             four=str(values[3])
             five=1/three
          except:
             continue
          if (four==cut) or (cut=="none"):
             np.ttt.extend([[one,two,three,five]])
      sss=np.transpose(np.ttt)
      return sss
#      return plt.errorbar(sss[0],sss[1],xerr=0,yerr=sss[2],marker='o',label=cut,linestyle="none")

def loadratio(filename,cut):
      np.ttt=[]
      for l in open(filename):
          try:
             values=l.split(",")
             one=float(values[0])
             two=(float(values[1])-sd(one))/sd(one)
             three=float(values[2])/sd(one)
             four=str(values[3])
          except:
             continue
          if (four==cut):
             np.ttt.extend([[one,two,three]])
      sss=np.transpose(np.ttt)
      return plt.errorbar(sss[0],sss[1],xerr=0,yerr=sss[2],marker='o',label=cut,linestyle="none")

def jan(q2): # Jan Ge
      x=q2
      jan = 1 -3.36591660e+00*x + 1.45487683e+01*x**2 -8.87959239e+01*x**3 + 4.61097705e+02*x**4 -1.67562381e+03*x**5 + 4.07646487e+03*x**6  -6.45411460e+03*x**7 + 6.34035079e+03*x**8 -3.49373923e+03*x**9 + 8.22601568e+02*x**10
      return jan

def jam(q2): # Jan Gm
     x=q2
     jam = 1 - 2.65842069e+00*x + 2.89693429e+00*x**2 + 2.54442451e+00*x**3 + 2.96659176e+01*x**4 -2.85555012e+02*x**5 + 9.25396398e+02*x**6  -1.57504071e+03*x**7 + 1.51259219e+03*x**8  -7.76928514e+02*x**9 +  1.66272626e+02*x**10
     return jam

def sd(q2):
      return (1+q2/0.71/25.7)**(-2)

def gevsd(q2):
      return (1+q2/0.71)**(-2)

def dd(q2):
      return (1+0.1176*q2/2)**(-2)

def dl(q2):
      return (1-q2*0.1176)

def jl(q2):
      return (1-q2*0.129)

def il(q2):
      return (1-q2*0.141)

def hl(q2):
      return (1-q2*0.1067)

#
# Load The Data Into 1D Vectors
#

q2=loadarray(filename,0,float)
ge=loadarray(filename,1,float)
dge=loadarray(filename,2,float)
nam=loadarray(filename,3,str)

www=1/dge
#
print ("Loaded ",len(q2)," points from", filename)
print ("From ",len(np.unique(nam))," authors")
print (np.unique(nam))

#
# Polynominal Fits 
#

fit=loadarray2(filename,"none")

p1, p1stat = lagu.lagfit(fit[0],fit[1],1,full=True,w=fit[3])
p2, p2stat = lagu.lagfit(fit[0],fit[1],2,full=True,w=fit[3])
p3, p3stat = lagu.lagfit(fit[0],fit[1],3,full=True,w=fit[3])
p4, p4stat = lagu.lagfit(fit[0],fit[1],4,full=True,w=fit[3])
p5, p5stat = poly.polyfit(fit[0],fit[1],5,full=True,w=fit[3])
p6, p6stat = poly.polyfit(fit[0],fit[1],6,full=True,w=fit[3])
p7, p7stat = poly.polyfit(fit[0],fit[1],7,full=True,w=fit[3])
p8, p8stat = poly.polyfit(fit[0],fit[1],8,full=True,w=fit[3])
p9, p9stat = poly.polyfit(fit[0],fit[1],9,full=True,w=fit[3])
p10, p10stat = poly.polyfit(fit[0],fit[1],10,full=True,w=fit[3])
p11, p11stat = poly.polyfit(fit[0],fit[1],11,full=True,w=fit[3])
p12, p12stat = poly.polyfit(fit[0],fit[1],12,full=True,w=fit[3])
p13, p13stat = poly.polyfit(fit[0],fit[1],13,full=True,w=fit[3])
p14, p14stat = poly.polyfit(fit[0],fit[1],14,full=True,w=fit[3])
p15, p15stat = poly.polyfit(fit[0],fit[1],15,full=True,w=fit[3])

print (p3)
print (p3stat) 

ffit1=poly.Polynomial(p1)
ffit2=poly.Polynomial(p2)
ffit3=poly.Polynomial(p3)
ffit4=poly.Polynomial(p4)
ffit5=poly.Polynomial(p5)
ffit6=poly.Polynomial(p6)
ffit7=poly.Polynomial(p7)
ffit8=poly.Polynomial(p8)
ffit9=poly.Polynomial(p9)
ffit10=poly.Polynomial(p10)
ffit11=poly.Polynomial(p11)
ffit12=poly.Polynomial(p12)
ffit13=poly.Polynomial(p13)
ffit14=poly.Polynomial(p14)
ffit15=poly.Polynomial(p15)

radius1=0
radius2=0
radius3=0
radius4=0
radius5=0
radius6=0
radius7=0
radius8=0
radius9=0
radius10=0
radius11=0
radius12=0
radius13=0
radius14=0
radius15=0

try:
 radius1=sqrt(-6*p1[1]/p1[0])
 radius2=sqrt(-6*p2[1]/p2[0])
 radius3=sqrt(-6*p3[1]/p3[0])
 radius4=sqrt(-6*p4[1]/p4[0])
 radius5=sqrt(-6*p5[1]/p5[0])
 radius6=sqrt(-6*p6[1]/p6[0])
 radius7=sqrt(-6*p7[1]/p7[0])
 radius8=sqrt(6*p8[1]/p8[0])
 radius9=sqrt(-6*p9[1])
 radius10=sqrt(-6*p10[1])
 radius11=sqrt(-6*p11[1])
 radius12=sqrt(-6*p12[1])
 radius13=sqrt(-6*p13[1])
 radius14=sqrt(-6*p14[1])
 radius15=sqrt(-6*p15[1])
except:
 print ("negative radius!")

ttt1=p1stat[0]+0.
ttt2=p2stat[0]+0.
ttt3=p3stat[0]+0.
ttt4=p4stat[0]+0.
ttt5=p5stat[0]+0.
ttt6=p6stat[0]+0.
ttt7=p7stat[0]+0.
ttt8=p8stat[0]+0.
ttt9=p9stat[0]
ttt10=p10stat[0]
ttt11=p11stat[0]
ttt12=p12stat[0]
ttt13=p13stat[0]
ttt14=p14stat[0]
ttt15=p15stat[0]

print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius1,ttt1[0]))
print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius2,ttt2[0]))
print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius3,ttt3[0]))
print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius4,ttt4[0]))
print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius5,ttt5[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius6,ttt6[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius7,ttt7[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius8,ttt8[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius9,ttt9[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius10,ttt10[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius11,ttt11[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius12,ttt12[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius13,ttt13[0]))

p1, p1stat = poly.polyfit(fit[0],fit[1],1,full=True)
p2, p2stat = poly.polyfit(fit[0],fit[1],2,full=True)
p3, p3stat = poly.polyfit(fit[0],fit[1],3,full=True)
p4, p4stat = poly.polyfit(fit[0],fit[1],4,full=True)
p5, p5stat = poly.polyfit(fit[0],fit[1],5,full=True)
p6, p6stat = poly.polyfit(fit[0],fit[1],6,full=True)
p7, p7stat = poly.polyfit(fit[0],fit[1],7,full=True)
p8, p8stat = poly.polyfit(fit[0],fit[1],8,full=True)
p9, p9stat = poly.polyfit(fit[0],fit[1],9,full=True)
p10, p10stat = poly.polyfit(fit[0],fit[1],10,full=True)
p11, p11stat = poly.polyfit(fit[0],fit[1],11,full=True)
p12, p12stat = poly.polyfit(fit[0],fit[1],12,full=True)
p13, p13stat = poly.polyfit(fit[0],fit[1],13,full=True)
p14, p14stat = poly.polyfit(fit[0],fit[1],14,full=True)
p15, p15stat = poly.polyfit(fit[0],fit[1],15,full=True)

ffit1=poly.Polynomial(p1)
ffit2=poly.Polynomial(p2)
ffit3=poly.Polynomial(p3)
ffit4=poly.Polynomial(p4)
ffit5=poly.Polynomial(p5)
ffit6=poly.Polynomial(p6)
ffit7=poly.Polynomial(p7)
ffit8=poly.Polynomial(p8)
ffit9=poly.Polynomial(p9)
ffit10=poly.Polynomial(p10)
ffit11=poly.Polynomial(p11)
ffit12=poly.Polynomial(p12)
ffit13=poly.Polynomial(p13)
ffit14=poly.Polynomial(p14)
ffit15=poly.Polynomial(p15)

radius1=0
radius2=0
radius3=0
radius4=0
radius5=0
radius6=0
radius7=0
radius8=0
radius9=0
radius10=0
radius11=0
radius12=0
radius13=0
radius14=0
radius15=0

try:
 radius1=sqrt(-6*p1[1]/p1[0])
 radius2=sqrt(-6*p2[1]/p2[0])
 radius3=sqrt(-6*p3[1]/p3[0])
 radius4=sqrt(-6*p4[1]/p4[0])
 radius5=sqrt(-6*p5[1]/p5[0])
 radius6=sqrt(-6*p6[1]/p6[0])
 radius7=sqrt(-6*p7[1]/p7[0])
 radius8=sqrt(6*p8[1]/p8[0])
 radius9=sqrt(-6*p9[1])
 radius10=sqrt(-6*p10[1])
 radius11=sqrt(-6*p11[1])
 radius12=sqrt(-6*p12[1])
 radius13=sqrt(-6*p13[1])
 radius14=sqrt(-6*p14[1])
 radius15=sqrt(-6*p15[1])
except:
 print ("negative radius!")

ttt1=p1stat[0]+0.
ttt2=p2stat[0]+0.
ttt3=p3stat[0]+0.
ttt4=p4stat[0]+0.
ttt5=p5stat[0]+0.
ttt6=p6stat[0]+0.
ttt7=p7stat[0]+0.
ttt8=p8stat[0]+0.
ttt9=p9stat[0]
ttt10=p10stat[0]
ttt11=p11stat[0]
ttt12=p12stat[0]
ttt13=p13stat[0]
ttt14=p14stat[0]
ttt15=p15stat[0]

print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius1,ttt1[0]))
print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius2,ttt2[0]))
print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius3,ttt3[0]))
print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius4,ttt4[0]))
print ('{0:.3f} fm with a total chi2 {1:3f}'.format(radius5,ttt5[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius6,ttt6[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius7,ttt7[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius8,ttt8[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius9,ttt9[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius10,ttt10[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius11,ttt11[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius12,ttt12[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius13,ttt13[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius14,ttt14[0]))
print ('{0:.3f} fm with a total chi2 {1:10}'.format(radius15,ttt15[0]))

#
# Rational Fraction Fits 
#

popt, pcov = curve_fit(func, fit[0], fit[1])
print ("popt = ",popt)

#
# Make Charge Form Factor Plot
#
plt.rcParams['font.size'] = 16
plt.rcParams['axes.labelsize'] = 18
plt.figure(figsize=(14,8))
lll=np.unique(nam)
count=0
for l in lll:
    count=count+1
#    if l != "Carlson" and l !="Berneaur Polynomial":
    if l != "Berneaur Polynomial":
       sss=loadarray2(filename,l)
       plt.errorbar(sss[0],sss[1],xerr=0,yerr=sss[2],marker='o',label=l,linestyle="none")
q2r=np.linspace(0,30,3000)
#plt.plot(q2r,ffit2(q2r), label="Quadratic Fit of Hand Data",color="blue",zorder=0)
plt.plot(q2r,dd(q2r), label="Doug 0.84fm Dipole",color="black",zorder=10)
plt.plot(q2r,sd(q2r), label="Standard 0.81fm Dipole",color="lime",zorder=0)
plt.plot(q2r,jan(q2r/25.7), label="Jan 0.88fm Polynomial",color="red",zorder=10)
#plt.plot(q2r,dl(q2r), label="Linear 0.84fm Function",color="blue",zorder=10)
#plt.plot(q2r,jl(q2r), label="Linear 0.88fm Function",color="red",zorder=0)
#plt.plot(q2r,ffit2(q2r), label="Fit Function",color="orange",zorder=0)
plt.plot(q2r, func(q2r, *popt), 'r-', label='Rational Function Fit',color="green",zorder=10)
plt.xlim(0,3.1)
plt.ylim(0.7,1.0)
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
ax.legend(new_handles, labels,loc=0)
#plt.legend(loc=1)
plt.tight_layout()
#plt.yscale('log')
#plt.xscale('log')
plt.show()

#
# Next Plot
#
plt.rcParams['font.size'] = 16
plt.rcParams['axes.labelsize'] = 18
plt.figure(figsize=(14,8))
plt.plot(q2r,(jan(q2r/25.7)-sd(q2r))/sd(q2r),label='Jan',zorder=10)
plt.plot(q2r,(dd(q2r)-sd(q2r))/sd(q2r),label='Doug',zorder=10)
plt.plot(q2r,(func(q2r,*popt)-sd(q2r))/sd(q2r),color="blue",zorder=10,label='Rational Func. Fit')
plt.plot(q2r,zero(q2r),color='black',zorder=10)
#plt.plot(q2r,(dd(q2r)-sd(q2r))/sd(q2r),color="black",zorder=10)
plt.xlim(0.,30)
plt.ylim(-0.5,0.5)
lll=np.unique(nam)
count=0
for l in lll:
    count=count+1
    if l != "Carlson" and l !="Berneaur Polynomial":
#    if l !="Berneaur Polynomial":
       loadratio(filename,l)

plt.tight_layout()
plt.legend(loc=0)
plt.show()

q2r=np.linspace(0,1,1000)

plt.rcParams['font.size'] = 16
plt.rcParams['axes.labelsize'] = 18
plt.xlabel("Q$^2$ [GeV$^{2}$]")
plt.figure(figsize=(14,8))
plt.ylabel("Jan FF Cross / SD FF Cross")
plt.xlim(0.,25)
plt.ylim(0.85,1.05)
plt.plot(q2r,(jan(q2r/25.7)**2+q2r/4/0.938/0.938*(jam(q2r/25.7)**2))/(sd(q2r)**2+q2r/4/0.938/0.938*(sd(q2r))),label='Jan Espilon = 1',zorder=10)
plt.plot(q2r,(0.5*((jan(q2r/25.7))**2)+q2r/4/0.938/0.938*(jam(q2r/25.7)**2))/(0.5*((sd(q2r))**2)+q2r/4/0.938/0.938*(sd(q2r))),label='Jan Espilon = 0.5',zorder=10)
plt.plot(q2r,(0.25*((jan(q2r/25.7))**2)+q2r/4/0.938/0.938*(jam(q2r/25.7)**2))/(0.25*((sd(q2r))**2)+q2r/4/0.938/0.938*(sd(q2r))),label='Jan Espilon = 0.25',zorder=10)
plt.plot(q2r,(q2r/4/0.938/0.938*(jam(q2r/25.7)**2))/(q2r/4/0.938/0.938*(sd(q2r))),label='Jan Espilon = 0',zorder=10)
plt.tight_layout()
plt.legend(loc=0)
plt.show()

#
# Exit
#
raise SystemExit()
