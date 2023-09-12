"""
Date ->          2021-12-12
Time ->          17:40:19
Day ->           Sunday
Month Name ->    December
Unix Time ->     1639311019
File Name ->     "main_encoder.py" when created i.e. on 2021-12-12
File Path ->     "C:/Google Drive/Programming/Python/Python tp Projects/Project 12 (Date Time Encoder){Basic}/main_encoder.py" when created i.e. on 2021-12-12

Main file to use for encoding stuff
"""


from datetime import datetime
from encoder_decoder import DateTime_EncoderDecoder
from pyperclip import copy as co
from main_decoder import format_date


if __name__ == "__main__":
    dt = datetime.now().strftime(
        "%Y-%m-%d-%H-%M-%S").split("-")
    encoded_date = DateTime_EncoderDecoder(
        dt).full_encoded_date_time_from_datetime
    print(f"{format_date(dt)}\tEncoded date is {encoded_date}")
    co(str(encoded_date))
    input("Press enter to exit")
