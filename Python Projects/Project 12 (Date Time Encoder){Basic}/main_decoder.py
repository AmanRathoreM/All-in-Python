"""
Date ->          2021-12-12
Time ->          17:47:37
Day ->           Sunday
Month Name ->    December
Unix Time ->     1639311457
File Name ->     "main_decoder.py" when created i.e. on 2021-12-12
File Path ->     "C:/Google Drive/Programming/Python/Python tp Projects/Project 12 (Date Time Encoder){Basic}/main_decoder.py" when created i.e. on 2021-12-12

Main file to use for decoding stuff
"""

from datetime import datetime
from pyperclip import copy as co
# from pyperclip import paste as pa
from encoder_decoder import DateTime_EncoderDecoder


def format_date(to_format):
    return str(to_format[2]+'-'+to_format[1]+'-'+to_format[0]+'  '+to_format[-3]+':'+to_format[-2]+':'+to_format[-1])


if __name__ == "__main__":
    # try:
    #     print(pa())
    #     decoded = DateTime_EncoderDecoder(datetime.now().strftime(
    #         "%Y-%m-%d-%H-%M-%S").split("-")).full_decoded_date_time_from_datetime(str(pa()))
    #     decoded = format_date(decoded)
    #     co(decoded)
    #     print(decoded)
    #     decoded = str(DateTime_EncoderDecoder(datetime.now().strftime(
    #         "%Y-%m-%d-%H-%M-%S").split("-")).full_decoded_date_time_from_datetime(input("Please input the Encoded date\n")))
    #     co(decoded)
    #     print(decoded)
    # except:
    decoded = DateTime_EncoderDecoder(datetime.now().strftime(
        "%Y-%m-%d-%H-%M-%S").split("-")).full_decoded_date_time_from_datetime(input("Please input the Encoded date\n"))
    co(format_date(decoded))
    print(format_date(decoded))
    input("Press enter to exit")
