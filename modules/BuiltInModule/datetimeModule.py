# datetime module
import datetime

# returns current date time 
currentDateTime = datetime.datetime.now()
print(currentDateTime)

print("month in short:",currentDateTime.strftime("%b"))
print("month full name:",currentDateTime.strftime("%B"))
print("month in number:",currentDateTime.strftime("%m"))
print("year in short:",currentDateTime.strftime("%y"))
print("year full:",currentDateTime.strftime("%Y"))
print("hour (00-23):",currentDateTime.strftime("%H"))
print("hour (00-11):",currentDateTime.strftime("%I"))
print("am/pm:",currentDateTime.strftime("%p"))
print("minutes (00-59):",currentDateTime.strftime("%M"))

# create date object
date = datetime.datetime(2024,6,25)
print(date)