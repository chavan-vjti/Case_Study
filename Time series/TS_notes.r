#importing data in R
> data<-read.csv("C:/Users/Siddhesh/Desktop/AnalyticsUniversity/death_age.csv")

#converting it into time series
> datats <- ts(data)

#Plotting the time series
> plot.ts(datats)

#Plotting the ACF and PACF of the time series
> acf <- acf(datats, lag.max = 20)
> pacf <- pacf (datats, lag.max = 20)

#plot the ACF and PACF for best model selection
> fit <- auto.arima(datats)

#ARIMA (0,0,0) is the best fit
#coefficient intercept = 53.7085

#Diagnostic plot
> tsdiag(fit)

#forecasting
> library(forecast)	#package installation
> fc <- forecast.Arima(fit, h=10)	#forecast for 10 years
> plot.forecast(fc)

> plot.ts(fc$residuals)
> residual<-resid(fit)
> hist(residual)
