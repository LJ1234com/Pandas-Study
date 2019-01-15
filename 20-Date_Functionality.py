import pandas as pd

######################### Time Series #####################
## Get Current Time
print(pd.datetime.now())

## Create a TimeStamp
print(pd.Timestamp('2017-03-01'))
print(pd.Timestamp(1587687255,unit='s'))

## Create a Range of Time
print(pd.date_range("11:00", "13:30", freq="30min").time)

## Converting to Timestamps
print(pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])))
print(pd.to_datetime(['2005/11/23', '2010.12.31', None]))


## Create a Range of Dates
print(pd.date_range('1/1/2011', periods=5))


## Change the Date Frequency
print(pd.date_range('1/1/2011', periods=5,freq='M'))

## bdate_range
print(pd.date_range('1/1/2011', periods=5))

start = pd.datetime(2011, 1, 1)
end = pd.datetime(2011, 1, 5)
print(pd.date_range(start, end))

## Offset Aliases
