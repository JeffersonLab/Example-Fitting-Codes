  #
  # R Fitting Of Hand 1963 Data
  # by Douglas Weadon Higinbotham, Jefferson Lab
  #
  message("")
  message("R Fitting of Hand 1963 Data")
  message("")
  #
  # Load the car library for the ellipses.
  # Load the gplots library for text on plot
  #
  library(car)
  library(gplots)
  #
  # Read the data
  #
  data <- read.table("hand.dat", header=TRUE ,  col.names = c("x", "y", "dy"))
  #data <- read.table("data/Carl-norm.dat", header=TRUE ,  col.names = c("x", "y", "dy"))
  #
  message("")
  message("Data has been read.")
  message("")
  # 
  # Define the model with fixed intercept.
  #
  fwd.model <- lm(data$y - 1.0 ~ -1 + data$x + I(data$x^2), weight=1/data$dy^2)
  #fwd.model <- lm(data$y ~ data$x + I(data$x^2), weight=1/data$dy^2)
  #
  #  
  # 
  message("")
  message('Results of Fit')
  message("")
  print(summary(fwd.model))
  #
  # Plot the results and diagnostics 
  #
  par(mfrow=c(3,2))
  plot(data$x,data$y,xlab=expression('Q2 [GeV/c]'^{2}),ylab=expression('G'[E]),ylim=range(c(data$y-data$dy, data$y+data$dy)),mgp=c(2.0,1.0,0))
  arrows(data$x,data$y-data$dy, data$x, data$y+data$dy, length=0.05, angle=90, code=3)
  lines(data$x,predict(fwd.model)+1)
  plot(fwd.model, mgp=c(2.0,1.0,0))
  #
  # Plot Information About The Final Fit
  #
  textplot (capture.output(summary(fwd.model)), valign="top")
