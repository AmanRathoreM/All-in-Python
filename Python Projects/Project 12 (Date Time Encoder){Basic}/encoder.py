'''
Date ->          2021-12-11
Time ->          15:42:48
Day ->           Saturday
Month Name ->    December
Unix Time ->     1639217568
File Name ->     "encoder.py" when created i.e. on 2021-12-11
File Path ->     "C:/Google Drive/Programming/Python/Python tp Projects/Project 12 (Date Time Encoder){Basic}/encoder.py" when created i.e. on 2021-12-11

This is a date encoder
'''

import string
# from time import strftime as dt
from datetime import datetime as dt

alphabets_list = list(string.ascii_uppercase)


class DateTime_Encoder():
    '''This class can be used to encode or decode time
    '''

    def __init__(self, List_of_DateTime):
        '''Feed your date-time list to it to initialize date-time

        Args:
            List_of_DateTime ([type]): [description]

        Raises:
            TypeError: If list is not passed as an argument or the length of list is != 6
        '''
        if not((type(List_of_DateTime) == list) and (len(List_of_DateTime) == 6)):
            raise TypeError(
                "Not a valid format or indices! Please re-check your provided time it must be in this format ['Year', 'Month', 'Date', 'Hour(in 24 hr format)', 'Minutes', 'Seconds']")
        self.List_of_DateTime = List_of_DateTime
        del List_of_DateTime

    def second_round_off(self, sec):
        if sec == 0:
            sec = 1
        if not sec % 3:
            return sec

        sec = sec+(3-(sec % 3))
        return sec

    def second_encoder(self, sec):
        '''Encodes Seconds

        Args:
            sec (int): Seconds you need to encode

        Returns:
            char: Encoded form of seconds, it's value varies from (A to T) if right argument is provided
        '''
        return alphabets_list[int(self.second_round_off(sec)/3)-1]

    def minute_encoder(self, min):
        '''Encodes Minute

        Args:
            min (int): Minute you need to encode

        Returns:
            str: Encoded form of Minute, it's value varies from (00 to 60) if right argument is provided
        '''
        if min <= 9:
            return str('0'+str(int(min)))
        return str(min)

    def hour_encoder(self, hr):
        '''Encodes Hour

        Args:
            hr (int): Hour you need to encode

        Returns:
            char: Encoded form of Hour
        '''
        if hr <= 9:
            return hr
        return alphabets_list[(hr-9)-1]

    def day_encoder(self, day):
        '''Encodes Day

        Args:
            day (int): Day you need to encode

        Returns:
            char: Encoded form of Day
        '''
        if day <= 9:
            return day
        return alphabets_list[(day-9)-1]

    def month_encoder(self, month):
        '''Encodes Month

        Args:
            month (int): Month you need to encode

        Returns:
            char: Encoded form of Month
        '''
        return alphabets_list[month-1]

    def year_encoder(self, year):
        '''Encodes Year

        Args:
            Year (int): Years you need to encode

        Returns:
            hex: Encoded form of year
        '''
        year = year-2020

        # if year <= 9:  # * till year 2029 year
        #     return year
        # elif year <= 35:  # * till year 2055
        #     return alphabets_list[(year-9)-1]

        return (str(hex(year))[2:]).upper()

    @property
    def full_encoded_date_time_from_datetime(self):
        '''Full date-time Encoder

        Args:
            datetime_list (list): A list of datetime in this format --> ['Year', 'Month', 'Date', 'Hour(in 24 hr format)', 'Minutes', 'Seconds']

        Returns:
            encoded_datetime: Encoded form of date and time
        '''

        datetime_list = self.List_of_DateTime

        encoded_datetime = str(self.year_encoder(
            int(datetime_list[0])))+str(self.month_encoder(int(datetime_list[1])))+str(self.day_encoder(int(datetime_list[2])))+str(self.hour_encoder(int(datetime_list[-3])))+str(self.minute_encoder(int(datetime_list[-2])))+str(self.second_encoder(int(datetime_list[-1])))

        return encoded_datetime

    """
    def full_encoded_date_time_from_unix_time(unix_time):
        '''Full date-time Encoder

        Args:
            datetime_list (list): A list of datetime in this format --> ['Year', 'Month', 'Date', 'Hour(in 24 hr format)', 'Minutes', 'Seconds']

        Returns:
            encoded_datetime: Encoded form of date and time
            
        '''

        datetime_list = str(dt.fromtimestamp(
            int(unix_time)).strftime("%Y-%m-%d-%H-%M-%S")).split("-")

        encoded_datetime = str(year_encoder(
            int(datetime_list[0])))+str(month_encoder(int(datetime_list[1])))+str(day_encoder(int(datetime_list[2])))+str(hour_encoder(int(datetime_list[-3])))+str(minute_encoder(int(datetime_list[-2])))+str(second_encoder(int(datetime_list[-1])))

        return encoded_datetime
    """


if __name__ == "__main__":

    unix_time = 1639237368
    List_of_DateTime = str(dt.fromtimestamp(
        int(unix_time)).strftime("%Y-%m-%d-%H-%M-%S")).split("-")

    # 1639237368 = P12LBL1

    List_of_DateTime = [2021, 12, 11, 15, 42, 48]

    ec = DateTime_Encoder(List_of_DateTime)
    print(ec.full_encoded_date_time_from_datetime)
    ec2 = DateTime_Encoder([2021, 12, 11, 00, 42, 5])
    print(ec2.full_encoded_date_time_from_datetime)
