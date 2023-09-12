"""
Date ->          2021-12-12
Time ->          15:31:13
Day ->           Sunday
Month Name ->    December
Unix Time ->     1639303273
File Name ->     "encoder_decoder.py" when created i.e. on 2021-12-12
File Path ->     "C:/Google Drive/Programming/Python/Python tp Projects/Project 12 (Date Time Encoder){Basic}/encoder_decoder.py" when created i.e. on 2021-12-12

Full class of date encoder and decoder
"""
from decoder import DateTime_Decoder
from encoder import DateTime_Encoder
from datetime import datetime


class DateTime_EncoderDecoder(DateTime_Encoder, DateTime_Decoder):
    def __init__(self, List_of_DateTime):
        DateTime_Encoder.__init__(self, List_of_DateTime)


if __name__ == "__main__":

    dt = datetime.now().strftime("%Y-%m-%d-%H-%M-%S").split("-")
    obj = DateTime_EncoderDecoder(dt)
    print(dt)
    encoded_dt = obj.full_encoded_date_time_from_datetime
    print(encoded_dt)
    print(obj.full_decoded_date_time_from_datetime(encoded_dt))

    def unix_to_dt(unix_time=int(datetime.now().timestamp()), format="%Y-%m-%d-%H-%M-%S"):
        return str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(unix_time))).split("-")

    def dt_to_unix(dt=datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), format="%Y-%m-%d-%H-%M-%S"):
        return time.mktime(datetime.strptime(str(dt), format).timetuple())
