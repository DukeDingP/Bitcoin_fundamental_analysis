import datetime
now = datetime.datetime.now()
delta = datetime.timedelta(days=3)
n_days = now + delta
print(n_days.strftime('%Y-%m-%d'))  #data-str

#str-date
t_str = '2012/03/05'
d = datetime.datetime.strptime(t_str, '%Y/%m/%d')
delta = datetime.timedelta(days=3)
n_days = d + delta
print(n_days.strftime('%Y/%m/%d'))  #data-str
print(d)

