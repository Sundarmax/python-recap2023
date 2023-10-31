import datetime
from datetime import date # import date alone
from datetime import time
from datetime import timedelta,datetime

def get_current_time():
    curr_date_time = datetime.datetime.now()
    print(curr_date_time)
    # get current date
    curr_date = datetime.date.today()
    print(curr_date)
    # get current time alone
    curr_time = datetime.time()
    print(curr_time)

def create_datetime_object():
    # datetime(year, month, day, hour, minute, second, microsecond)
    b = datetime.datetime(2022, 12, 28, 23, 55, 59, 342380)
    print(b)

def create_date_obejct():
    date_obj = datetime.date(2023,12,8)
    print(type(date_obj), date_obj)
    # get today date
    print(date.today())
    # get date from timestamp
    date_obj2 = date.fromtimestamp(1326244364)
    print(date_obj2)

def create_time_object():
    a = time(8,15,21) # # time(hour = 0, minute = 0, second = 0)
    print(a)
    print("Hour =", a.hour)
    print("Minute =", a.minute)
    print("Second =", a.second)
    print("Microsecond =", a.microsecond)

def get_year_month_day():
    today = date.today()
    print(dir(today)) # supported attributes
    print("Current year:", today.year)
    print("Current month:", today.month)
    print("Current day:", today.day)


def create_timedelta_object():
    # use date or datetime object to find diff of them
    # t1 = date(2018,7,12)
    # t2 = date(2017,12,23)
    # t3 = t1 - t2
    # print(t3,type(t3))
    t3  = timedelta(weeks=2, days=5, hours=1, seconds=33)
    t4  = timedelta(weeks=0, days=10, hours=2, seconds=0)
    t5 = t3 - t4
    print(t5)

def strftime_func():
    now = datetime.now()
    d = now.strftime("%m%d%Y")
    t = now.strftime("%H:%M:%S")
    print("date : ", d,type(d))
    print("time : ", t,type(t))

def strptime_func():
    # use striptime to create date object
    date_string = "21 June, 2023"
    date_object = datetime.strptime(date_string, "%d %B, %Y")
    print(date_object)

#get_current_time()
#create_date_obejct()
#get_year_month_day()
#create_time_object()
#create_datetime_object()
#create_timedelta_object()
# #strftime_func()
strptime_func()