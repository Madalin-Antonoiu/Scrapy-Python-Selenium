import timeago, datetime

now = datetime.datetime.now();
#date = '27.05.2020 11:17'
#


date_time_str1 = '27/05/2020 12:17 PM'
#format = '%Y-%m-%d %H:%M %p'

date_time_obj = datetime.datetime.strptime(date_time_str1, '%d/%m/%Y %I:%M %p')


print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)

print(timeago.format(date_time_obj, now))