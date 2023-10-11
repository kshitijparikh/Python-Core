import datetime

x = datetime.datetime.now()
print(type(x))
print("Date_Time =", x)

y = datetime.datetime(2012, 2, 13)
print(y)

print("Time =", x.time())
print("Date =", x.date())
print("Current Date & Time =", x.now())
print("Maximum Date & Time =", x.max)
print("Minimum Date & Time =", x.min)
print("Date & Time + Timezone =", x.astimezone())
print("Day as Month =", x.day)
print("Month =", x.month)
print("Year =", x.year)
print("Hour =", x.hour)
print("Minute =", x.minute)
print("Second =", x.second)
print("Microsecond =", x.microsecond)
print("Time Zone Information =", x.tzinfo)
print("Class Type =", x.__class__)

"""
%Y: Year with century as a decimal number (e.g., "2023").
%y: Year without century as a zero-padded decimal number (e.g., "23" for 2023).
%m: Month as a zero-padded decimal number (e.g., "03" for March).
%d: Day of the month as a zero-padded decimal number (e.g., "05" for the 5th day).
%H: Hour (24-hour clock) as a zero-padded decimal number (e.g., "08" for 8 AM).
%I: Hour (12-hour clock) as a zero-padded decimal number (e.g., "08" for 8 AM or PM).
%M: Minute as a zero-padded decimal number (e.g., "07" for 7 minutes past the hour).
%S: Second as a zero-padded decimal number (e.g., "09" for 9 seconds past the minute).
%f: Microsecond as a decimal number (e.g., "123456").
%p: AM or PM designation (e.g., "AM" or "PM").
%A: Full weekday name (e.g., "Monday").
%a: Abbreviated weekday name (e.g., "Mon").
%B: Full month name (e.g., "March").
%b: Abbreviated month name (e.g., "Mar").
%c: Locale's appropriate date and time representation (e.g., "Tue Mar 5 08:07:09 2023").
%x: Locale's appropriate date representation (e.g., "03/05/23").
%X: Locale's appropriate time representation (e.g., "08:07:09").
"""

print("Year in 4 digits =", x.strftime("%Y"))
print("Year in last 2 digits =", x.strftime("%y"))
print("Moth in zero-padded number =", x.strftime("%m"))
print("Day of month in zero-padded number =", x.strftime("%d"))
print("Hour(24) in zero-padded number =", x.strftime("%H"))
print("Hour(12) in zero-padded number =", x.strftime("%I"))
print("Minutes in zero-padded number =", x.strftime("%M"))
print("Second in zero-padded number =", x.strftime("%S"))
print("Microsecond in number =", x.strftime("%f"))
print("AM or PM =", x.strftime("%p"))
print("Full weekday name =", x.strftime("%A"))
print("Abbreviated weekday name =", x.strftime("%a"))
print("Full month name =", x.strftime("%B"))
print("Abbreviated month name", x.strftime("%b"))
print("Locale's appropriate date and time representation =", x.strftime("%c"))
print("Locale's appropriate date representation =", x.strftime("%x"))
print("Locale's appropriate time representation =", x.strftime("%X"))