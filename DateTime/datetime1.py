import datetime

date = datetime.date(2025, 11, 2) # we will access datetime module call the date() method and assigning it to date object
# we are passing arguments (year, month, day)
today = datetime.date.today() # module(datetime).class(date).method(today())
time = datetime.time(12,30,0) # module(datetime).method(time) we have pass arguments as hr,min, secs
print(time)
print(today)
print(date)

################################
# To display current date and time....

now = datetime.datetime.now() # module(datetime), class(datetime), method(now())
print(now)

now = now.strftime("%H:%M:%S %m-%d-%Y ")
print(now)