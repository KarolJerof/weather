library(weatherData)
library(ggplot2)
library(scales)
library(plyr)

w2017 <- getWeatherForYear("sfo",2017)

FY2016 = getWeatherForDate("sfo", start_date = '2016-04-01', end_date = '2017-03-31', opt_detailed = TRUE)
n = dim(FY2016)[1]
k = dim(FY2016)[2]

dailyData = matrix(,nrow = n, ncol =1)
for (i in 1:n){
  print(i)
  tmp =  getDetailedWeather("sfo",FY2016$Date[i])
}

dailydata = getDetailedWeather("sfo",'2017-03-31')

w2013$shortdate <- strftime(w2013$Time, format="%m-%d")

meanTemp <- ddply(w2013, .(shortdate), summarize, mean_T=mean(TemperatureF))
meanTemp$shortdate <- as.Date(meanTemp$shortdate,format="%m-%d")

ggplot(meanTemp, aes(shortdate, mean_T)) + geom_line() +
  scale_x_date(labels=date_format("%m/%d")) + xlab("") + ylab("Mean Temp deg F") +
  ggtitle("2013 Average Daily Temperature at SFO")