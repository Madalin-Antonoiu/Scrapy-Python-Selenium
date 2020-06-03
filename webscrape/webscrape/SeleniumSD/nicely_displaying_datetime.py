import datetime

x = datetime.datetime.now()
formatted = "%a, %d-%m-%Y, at %H:%M"
date_time = x.strftime(formatted)
print(date_time)