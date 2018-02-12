#getwd() will give you the current working directory
#To set the working directory, go to Sessions -> Select Working Directory -> Choose Directory
#Browse for the appropriate directory
#To read the csv file, data<- read.csv("import values.csv", head=TRUE)
# to get any column, print(data$import)

#Before executing this script it is very important to set the working directory where
#CSV file is located 

#install.packages(forecast)
library(tseries)
library(forecast)
GEPLkw<-read.csv("import values.csv", head = TRUE)
summary(GEPLkw)
head(GEPLkw)
tail(GEPLkw)
options(max.print = 420000)  #This is to set the limit on your data
GEPLkw

plot(GEPLkw$import)
locator()

selectPt <- fhs(givenData)
acf(input_data$import)
pacf(input_data$import)
dimport<-diff(input_data$import)
plot(dimport, xlab = "Time", ylab = "Out")
dimport
#print dimport[1]
input_data1<-ts(input_data$import, frequency = 5)
options(max.print = 42000)
#input_data1<-ts(input_data1$import, frequency = 5)
input_data1
