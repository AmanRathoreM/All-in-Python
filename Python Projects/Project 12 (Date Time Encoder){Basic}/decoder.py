"""
Date ->          2021-12-12
Time ->          14:10:10
Day ->           Sunday
Month Name ->    December
Unix Time ->     1639298410
File Name ->     "decoder.py" when created i.e. on 2021-12-12
File Path ->     "C:/Google Drive/Programming/Python/Python tp Projects/Project 12 (Date Time Encoder){Basic}/decoder.py" when created i.e. on 2021-12-12

This is a date decoder
"""

import string
# from time import strftime as dt
from datetime import datetime as dt

alphabets_list = list(string.ascii_uppercase)


class DateTime_Decoder():
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

    def second_round_off(self, sec):
        if sec == 0:
            sec = 1
        if not sec % 3:
            return sec

        sec = sec+(3-(sec % 3))
        return sec

    def second_decoder(self, en_sec):
        '''Encodes Seconds

        Args:
            en_sec (int): Encoded Second you need to decode

        Returns:
            int: Decoded form of second, it's value varies from (00 to 60) if right argument is provided
        '''
        return (alphabets_list.index(str(en_sec))+1)*3
        # return alphabets_list[int(self.second_round_off(sec)/3)-1]

    def minute_decoder(self, en_min):
        '''Decodes Minute

        Args:
            en_min (int): Minute you need to decode

        Returns:
            str: Decoded form of Minute, it's value varies from (00 to 59) if right argument is provided
        '''
        return str(en_min)

    def hour_decoder(self, en_hr):
        '''Decodes Hour

        Args:
            en_hr (char): Hour you need to decode

        Returns:
            int: Decoded form of Hour
        '''
        try:
            en_hr = int(en_hr)
            return en_hr
        except:
            return alphabets_list.index(en_hr)+10

    def day_decoder(self, en_day):
        '''Decodes Day

        Args:
            en_day (char): Day you need to decode

        Returns:
            char: Decoded form of Day
        '''
        try:
            en_day = int(en_day)
            return en_day
        except:
            return alphabets_list.index(en_day)+10

    def month_decoder(self, en_month):
        '''Decodes Month

        Args:
            en_month (int): Month you need to decode

        Returns:
            int: Decoded form of Month
        '''

        return alphabets_list.index(en_month)+1

    def year_decoder(self, en_year):
        '''Decodes Year

        Args:
            Year (int): Years you need to encode

        Returns:
            int: Decoded form of year
        '''

        return int(str(en_year), 16)+2020

    def full_decoded_date_time_from_datetime(self, en_datetime):
        '''Full date-time decoder

        Args:
            en_datetime (str): Encoded form of date

        Returns:
            list: Decoded form of date and time in this format --> ['Year', 'Month', 'Date', 'Hour(in 24 hr format)', 'Minutes', 'Seconds'] 
        '''

        # [2021, 12, 11, 15, 42, 48]
        # [1,    L,  B,  F,  42, P]

        encoded_datetime_list = [en_datetime[:-6]]
        encoded_datetime_list.append(en_datetime[-6:-5])
        encoded_datetime_list.append(en_datetime[-5:-4])
        encoded_datetime_list.append(en_datetime[-4:-3])
        encoded_datetime_list.append(en_datetime[-3:-1])
        encoded_datetime_list.append(en_datetime[-1])

        decoded_datetime = str(str(self.year_decoder(
            encoded_datetime_list[0]))+'-'+str(self.month_decoder(encoded_datetime_list[1]))+'-'+str(self.day_decoder(encoded_datetime_list[2]))+'-'+str(self.hour_decoder(encoded_datetime_list[-3]))+'-'+str(self.minute_decoder(encoded_datetime_list[-2]))+'-'+str(self.second_decoder(encoded_datetime_list[-1]))).split('-')

        if decoded_datetime[-1] == "60":
            # decoded_datetime[-2] = str(int(decoded_datetime[-2])+1)
            decoded_datetime[-1] = "57"

        # if decoded_datetime[-2] == "60":
        #     decoded_datetime[-3] = str(int(decoded_datetime[-3])+1)
        #     decoded_datetime[-2] = "00"



        return decoded_datetime


if __name__ == "__main__":

    List_of_DateTime = [2021, 12, 11, 15, 42, 48]

    obj = DateTime_Decoder(List_of_DateTime)
    # print(obj.full_encoded_date_time_from_datetime())

    i = -5

    # while i != 65:
    #     print(f"{i} = {obj.year_decoder('12A')}")
    #     i = i+1

    # for i in alphabets_list:
    #     print(f"{i} = {obj.hour_decoder(i)}, {obj.day_decoder(i)}")
    for i in alphabets_list:
        print(f"{i} = {obj.second_decoder(i)}")

    print(f"{obj.full_decoded_date_time_from_datetime('1LVN59A')}")
