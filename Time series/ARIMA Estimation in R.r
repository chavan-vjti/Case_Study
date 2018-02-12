#forecast package should be installed
#know the path of working directory
Library(forecast)

#set working directory
setwd("D://Siddhesh's Data//OpenCV Sentdex//Case_Study//Time series")

#import data
inf_data <- read.csv("UKCPI.csv")
inf_data$UKCPI <- ts(inf_data$UKCPI, start=c(1998,1), end=c(2015,4), frequency=4) #4 stands for quarterly data
summary(inf_data)	#prints the summary of data

#Inflation of index
#dUKCPI <- diff(inf_data$UKCPI)
dUKCPI<-diff(inf_data,4)	#this creates year on year (4 quarter differences)

plot(dUKCPI)

#Estimating AR model
fit_diff_ar <- arima(dUKCPI, order=c(1,0,0))	#Arima model is part of forecast package
summary(fit_diff_ar)

#forecating
fit_diff_arf <- forecast(fit_diff_ar, h=12) #12 quarters, 3 years of data
plot(forecast(fit_diff_ar, h=12), inclue=20)	#includes last 20 years of data


