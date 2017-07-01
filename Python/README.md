From page 347 of <a href="https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.35.335">L. Hand et al., Rev. Mod. Rphys. 35 (1963) 335</a> paper, one finds the following statement, "The accurate values of GE at low q2 enable us to
state the derivative (dGE/dq2) at q2 = 0 accurately.
We use the data in Table I q2 = 1.05 fm^{-2}. It is
neeessary to use a quadratic fit to GE = 1 - 1/6(r)q2 + Aq4 
using values of q2 up to 3 fm^{-2} to determine the
parameter A.   The data are quite consistent and we
deduce (dGE/dq ) at q2=0 is -0.108 & 0.003 fm^{-2}
where the rms radius of the proton is given by
(r) = 0.805 & 0.011 fm."

This Python code does exactly this.   First fitting the data
upto 3 fm^{-2} and then passing the parameter A to a second
fit upto 1.05 fm^{-2}.   Amusingly, this fits gives 0.853  +/-  0.018 fm
where the uncertainty is calculated from the covariance matrix.  

<img src="https://raw.githubusercontent.com/JeffersonLab/Example-Fitting-Codes/master/Python/output.pdf" width="1024">
