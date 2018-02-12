#Data is a seasonal data
beer1 <- read.scv(file.choose(), header=TRUE)
#Plot it
plot(beer1,type="1") #its a seasonal pattern, this data is not stationary, differencing will convert series into stationary

#plot ACF and PACF on same graph, checking for stationary
par(mfrow=c(2,1))
acf(beer1$Production)
pacf(beer1$Production)

#Difference the series and plot it
dbeer1<- diff(beer1$Production)
ndifbeer1<- length(dbeer)
plot(1:ndifbeer1,dbeer1,type="1")

#plot ACF and PACF on same graph
par(mfrow=c(2,1))
acf(dbeer)
pacf(dbeer1)

#Fit the model
beer1.fit<-arima(beer1$Production,order=c(1,1,0),seasonal=linear(order=c(1,1,0),period=12),include.mean=FALSE)
beer1.fit #s.e Standard Error should be small
#Generate predictions
beer1.pred <- predict(beer1.fit, n.ahead=12)
plot(beer1, type="1", xlim=c(400,488),ylim=c(50,250))
lines(beer1.pred$pred, col="blue")
lines(beer1.pred$pred+2*beer1.pred$se, col="red")
lines(beer1.pred$pred-2*beer1.pred$se,col="red")
