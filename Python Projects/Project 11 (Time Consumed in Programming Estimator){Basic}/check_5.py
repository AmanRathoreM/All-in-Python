import time


# * Year,Month,Day,Date,Proper Date,Time,Unix Time,Epoch time(tm_year),Epoch time(tm_mon),Epoch time(tm_mday),Epoch time(tm_hour),Epoch time(tm_min),Epoch time(tm_sec),Epoch time(tm_wday),Epoch time(tm_yday),Epoch time(tm_isdst),Time Zone,Time Zone Name,Type (Starting or Ending)

#! header = "Year,Month,Day,Date,Proper Date,Time,Unix Time,Epoch time(tm_year),Epoch time(tm_mon),Epoch time(tm_mday),Epoch time(tm_hour),Epoch time(tm_min),Epoch time(tm_sec),Epoch time(tm_wday),Epoch time(tm_yday),Epoch time(tm_isdst),Time Zone,Time Zone Name,Type (Starting or Ending)"

# * tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0

Year = time.strftime("%Y")
Month = time.strftime("%B")
Day = time.strftime("%A")
Date = time.strftime("%d")
Proper_Date = time.strftime("%d:%m:%Y")
Time = time.strftime("%H:%M:%S")
Unix_Time = time.time()
Epoch_time_tm_year = time.gmtime(0)[0]
Epoch_time_tm_mon = time.gmtime(0)[1]
Epoch_time_tm_mday = time.gmtime(0)[2]
Epoch_time_tm_hour = time.gmtime(0)[3]
Epoch_time_tm_min = time.gmtime(0)[4]
Epoch_time_tm_sec = time.gmtime(0)[5]
Epoch_time_tm_wday = time.gmtime(0)[6]
Epoch_time_tm_yday = time.gmtime(0)[7]
Epoch_time_tm_isdst = time.gmtime(0)[8]
Time_Zone = time.strftime("%z")
Time_Zone_Name = time.strftime("%Z")
Type_Starting_or_Ending = "None"

# print(time.gmtime(0))

with open('check5.csv', 'a', encoding='UTF8') as file:
    data = f"{Year},{Month},{Day},{Date},{Proper_Date},{Time},{Unix_Time},{Epoch_time_tm_year},{Epoch_time_tm_mon},{Epoch_time_tm_mday},{Epoch_time_tm_hour},{Epoch_time_tm_min},{Epoch_time_tm_sec},{Epoch_time_tm_wday},{Epoch_time_tm_yday},{Epoch_time_tm_isdst},{Time_Zone}, {Time_Zone_Name}, {Type_Starting_or_Ending}\n"

    file.write(data)
