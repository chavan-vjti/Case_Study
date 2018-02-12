#import_values <- read_excel("F:/Case_Study/Time series/import values.xlsx")
#setwd("F:/Case_Study/Time series")
install.packages("forecast")
input_data<-read.csv("import values.csv", head = TRUE)
head(input_data)
summary(input_data)
input_data
#options(max.print = 42000)
input_data
options(max.print = 420000)
input_data
plot(input_data$import)
locator(n=3)
adf.test(input_data$import, altenaively="stationary")
adf.test(input_data, altenaively="stationary")
adf.test(import, altenaively="stationary")
library(tseries)
adf.test(input_data, altenaively="stationary")
adf.test(input_data$import, altenaively="stationary")
adf.test(input_data$import, alternatively="stationary")
adf.test(import, alternatively="stationary")
adf.test(input_data$import, alternatively="stationary")
input_data
guess<-input_data$import
guess
plot(guess)
summary(guess)
library(forecast)
givenData <- read.csv("import values.csv")
givenData
library(tseries)
attach(givenData$import)
attach(givenData)
import
plot(import)
d.import <- diff(import)
summary(d.import)
summary(import)
var(d.import, y = NULL, na.rm = FALSE, use)
var(d.import)
var(import)
dd.import < diff(d.import)
dd.import <- diff(d.import)
var(dd.import)
acf(d.import)
pacf(d.import)
plot(d.import)
arima(d.import, order=c(1,0,1))
arima.final<-arima(d.import, c(1,0,1))
arima.final
tsdiag(final.arima)
tsdiag(arima.final)
arima.final<-arima(import, c(1,1,1))
arima.final
predicted<-predict(arima.final, n.head = 96*30)
predicted
predicted<-predict(arima.final, n.head = 2880)
predicted
forecasted<-forecast(arima.final, h=2880)
forecasted
View(forecasted)
forecasted[["x"]]
summary(forecasted)
summary(forecasted)
forecasted[["x"]]
View(forecasted)
View(predicted)
forecasted[["x"]]
forecasted[["method"]]
forecasted[["model"]]
forecasted[["level"]]
forecasted[["model"]]
forecasted[["model"]]
forecasted[["lower"]]
forecasted[["fitted"]]
