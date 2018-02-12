#Once you read your data in X, follow followings steps
tail(X)
length(X)
#make correlograms
acf(X)	#acf plot gives number of MA term
pacf(X)	#pacf gives number of AR terms
#fir ARMA model
auto.arima(X)	#Automatically gives number of AR and MA terms
fit=arima(X, order = c(4,0,2))
fit_resid = residual(fit)
#Diagnostics check series correlation
Box.test(fit_resid, lag=10, type = "Ljung-Box")#p-value should be as low as possible

#forecast using the ARMA model
forecast_X=forecast(fit, h=20)	#estimate nest 20 models
#accuracy test
accuracy(forecast_X, currency[1687:1706,8])