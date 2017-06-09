#
# Example of Fitting the 1963 Hand Data Using GNUPLOT
# by Douglas Higinbotham
#
set terminal wxt font 'Verdana,14' size 1200,600
#
# Data Files
# -----------
# Yount.dat
# Lehmann.dat
# Drickey.dat
# Bumiller
#
# using a system call to cat the ASCII data files together
#
system 'cat Lehmann.dat Drickey.dat Yount.dat Bumiller.dat > all.dat'
#
# Standard Functions
# ------------------
#
sd(x)=(1+0.1100/2*x)**(-2) # 0.81fm Standard Dipole
dd(x)=(1+0.1176/2*x)**(-2) # 0.84fm doug Dipole
#
# Determine Hand's A Parameter
# ---------------------------- 
#
set xrange [0:3]
f(x)=1+f1*x+A*x**2
fit f(x) 'all.dat' using 1:2:3 yerrors via f1,A
#
# Fit Low Q2 Using A Parameter 
# ----------------------------
#
set xrange [0:1.05]
g(x)=1+g1*x+A*x**2
fit g(x) 'all.dat' using 1:2:3 yerrors via g1
print 'using all.dat file with cut',g1
#
# Make Nice Plot of the Results
# -----------------------------
set xrange [0:1.1]
set yrange [0.85:1.0]
#
#
set xlabel 'Q^2 [fm^{-2}]'
set ylabel 'G_E'
#
plot \
     'Yount.dat'   using 1:2:3 with yerrorbars lw 2 title 'Yount', \
     'Lehmann.dat' using 1:2:3 with yerrorbars lw 2 title 'Lehmann', \
     'Drickey.dat' using 1:2:3 with yerrorbars lw 2 title 'Drickey', \
     'Bumiller.dat' using 1:2:3 with yerrorbars lw 2 title 'Bumiller', \
     sd(x) lw 2 lc 'green' title 'Standard 0.81fm Dipole', \
     dd(x) lw 2 lc 'red' title 'Doug 0.84fm Dipole', \
     g(x)  lw 2 lc 'blue' title 'Hand Quadratic Fit' 
#
# Print to screen the proton radius from this fit.
#
print sqrt(-6*g1),'is my value of the proton using the 1963 radius extraction proceedure.'
#
pause -1
#
