# Date 06-10-2021

try:
    import time
    from datetime import datetime
    import pandas as pd

    main_csv = pd.read_csv("anylasis_of_time_consumed_in_programming.csv", usecols=[
        "Proper Date", "Time"]).tail(2)

    # * Year,Month,Day,Date,Proper Date,Time,Unix Time,Epoch time(tm_year),Epoch time(tm_mon),Epoch time(tm_mday),Epoch time(tm_hour),Epoch time(tm_min),Epoch time(tm_sec),Epoch time(tm_wday),Epoch time(tm_yday),Epoch time(tm_isdst),Time Zone,Time Zone Name,Type (Starting or Ending)

    print("Welcome to our Time Analysis Programe\n")

    programming_started = main_csv.iat[-1, 1]
    # programming_done_for_how_much_time = str(datetime.strptime(
    #     main_csv.iat[-1, 1], "%H:%M:%S") - datetime.strptime(main_csv.iat[-2, 1], "%H:%M:%S"))
    Last_time_ended_programming_date = main_csv.iat[-1, 0]
    Last_time_ended_programming_time = main_csv.iat[-1, 1]

    with open("info_regarding_previous_use.txt", 'r')as previous_use:
        if previous_use.read() == 's':
            choice = 'e'

        else:
            choice = 's'

    Year = time.strftime("%Y")
    Month = time.strftime("%B")
    Day = time.strftime("%A")
    Date = time.strftime("%d")
    Proper_Date = time.strftime("%d:%m:%Y")
    Time = time.strftime("%H:%M:%S")
    Unix_Time = int(time.time())
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

    if choice == 'e':
        print("I\'ll End your Programming time\n")

        Type_Starting_or_Ending = "Ending"
        with open("info_regarding_previous_use.txt", 'w')as previous_use:
            previous_use.write('e')

        with open("anylasis_of_time_consumed_in_programming.csv", 'a')as main_file:
            data = f"{Year},{Month},{Day},{Date},{Proper_Date},{Time},{Unix_Time},{Epoch_time_tm_year},{Epoch_time_tm_mon},{Epoch_time_tm_mday},{Epoch_time_tm_hour},{Epoch_time_tm_min},{Epoch_time_tm_sec},{Epoch_time_tm_wday},{Epoch_time_tm_yday},{Epoch_time_tm_isdst},{Time_Zone}, {Time_Zone_Name}, {Type_Starting_or_Ending}\n"

            main_file.write(data)

        main_csv = pd.read_csv("anylasis_of_time_consumed_in_programming.csv", usecols=[
            "Proper Date", "Time"]).tail(2)
        programming_done_for_how_much_time = str(datetime.strptime(
            main_csv.iat[-1, 1], "%H:%M:%S") - datetime.strptime(main_csv.iat[-2, 1], "%H:%M:%S"))
        print(
            f"You had started Programming at {programming_started}\nYou had done programming for {programming_done_for_how_much_time}\nI'm ending it\n")

    else:  # * Choice is s

        print(
            f"I\'ll Start your Programming time\n\nLast time you had Ended doing programming on {Last_time_ended_programming_date} at {Last_time_ended_programming_time}\n")

        Type_Starting_or_Ending = "Starting"
        with open("info_regarding_previous_use.txt", 'w')as previous_use:
            previous_use.write('s')
        with open("anylasis_of_time_consumed_in_programming.csv", 'a')as main_file:
            data = f"{Year},{Month},{Day},{Date},{Proper_Date},{Time},{Unix_Time},{Epoch_time_tm_year},{Epoch_time_tm_mon},{Epoch_time_tm_mday},{Epoch_time_tm_hour},{Epoch_time_tm_min},{Epoch_time_tm_sec},{Epoch_time_tm_wday},{Epoch_time_tm_yday},{Epoch_time_tm_isdst},{Time_Zone}, {Time_Zone_Name}, {Type_Starting_or_Ending}\n"

            main_file.write(data)
except Exception as error_msg:
    print(error_msg)


input("Press \'Enter\' to Exit")
