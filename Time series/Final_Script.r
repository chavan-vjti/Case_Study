#Set the working directory where CSV/data file is located
#Upload the required packages
library(forecast)
library(tseries)

#Read the CSV file in R object
import_values <- read.csv("import values.csv")

#Print first few observations
head(import_values)
attach(import_values)

#Review the summary of required data
summary(import)

#Plot the import values
plot(import)    #Non stationary data

#Perform first order differencing to convert data to stationary
d.import <- diff(import)
plot(d.import)
summary(d.import)

#Augmented Dicky Fuller test for p-value
adf.test(d.import, alternative = "stationary")

#Lookf acf and pacf plots
acf(d.import)
pacf(d.import)
auto.arima(d.import)

#Model application
arima(d.import, order=c(4,0,3))
#arima(import, order=c(4,1,3))

#Store the result in an object
arima.final <- arima(d.import, order=c(4,0,3))
tsdiag(arima.final)

#Forecasting using final model
arima.final <- arima(import, order = c(4,1,3))
summary(arima.final)
predicted <- forecast(arima.final, h=2976, level = c(90,95))
